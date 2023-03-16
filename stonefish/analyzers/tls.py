""" Module contain a TLS analyzer """

from stonefish.analyzers.base import BaseAnalyzer
from stonefish.analyzers.normalizers import BinaryStepNormalizer


class TLSAnalyzer(BaseAnalyzer):
    """ TLS analyzer """
    name = 'Проверка SSL'
    description = 'Анализатор проверяет использование SSL/TLS'
    normalizer = BinaryStepNormalizer()

    def execute(self) -> int:
        """ Method execute analyzer and return a points """
        result = 0
        if self.url.scheme == 'https':
            result = 1
        elif self.url.scheme == 'http':
            result = 0
        return result
