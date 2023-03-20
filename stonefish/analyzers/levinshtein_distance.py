""" Levenshtein distance analyzer """

from strsimpy import NormalizedLevenshtein

from stonefish.analyzers.base import BaseAnalyzer
from stonefish.analyzers.trusted_domains import TrustedDomainAnalyzer
from stonefish.analyzers.normalizers import ThNormalizer


class LevenshteinDistanceAnalyzer(BaseAnalyzer):
    """ Levenshtein distance analyzer """
    name = 'Typosquatting'
    description = 'Проверка домена на typosquatting'
    normalizer = ThNormalizer(shift=-0.1, factor=50)

    def execute(self) -> int:
        """ Method execute analyzer and return a points """
        points = 1
        if self.__is_trusted:
            return points
        lev = NormalizedLevenshtein()
        with open('./stonefish/static/top-100000-domains', 'r') as file:
            trusted_domains = file.readlines()
            min_distance = lev.distance(self.url.hostname + '\n', trusted_domains[0])
            for domain in trusted_domains:
                distance = lev.distance(self.url.hostname + '\n', domain)
                if distance < min_distance:
                    min_distance = distance
        return min_distance

    @property
    def __is_trusted(self):
        """ Property return True if domain in trust list """
        return TrustedDomainAnalyzer(self.url.geturl()).execute() == 1
