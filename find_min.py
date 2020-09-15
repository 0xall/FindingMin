import argparse

from matplotlib import pyplot as plt

from decimal import Decimal
from polynomial import Polynomial
from root import get_newton_raphson
from root.approximation import get_min_approximation, get_min_approximation_with_momentum
from visualization import visualize_newton_iteration

args = argparse.ArgumentParser()
args.add_argument('coefficients', type=str, nargs='+', help='Coefficient list for polynomial')
args.add_argument('--floating-points', '-f', type=int, default=10, metavar='N', help='The number of floating points to use.')
args.add_argument('--start', '-s', type=str, help='The starting point x')
args.add_argument('--visual', '-v', action='store_true', help='Visualize iteration')
args.add_argument('--approximation', type=str, help='Using approximation using interval h')
args.add_argument('--count', '-n', default=8, type=int, help='iterates maximum N')
args.add_argument('--with-momentum', action='store_true', help='Add momentum for approximation method.')


if __name__ == '__main__':
    args = args.parse_args()

    def visualize_if_visual_option_true(p, x, step=0):
        if args.visual:
            visualize_newton_iteration(p=p, x=x, step=step)
            plt.show()

    # changes decimal floating points before calculating.
    Decimal.change_floating_points(args.floating_points)

    # constructs polynomial function from the parameter.
    polynomial = Polynomial(*args.coefficients)

    first_diff = polynomial.differential()
    second_diff = first_diff.differential()

    # print polynomial, 1st derivative and 2nd derivative forms.
    print('Polynomial     :', polynomial)

    if not args.approximation:
        print('1st Derivative :', first_diff)
        print('2nd Derivative :', second_diff)

    x = Decimal(args.start)

    if args.approximation:
        print(f'Using approximation with interval h = {args.approximation}')
        approximation = abs(Decimal(args.approximation))

        visualize_if_visual_option_true(polynomial, x)

        prev_x = x
        for i in range(args.count):
            _prev_x = x

            if args.with_momentum:
                x = get_min_approximation_with_momentum(polynomial, x, approximation, prev_x)
            else:
                x = get_min_approximation(polynomial, x, approximation)
            prev_x = _prev_x
            visualize_if_visual_option_true(polynomial, x, step=i + 1)
    else:
        # visualize before iteration.
        visualize_if_visual_option_true(polynomial, x)

        # visualize per iterations.
        for i in range(args.count):
            x, _ = get_newton_raphson(first_diff, x, 1)
            visualize_if_visual_option_true(polynomial, x, step=i + 1)

    print(f'x for local minimum : {x}')
    print(f'local minimum : {polynomial(x)}')