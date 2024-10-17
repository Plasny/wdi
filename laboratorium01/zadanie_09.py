#!/usr/bin/env python3

from enum import Enum
from typing import Callable


class Operations(Enum):
    deposit = 'wpłata'
    withdrawal = 'wypłata'
    balance = 'sprawdź saldo'
    exit = 'zakończ program'


class Bankomat():
    balance: float = 0
    pin: str

    def __init__(self, pin: str = '0000'):
        self.pin = pin

    @staticmethod
    def check_pin(func: Callable):
        def wrapper(*args):
            self = args[0]

            try:
                user_pin = input('Wprowadź PIN: ')
            except Exception:
                exit()

            if self.pin != user_pin:
                print('Nieprawidłowy PIN')
                return

            func(self)
        return wrapper

    @staticmethod
    def enter_amount(func: Callable):
        def wrapper(*args):
            self = args[0]

            try:
                amount = input('Wprowadź kwotę: ')
            except Exception:
                exit()

            try:
                amount = float(amount)
            except Exception:
                print('Wprowadzono złą kwotę')
                return

            if amount != round(amount, 2):
                print('Wprowadzono złą kwotę')
                return

            func(self, amount)
        return wrapper

    @check_pin
    def show_balance(self):
        print(f'Aktualny stan konta to {self.balance}')

    @check_pin
    @enter_amount
    def deposit(self, n: int | float = 0):
        self.balance += n
        print(f'Wpłacono {n}, aktualny stan konta to {self.balance}')

    @check_pin
    @enter_amount
    def withdrawal(self, n: int | float = 0):
        if self.balance - n > 0:
            self.balance -= n
            print(f'Wypłacono {n}, pozostałe środki to {self.balance}')
        else:
            print('Nie posiadasz wywstarczającej ilości środków na koncie.')


def input_operation(b: Bankomat):
    while True:
        try:
            user_input = input('Wprowadź operacje: ')
        except KeyboardInterrupt:
            print('\nBye')
            exit()

        if user_input not in Operations:
            print('Błędna operacja. '
                  f'Możliwe operacje to: {[op.value for op in Operations]}')
            continue

        match user_input:
            case Operations.balance.value:
                b.show_balance()
            case Operations.exit.value:
                break
            case Operations.withdrawal.value:
                b.withdrawal()
            case Operations.deposit.value:
                b.deposit()

        print('\nCo chcesz zrobić w kolejnym kroku?')


def main():
    print('Początkowy PIN to 0000\n')
    bankomat = Bankomat('0000')
    input_operation(bankomat)


if __name__ == '__main__':
    main()
