""" Binary step normalizer """

from stonefish.analyzers.normalizers.base_normalizer import BaseNormalizer


class BinaryStepNormalizer(BaseNormalizer):
    """ Binary step normalizer """
    def __call__(self, x: float) -> float:
        """ Normalizer function return value from 0 to 1 """
        return 1 if x + self.shift > 0 else 0
