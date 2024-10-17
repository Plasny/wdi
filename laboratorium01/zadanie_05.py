#!/usr/bin/env python3

from sys import stderr


def get_num_from_user(description: str, only_int: bool = False):
    while True:
        user_num = input(description)

        try:
            num = int(user_num)
            break
        except:  # noqa
            print("Podana liczba jest nieprawidłowa.", file=stderr)

            if only_int:
                continue

            try:
                num = float(user_num)
                break
            except:  # noqa
                continue

    return num


def main():
    num = get_num_from_user("Wprowadzona przez Ciebie liczba to ")
    print(num)


if __name__ == '__main__':
    main()
