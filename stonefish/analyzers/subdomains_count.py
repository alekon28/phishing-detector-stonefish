""" Subdomains count analyzer """

from stonefish.analyzers.base import BaseAnalyzer


class SubDomainsCountAnalyzer(BaseAnalyzer):
    """ Subdomains count analyzer """
    name = 'Кол-во поддоменов'
    description = 'Анализ количества поддоменов'
    factor = 1

    def execute(self) -> int:
        """ Method execute analyzer and return a points """
        points = 100
        subdomain_count = len(self.url.hostname.split('.'))
        if subdomain_count < 3:
            subdomain_count = 3
        return points - ((subdomain_count - 3) * 60) if points - ((subdomain_count - 3) * 60) > 0 else 1
