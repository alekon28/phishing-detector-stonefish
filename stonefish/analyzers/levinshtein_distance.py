""" Levenshtein distance analyzer """

from strsimpy import NormalizedLevenshtein

from stonefish.analyzers.trusted_domains import TrustedDomainAnalyzer


class LevenshteinDistanceAnalyzer(TrustedDomainAnalyzer):
    """ Levenshtein distance analyzer """
    name = 'Typosquatting'
    description = 'Проверка домена на typosquatting'
    factor = 1

    def execute(self) -> int:
        """ Method execute analyzer and return a points """
        points = 100
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
            if 0 <= min_distance <= 0.15:
                points = 10
        return points

    @property
    def __is_trusted(self):
        """ Property return True if domain in trust list """
        return super().execute() == 100
