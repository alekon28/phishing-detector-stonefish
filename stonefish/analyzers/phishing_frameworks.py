""" Analyzer for detecting known phishing frameworks """

import requests

from stonefish.analyzers.base import BaseAnalyzer
from stonefish.analyzers.normalizers import BinaryStepNormalizer


class PhishingFrameworkAnalyzer(BaseAnalyzer):
    """ Analyzer for detecting known phishing frameworks """
    name = 'Фреймворки'
    description = 'Маркеры использования известных фреймворков для фишинга'
    normalizer = BinaryStepNormalizer()

    def execute(self) -> int:
        """ Method execute analyzer and return a points from 1 to 100 """
        points = 0
        try:
            requests.get(f'{self.url.scheme}://{self.url.hostname}:3333/')
        except Exception as err:
            points = 1
        finally:
            return points
