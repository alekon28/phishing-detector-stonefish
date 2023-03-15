""" Digits count analyzer """

from stonefish.analyzers.base import BaseAnalyzer


class DigitsCountAnalyzer(BaseAnalyzer):
    """ Digits count analyzer """
    name = 'Кол-во цифр'
    description = 'Анализ количества цифр в доменном имени'
    factor = 1

    def execute(self) -> int:
        """ Method execute analyzer and return a points """
        points = 100
        digits_count = 0
        for symbol in self.url.hostname:
            if symbol.isdigit():
                digits_count += 1

        return points - digits_count * 10 if (points - digits_count * 10) > 1 else 1
