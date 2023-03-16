""" Subdomains count analyzer """

from stonefish.analyzers.base import BaseAnalyzer
from stonefish.analyzers.normalizers import ThNormalizer


class SubDomainsCountAnalyzer(BaseAnalyzer):
    """ Subdomains count analyzer """
    name = 'Кол-во поддоменов'
    description = 'Анализ количества поддоменов'
    normalizer = ThNormalizer(shift=-4, factor=-0.5)

    def execute(self) -> int:
        """ Method execute analyzer and return a points """
        return len(self.url.hostname.split('.'))
