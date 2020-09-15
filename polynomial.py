from functools import reduce
from typing import List

from decimal import Decimal


class Polynomial:
    """
    Represents polynomial function. It supports the calculating value in x and
    getting differential of polynomial function.
    """
    def __init__(self, *args: Decimal):
        if len(args) == 0:
            # if no polynomial arguments (it means no coefficient), it's 0-degree polynomial (y = 0)
            self.coefficients = [Decimal()]
        else:
            self.coefficients = list(reversed([Decimal(arg) for arg in args]))

    def __call__(self, x: Decimal):
        """
        Returns the value from the polynomial with x.
        :param x: the value.
        :return: calculated from the polynomial with x.
        """
        return reduce(
            lambda prev, value: prev + value[1] * (x ** value[0]),
            enumerate(self.coefficients),
            Decimal()
        )

    def __repr__(self):
        def coefficient_str(d: Decimal, is_first: bool = False):
            int_part, float_part = str(d).split('.')

            i = 0
            for c in reversed(float_part[1:]):
                if c != '0':
                    break
                i += 1

            float_part = float_part[:len(float_part) - i]
            if is_first:
                sign = d.sign
                if sign == '+':
                    sign = ''
                return f'{sign}{abs(int(int_part))}.{float_part}'
            else:
                return f' {d.sign} {abs(int(int_part))}.{float_part}'

        def variable_str(n: int):
            if n == 0:
                return ''
            elif n == 1:
                return 'x'
            else:
                return f'x^{n}'

        builder = [f'{coefficient_str(coefficient, level == len(self.coefficients) - 1)} {variable_str(level)}'
                   for level, coefficient
                   in enumerate(self.coefficients)]

        return ''.join(reversed(builder))

    def differential(self):
        """
        Returns the differential polynomial object.
        :return: the differential polynomial.
        """
        return Polynomial(*reversed([(coefficient * (degree + 1)) for degree, coefficient in enumerate(self.coefficients[1:])]))
