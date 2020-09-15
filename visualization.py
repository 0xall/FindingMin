from decimal import Decimal
from typing import Tuple

from polynomial import Polynomial

import numpy as np
from matplotlib import pyplot as plt


def visualize_polynomial(p: Polynomial, interval: Tuple[str, str]):
    x = np.linspace(float(interval[0]), float(interval[1]), 100)
    y = np.zeros(len(x))

    for level, coefficient in enumerate(p.coefficients):
        y += float(coefficient) * (x ** level)

    plt.axhline(y=0, color='lightgray')
    plt.axvline(x=0, color='lightgray')
    plt.plot(x, y)
    plt.xlim(float(interval[0]), float(interval[1]))


def visualize_newton_iteration(p: Polynomial, x: Decimal, step: int = 0):
    diff = p.differential()
    gradient = diff(x)
    gradient_polynomial = Polynomial(gradient, - gradient * x + p(x))

    plt.subplot(2, 1, 1)
    plt.title(f'STEP {step} (x = {x}, y = {p(x)})')
    visualize_polynomial(p, (x - 1, x + 1))
    visualize_polynomial(gradient_polynomial, (x - 1, x + 1))
    plt.plot(float(x), float(p(x)), 'bo')

    plt.subplot(2, 1, 2)
    visualize_polynomial(diff, (x - 1, x + 1))
    plt.plot(float(x), float(diff(x)), 'bo')
