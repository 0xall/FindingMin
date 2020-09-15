from decimal import Decimal

from polynomial import Polynomial


def get_min_approximation(polynomial: Polynomial, x: Decimal, h: Decimal):
    """
    Gets the root value by using Newton-Raphson method.

    :param polynomial: the polynomial function for calculating the root.
    :param start: start position for Newton-Raphson method.
    :param count: the maximum number of iteration.

    :return: the root value found and error (%)
    """

    # get function value.
    poly_x = polynomial(x)

    gradient = (polynomial(x + h) - poly_x) / h
    gradient_2 = (polynomial(x + h) - Decimal(2) * polynomial(x) + polynomial(x - h)) / (h ** 2)

    return x - gradient / gradient_2 if gradient_2 != Decimal(0) else x


def get_min_approximation_with_momentum(polynomial: Polynomial, x: Decimal, h: Decimal, prev_x: Decimal):
    """
    Gets the root value by using Newton-Raphson method.

    :param polynomial: the polynomial function for calculating the root.
    :param start: start position for Newton-Raphson method.
    :param count: the maximum number of iteration.

    :return: the root value found and error (%)
    """

    # get function value.
    poly_x = polynomial(x)

    gradient = (polynomial(x + h) - poly_x) / h
    gradient_2 = (polynomial(x + h) - Decimal(2) * polynomial(x) + polynomial(x - h)) / (h ** 2)

    return x - gradient / gradient_2 + (x - prev_x) * Decimal('0.2') if gradient_2 != Decimal(0) else x
