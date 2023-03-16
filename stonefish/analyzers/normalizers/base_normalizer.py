""" Base normalizer """

from abc import ABCMeta, abstractmethod


class BaseNormalizer(metaclass=ABCMeta):
    """ Base normalizer """
    def __init__(self, /, *, shift=0, factor=1):
        """ Initializing """
        self.shift = shift
        self.factor = factor

    @abstractmethod
    def __call__(self, x: float) -> float:
        """ Normalizer function return value from 0 to 1 """
