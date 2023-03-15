""" Module contain a TLS analyzer """

from stonefish.analyzers.base import BaseAnalyzer


class TLSAnalyzer(BaseAnalyzer):
    """ TLS analyzer """
    name = 'Проверка SSL'
    description = 'Анализатор проверяет использование SSL/TLS'
    factor = 1

    def execute(self) -> int:
        """ Method execute analyzer and return a points """
        result = 50
        if self.url.scheme == 'https':
            result = 100
        elif self.url.scheme == 'http':
            result = 20
        return result
