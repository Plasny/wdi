#!/usr/bin/env python3

import datetime


def calculate_age(birth_date: datetime.date,
                  current_date: datetime.date = datetime.date.today()):
    age = current_date.year - birth_date.year

    if (current_date.month < birth_date.month
            and current_date.day < birth_date.day):
        age -= 1

    return age


def main():
    name = "Paweł Pasternak"
    birth_date = datetime.date(2004, 9, 9)
    current_date = datetime.date.today()
    age = calculate_age(birth_date, current_date)

    print(name)
    print(age)


if __name__ == '__main__':
    main()
