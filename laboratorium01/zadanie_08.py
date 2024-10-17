#!/usr/bin/env python3

import random
from zadanie_05 import get_num_from_user


def print_row(space: int, stars: int):
    for _ in range(0, space):
        print(' ', end='')
    if stars == 1:
        print('X')
    else:
        # TODO something better
        rn = random.randint(0, stars - 1)
        for n in range(0, stars):
            if n == rn:
                print('o', end='')
            else:
                print('*', end='')
        print()


def main():
    size = int(get_num_from_user("Podaj rozmiar choinki ", only_int=True))
    ozdoby = True
    i = 1
    j = size - 1

    while i / 2 < size:
        if ozdoby:
            print_row(j, i)
        else:
            print(' ' * j, '*' * i, sep='')

        i += 2
        j -= 1

    print(' ' * (size - 1), 'U', sep='')


if __name__ == '__main__':
    main()
