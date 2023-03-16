""" Sigmoid based on hyperbolic tangent function """

from math import exp

from stonefish.analyzers.normalizers.base_normalizer import BaseNormalizer


class ThNormalizer(BaseNormalizer):
    """ Normalizer based on hyperbolic tangent function """
    def __call__(self, x: float) -> float:
        return 1 / (1 + exp((x + self.shift) * self.factor))
