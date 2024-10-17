#!/usr/bin/env python3

from zadanie_05 import get_num_from_user


def main():
    start = int(get_num_from_user("Podaj liczbę 1 ", only_int=True))
    end = int(get_num_from_user("Podaj liczbę 2 ", only_int=True))

    if start > end:
        (start, end) = (end, start)

    if (size := end - start) > 20:
        middle = (start + size) // 2
        for n in range(middle - 3, middle + 3):
            print(n)
        return

    i = start
    while i <= end:
        print(i)
        i += 1


if __name__ == '__main__':
    main()
