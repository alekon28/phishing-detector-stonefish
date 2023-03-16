""" Module contain a BaseAnalyzer class """

from abc import ABCMeta, abstractmethod
from urllib.parse import urlparse
import logging

from stonefish.models.analyzer import AnalyzerVerdictModel
from stonefish.analyzers.normalizers import ThNormalizer


class BaseAnalyzer(metaclass=ABCMeta):
    """ Base analyzer """
    name = 'Base analyzer'
    description = 'Analyzer for implements other analyzers'
    normalizer = ThNormalizer(shift=0, factor=1)
    weight = 1

    def __init__(self, url):
        """ Initialize """
        self.url = urlparse(url)

    @abstractmethod
    def execute(self) -> int:
        """ Method execute analyzer and return a points """
        raise NotImplementedError()

    def analyze(self) -> AnalyzerVerdictModel:
        """ Method execute analyzer and return a verdict """
        points = 0
        success = False
        try:
            points = self.execute()
            success = True
        except Exception as err:
            logging.getLogger('__app__').warning(f'Analyzer "{self.__class__}" was crashed with exception: "{err}"',
                                                 exc_info=True)
        return AnalyzerVerdictModel(
            points=points,
            weight=self.weight,
            result=self.normalizer(points),
            name=self.name,
            description=self.description,
            success=success
        )
