""" Analyzer for trusted domains """

from stonefish.analyzers.base import BaseAnalyzer
from stonefish.analyzers.normalizers import BinaryStepNormalizer


class TrustedDomainAnalyzer(BaseAnalyzer):
    """ Analyzer for trusted domains"""
    name = 'Доверенный домен'
    description = 'Находится ли домен в списке доверенных'
    normalizer = BinaryStepNormalizer()

    def execute(self) -> int:
        """ Method execute analyzer and return a points """
        with open('./stonefish/static/top-1000000-domains', 'r') as file:
            points = 0
            trusted_domains = file.readlines()
            if '.'.join(self.url.hostname.split('.')[-2:]) + '\n' in trusted_domains:
                points = 1
            return points
