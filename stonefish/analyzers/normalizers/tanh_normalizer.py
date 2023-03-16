""" Normalizer based on hyperbolic tangent function """

from math import tanh

from stonefish.analyzers.normalizers.base_normalizer import BaseNormalizer


class ThNormalizer(BaseNormalizer):
    """ Normalizer based on hyperbolic tangent function """
    def __call__(self, x: float) -> float:
        return tanh((x + self.shift) * self.factor) * 0.5 + 0.5
