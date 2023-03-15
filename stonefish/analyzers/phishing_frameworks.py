""" Analyzer for detecting known phishing frameworks """

import requests

from stonefish.analyzers.base import BaseAnalyzer


class PhishingFrameworkAnalyzer(BaseAnalyzer):
    """ Analyzer for detecting known phishing frameworks """
    name = 'Фреймворки'
    description = 'Маркеры использования известных фреймворков для фишинга'
    factor = 1

    def execute(self) -> int:
        """ Method execute analyzer and return a points from 1 to 100 """
        points = 10
        try:
            requests.get(f'{self.url.scheme}://{self.url.hostname}:3333/')
        except Exception as err:
            points = 100
        finally:
            return points
