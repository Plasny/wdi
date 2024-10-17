#!/usr/bin/env python3

import random


operations = frozenset(['-', '+', '*', '/', '#', '^', 'x'])


def perform_operation(op: str, arr: list[float]) -> bool:
    match op:
        case '+':
            n = sum(arr)
            print(f'Suma {arr} wynosi: {n}')
        case '-':
            i = arr[0]
            for n in arr[1:]:
                i -= n
            print(f'Różnica {arr} wynosi: {i}')
        case '*':
            i = arr[0]
            for n in arr[1:]:
                i *= n
            print(f'Iloczyn {arr} wynosi: {i}')
        case '/':
            i = arr[0]
            for n in arr[1:]:
                i /= n
            print(f'Iloraz {arr} wynosi: {i}')
        case '#':
            i = arr[0]
            for n in arr[1:]:
                i **= n
            print(f'Potęgowanie {arr} wynosi: {i}')
        case '^':
            i = arr[0]
            for n in arr[1:]:
                i **= 1/n
            print(f'Pierwiastkowanie {arr} wynosi: {i}')
        case 'x':
            print(f'Losowa liczba: {random.random()}')

    user_in = input('Czy chcesz wprowadzić nowe dane? ')

    if user_in == 'T':
        return True

    return False


def main():
    arr = []

    while True:
        user_in = input()
        try:
            num = float(user_in)
        except Exception:
            if user_in not in operations:
                print('Wrong input')
                continue

            if not perform_operation(user_in, arr):
                exit()

            arr = []
            continue

        arr.append(num)


if __name__ == '__main__':
    main()
