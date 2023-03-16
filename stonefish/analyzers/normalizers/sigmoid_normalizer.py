""" Sigmoid based on sigmoid function """

from math import exp

from stonefish.analyzers.normalizers.base_normalizer import BaseNormalizer


class SigmoidNormalizer(BaseNormalizer):
    """ Sigmoid based on sigmoid function """
    def __call__(self, x: float) -> float:
        return 1 / (1 + exp((x + self.shift) * self.factor))
