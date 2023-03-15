""" Analyzer for trusted domains """

from stonefish.analyzers.base import BaseAnalyzer


class TrustedDomainAnalyzer(BaseAnalyzer):
    """ Analyzer for trusted domains"""
    name = 'Доверенный домен'
    description = 'Находится ли домен в списке доверенных'
    factor = 1

    def execute(self) -> int:
        """ Method execute analyzer and return a points """
        with open('./stonefish/static/top-1000000-domains', 'r') as file:
            points = 50
            trusted_domains = file.readlines()
            if '.'.join(self.url.hostname.split('.')[-2:]) + '\n' in trusted_domains:
                points = 100
            return points
