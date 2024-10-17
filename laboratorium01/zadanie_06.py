#!/usr/bin/env python3

from zadanie_05 import get_num_from_user

"""
    Komentarz
    który
    jest
    w
    wielu
    liniach
"""

# komentarz który jest w jednej linijce


def check_nums(num1: int | float, num2: int | float) -> tuple[int | float,
                                                              int | float]:
    if num1 < 0 and num2 < 0:
        print('Obie liczby mniejsze od zera. Kończę program.')
        exit()

    if num1 < 0:
        num1 = abs(num1)

    if num2 < 0:
        num2 = abs(num1)

    return (num1, num2)


def main():
    num1 = get_num_from_user("Podaj liczbę 1 ")
    num2 = get_num_from_user("Podaj liczbę 2 ")
    (num1, num2) = check_nums(num1, num2)

    print(f'num1 = {num1}, num2 = {num2}')
    print(f'Suma podanych liczb: {num1 + num2}')
    print(f'Różnica podanych liczb: {num1 - num2}')
    if (n := num1 * num2) == 10:
        print(f'Iloczyn podanych liczb: {n} Yay!')
    else:
        print(f'Iloczyn podanych liczb: {n}')
    print(f'Iloraz podanych liczb: {num1 / num2}')
    print(f'Kwadraty podanych liczb: {num1**2}, {num2**2}')
    print(f'Pierwiastki podanych liczb: {num1**0.5}, {num2**0.5}')


if __name__ == '__main__':
    main()
