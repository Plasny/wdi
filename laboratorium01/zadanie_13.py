#!/usr/bin/env python3

def fx(x0: float, x1: float) -> float:
    # for sqrt -> x0**2 - x1
    return x0**3 - x1


def fx_prim(x: float) -> float:
    # for sqrt -> 2 * x
    return 3 * x**2


def sqrt3(n1: float, eps: float, verbose=False) -> float:
    n0 = 1.0

    if verbose:
        print('\n  Wzór Newtona-Raphsona (na pierwiastek 3 stopnia):')
        print('  x_k+1 = x_k - (f(x_k) - a)/f\'(x_k)')
        print('  x_k+1 = x_k - (x_k**3 - a)/(3 * x_k**2)\n')

    while (abs(n0**3 - n1) > eps):
        x_k1 = n0 - fx(n0, n1) / fx_prim(n0)

        if verbose:
            print(f'  x_k = {n0}, f(x_k)={fx(n0, n1)}, f\'(x_k)={fx_prim(n0)}')
            print(f'  {x_k1} = {n0} - {fx(n0, n1)} / {fx_prim(n0)}')
            print(f'  x_k1 = {x_k1}\n')

        n0 = x_k1

    if verbose:
        print('')

    return n0


def round_number_to_eps(n: float, eps: float):
    i = 0

    while (eps < 1):
        eps *= 10
        i += 1

    return int(n * 10**i) / 10**i


def main():
    eps = 0.000001
    n = float(input('Wprowadź liczbę, której pierwiastek 3 stopnia'
                    'chcesz obliczyć '))

    # v = sqrt3(n, eps, verbose=True)
    v = sqrt3(n, eps)
    v = round_number_to_eps(v, eps)
    print(f'Pierwiastek trzeciego stopnia z {n} jest równy {v}, z dokładnością'
          f' wynoszącą {eps}')


if __name__ == '__main__':
    main()
