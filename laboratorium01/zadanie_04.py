#!/usr/bin/env python3

import datetime
from zadanie_02 import calculate_age


def no_variables_muliple_prints():
    print('Paweł')
    print('Pasternak')
    print(calculate_age(datetime.date(2004, 9, 9)))
    print('Pizza')
    print('Pies')
    print('%.1f' % (5 / 7), end=',')
    print('%.3f' % (5 / 7), end=',')
    print('%.5f' % (5 / 7), end=',')
    print('%.10f' % (5 / 7))


def variables_single_print():
    name = 'Paweł'
    surname = 'Pasternak'
    age = calculate_age(datetime.date(2004, 9, 9))
    favourite_food = 'Pizza'
    favourite_animal = 'Pies'
    num = 5 / 7

    p_str = f"""
{name}
{surname}
{age}
{favourite_food}
{favourite_animal}
{round(num, 1)},{round(num, 3)},{round(num, 5)},{round(num, 10)}
"""

    print(p_str)


def main():
    no_variables_muliple_prints()
    variables_single_print()


if __name__ == '__main__':
    main()
