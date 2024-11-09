#!/usr/bin/env python3

from typing import List


class Matrix():
    arr2d: List[List[int]]
    "2d integer list"
    size: int
    "size of 2d integer list"

    def __init__(self, n: int):
        "Creates a matrix of size (2n-1)*(2n-1) filled with zeros."

        if n < 2:
            raise BaseException('n is to small. It should be at least 2.')

        self.arr2d = []
        self.size = 2 * n - 1

        for _ in range(self.size):
            self.arr2d.append([0 for _ in range(self.size)])

    def edges(self, n: int):
        "Creates a border with the number `n`."

        self.arr2d[0] = [n for _ in range(self.size)]

        for i in range(1, self.size - 1):
            self.arr2d[i][0] = n
            self.arr2d[i][self.size - 1] = n

        self.arr2d[self.size - 1] = [n for _ in range(self.size)]

    def diagonal(self, which: int, n: int):
        """
        Parameter `which` is used to choose which diagonal to fill with `n`.

        0: \\        1: /           2: X
        [1, 0, 0]    [0, 0, 1]    [1, 0, 1]
        [0, 1, 0]    [0, 1, 0]    [0, 1, 0]
        [0, 0, 1]    [1, 0, 0]    [1, 0, 1]
        """

        if which not in (0, 1, 2):
            raise BaseException('Wrong `which` parameter')

        if which in (0, 2):
            for i in range(self.size):
                self.arr2d[i][i] = n

        if which in (1, 2):
            for i in range(self.size):
                self.arr2d[self.size - 1 - i][i] = n

    def edges_pattern(self, n: int, start_with_zero=False):
        """
        Creates a border with the number `n`, alternating with 0.

        Parameter `start_with_zero` decides whether the left top corner
        (arr[0][0]) should be 0 or `n`.
        """
        n1, n2 = (0, n) if start_with_zero else (n, 0)

        # this function inherits everything from the parent method
        # `edges_pattern`. It is like arrow functions in JavaScript
        # `const f = () => {}`.
        def run(i: int, j: int, i_inc: bool, k=0):
            """
            Recursive helper function
            `i` - first index of arr2d
            `j` - second index of arr2d
            `i_inc` - whether to increment `i` or `j`
            """

            if i == self.size - 1 and j == self.size - 1:
                return

            if self.size - 1 in (i, j) and 0 in (i, j):
                i_inc = not i_inc

            self.arr2d[i][j] = n2 if k % 2 == 0 else n1
            k += 1

            if i_inc:
                run(i + 1, j, i_inc, k)
            else:
                run(i, j + 1, i_inc, k)

        self.arr2d[0][0] = n1
        self.arr2d[self.size - 1][self.size - 1] = n1

        run(1, 0, True)
        run(0, 1, False)

    def pretty_print(self):
        print('Matrix:')
        for arr in self.arr2d:
            print('[', end='')
            for n in arr:
                if n != 0:
                    print(f'\33[1;35m{n}\33[0m', end=' ')
                else:
                    print(n, end=' ')
            print('\b]')
        print()


def main():
    m = Matrix(6)
    m.pretty_print()
    m.edges(1)
    m.pretty_print()
    m.diagonal(0, 2)
    m.pretty_print()
    m.diagonal(1, 3)
    m.pretty_print()
    m.diagonal(2, 4)
    m.pretty_print()
    m.edges_pattern(5)
    m.pretty_print()

    m = Matrix(3)
    m.edges_pattern(2)
    m.pretty_print()
    m.edges_pattern(3, True)
    m.pretty_print()


if __name__ == '__main__':
    main()
