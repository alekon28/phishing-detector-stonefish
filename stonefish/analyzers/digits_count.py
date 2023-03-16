""" Digits count analyzer """

from stonefish.analyzers.base import BaseAnalyzer
from stonefish.analyzers.normalizers import ThNormalizer


class DigitsCountAnalyzer(BaseAnalyzer):
    """ Digits count analyzer """
    name = 'Кол-во цифр'
    description = 'Анализ количества цифр в доменном имени'
    normalizer = ThNormalizer(shift=-4, factor=-0.5)

    def execute(self) -> int:
        """ Method execute analyzer and return a points """
        digits_count = 0
        for symbol in self.url.hostname:
            if symbol.isdigit():
                digits_count += 1

        return digits_count
