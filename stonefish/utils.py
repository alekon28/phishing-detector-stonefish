""" Module contain utils """

from uuid import uuid4, UUID
from datetime import timedelta
import logging

from fastapi import BackgroundTasks, HTTPException
import requests

from stonefish.models.analyzer import AnalyzersOutcomeModel
from stonefish.models.api import ResultResponseModel, AnalyzeResponseModel
from stonefish.redis_client import RedisClient
from stonefish.analyzers import (
    TLSAnalyzer,
    DnsVerificationTagsAnalyzer,
    TrustedDomainAnalyzer,
    LevenshteinDistanceAnalyzer,
    DigitsCountAnalyzer,
    SubDomainsCountAnalyzer,
)


class Utils:
    """ Utils """
    def __init__(self):
        self.analyzers = [
            TLSAnalyzer,
            DnsVerificationTagsAnalyzer,
            TrustedDomainAnalyzer,
            LevenshteinDistanceAnalyzer,
            DigitsCountAnalyzer,
            SubDomainsCountAnalyzer,
        ]
        self.redis = RedisClient()

    def run_analyzers(self, url: str, bg_tasks: BackgroundTasks) -> AnalyzeResponseModel:
        """ Method run all analyzers """
        if not self._is_valid_url(url):
            raise HTTPException(400, 'Ресурс недоступен или указан неверный URL')
        session_id = uuid4()
        self.redis.client.set(str(session_id), ResultResponseModel(
            url=url, complete=False, details=[], outcome=AnalyzersOutcomeModel()
        ).json())
        bg_tasks.add_task(self._collect_analyzer_results, session_id, url)
        return AnalyzeResponseModel(session_id=session_id)

    def get_result(self, session_id) -> ResultResponseModel:
        """ Method return analyzer results """
        return ResultResponseModel.parse_raw(self.redis.client.get(str(session_id)))

    def _collect_analyzer_results(self, session_id: UUID, url: str):
        """ Method collect analyzers results """
        for analyzer in self.analyzers:
            result = analyzer(url).analyze()
            existing_result = ResultResponseModel.parse_raw(self.redis.client.get(str(session_id)))
            existing_result.details.append(result)
            self.redis.client.set(str(session_id), existing_result.json())
        existing_result = ResultResponseModel.parse_raw(self.redis.client.get(str(session_id)))
        existing_result.outcome = self._make_outcome(existing_result)
        existing_result.complete = True
        self.redis.client.set(str(session_id), existing_result.json(), timedelta(seconds=300))

    def _make_outcome(self, results: ResultResponseModel):
        """ Method return outcome """
        result_sum, result_sum_max, result_sum_weight, result_sum_weight_max, success_completed = 0, 0, 0, 0, 0
        for res in results.details:
            if res.success:
                result_sum += res.result
                result_sum_max += 1
                result_sum_weight += res.result * res.weight
                result_sum_weight_max += 1 * res.weight
                success_completed += 1
        return AnalyzersOutcomeModel(
            points=result_sum * 100 if success_completed > 0 else 0,
            points_max=result_sum_max * 100 if success_completed > 0 else 0,
            result=result_sum_weight * 100 if success_completed > 0 else 0,
            result_max=result_sum_weight_max * 100 if success_completed > 0 else 0,
            score=result_sum_weight / result_sum_weight_max * 100 if success_completed > 0 else 0
        )

    def _is_valid_url(self, url):
        """ Method check connection """
        try:
            requests.get(url)
            return True
        except Exception as err:
            logging.getLogger('__app__').info(f'Url "{url}" is invalid. Reason: "{err}"')
            return False
