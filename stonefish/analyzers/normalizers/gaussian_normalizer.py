""" Normalizer based on Gaussian function """

from math import exp

from stonefish.analyzers.normalizers.base_normalizer import BaseNormalizer


class GaussianNormalizer(BaseNormalizer):
    """ Normalizer based on Gaussian function """
    def __call__(self, x: float) -> float:
        """ Normalizer function return value from 0 to 1 """
        return exp(((-x + self.shift) * self.factor) ** 2)
