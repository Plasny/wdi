#!/usr/bin/env python3

from typing import List, Tuple

SIZE = 40


dane_g = [(33, 22), (6, 18), (7, 19)]
dane_w = [(32, 20), (30, 20), (28, 20)]
dane_h = [(3, 3), (4, 4), (32, 21)]
dane_s = [(12, 13), (5, 20), (4, 22)]


def visualiseFn(
    data_g: List[Tuple[int, int]] = [],
    data_h: List[Tuple[int, int]] = [],
    data_s: List[Tuple[int, int]] = [],
    data_w: List[Tuple[int, int]] = [],
    stars=True
) -> None:
    t = [[' ' for _ in range(SIZE)] for _ in range(SIZE)]

    for e in data_g:
        # goniec
        t[e[1]][e[0]] = 'G'

    for e in data_w:
        # wieża
        t[e[1]][e[0]] = 'W'

    for e in data_h:
        # hetman
        t[e[1]][e[0]] = 'H'

    for e in data_s:
        # skoczek
        t[e[1]][e[0]] = 'S'

    if stars:
        for e in data_g:
            for i in range(SIZE):
                for j in range(SIZE):
                    if abs(i - e[1]) == abs(j - e[0]) and t[i][j] == ' ':
                        t[i][j] = '*'

        for e in data_w:
            for i in range(SIZE):
                for j in range(SIZE):
                    if (i == e[1] or j == e[0]) and t[i][j] == ' ':
                        t[i][j] = '*'

        for e in data_h:
            for i in range(SIZE):
                for j in range(SIZE):
                    if abs(i - e[1]) == abs(j - e[0]) and t[i][j] == ' ':
                        t[i][j] = '*'
                    if (i == e[1] or j == e[0]) and t[i][j] == ' ':
                        t[i][j] = '*'

        for e in data_s:
            s_moves = [(-2, -1), (-2, 1), (2, -1), (2, 1),
                       (-1, -2), (-1, 2), (1, -2), (1, 2)]
            for m in s_moves:
                try:
                    if t[e[1] + m[0]][e[0] + m[1]] == ' ':
                        t[e[1] + m[0]][e[0] + m[1]] = '*'
                except IndexError:
                    pass

    print('')
    print('    ', end='')
    for i in range(SIZE):
        print((i // 10) % 10, end='')
    print('\n    ', end='')
    for i in range(SIZE):
        print(i % 10, end='')
    print('\n   ', end='')
    print('-' * (SIZE + 2))
    for i in range(SIZE):
        print('%02d |' % i,  end='')
        for j in range(SIZE):
            print(t[i][j], end='')
        print('|')
    print('   ', end='')
    print('-' * (SIZE + 2))
    print('')


def check_s(
    dane_s: List[Tuple[int, int]],
    visualise=False
) -> List[Tuple[Tuple[int, int], Tuple[int, int]]]:
    out = []
    # skoczek nie może bić się wzajemnie z figurą inną niż skoczek

    s_moves = [(-2, -1), (-2, 1), (2, -1), (2, 1),
               (-1, -2), (-1, 2), (1, -2), (1, 2)]
    for i, e1 in enumerate(dane_s):
        for e2 in dane_s[i+1:]:
            for m in s_moves:
                if (e1[0] + m[0], e1[1] + m[1]) == e2:
                    out.append((e1, e2))
                    print(f'Skoczki na {e1} i {e2} mogą się bić.')

    if visualise:
        visualiseFn(data_s=dane_s)

    return out


def check_g(
    dane_g: List[Tuple[int, int]],
    dane_h: List[Tuple[int, int]],
    visualise=False
) -> List[Tuple[Tuple[int, int], Tuple[int, int]]]:
    out = []

    # goniec nie może bić się wzajemnie z figurą inną niż goniec lub hetman
    for i, e1 in enumerate(dane_g):
        for e2 in dane_h:
            if abs(e1[0] - e2[0]) == abs(e1[1] - e2[1]):
                print(f'Goniec na {e1} i hetman na {e2} mogą się bić.')
                out.append((e1, e2))
        for e2 in dane_g[i+1:]:
            if abs(e1[0] - e2[0]) == abs(e1[1] - e2[1]):
                print(f'Gońce na {e1} i {e2} mogą się bić.')
                out.append((e1, e2))

    if visualise:
        visualiseFn(data_g=dane_g, data_h=dane_h)

    return out


def check_w(
    dane_w: List[Tuple[int, int]],
    dane_h: List[Tuple[int, int]],
    visualise=False
) -> List[Tuple[Tuple[int, int], Tuple[int, int]]]:
    out = []

    # wieża nie może bić się wzajemnie z figurą inną niż wieża lub hetman
    for i, e1 in enumerate(dane_w):
        for e2 in dane_h:
            if e1[0] == e2[0] or e1[1] == e2[1]:
                print(f'Wieża na {e1} i hetman na {e2} mogą się bić.')
                out.append((e1, e2))
        for e2 in dane_w[i+1:]:
            if e1[0] == e2[0] or e1[1] == e2[1]:
                print(f'Wieże na {e1} i {e2} mogą się bić.')
                out.append((e1, e2))

    if visualise:
        visualiseFn(data_w=dane_w, data_h=dane_h)

    return out


def check_h(
    dane_h: List[Tuple[int, int]],
    visualise=False
) -> List[Tuple[Tuple[int, int], Tuple[int, int]]]:
    out = []
    for i, e1 in enumerate(dane_h):
        for e2 in dane_h[i+1:]:
            if (
                abs(e1[0] - e2[0]) == abs(e1[1] - e2[1])
                or e1[0] == e2[0] or e1[1] == e2[1]
            ):
                out.append((e1, e2))
                print(f'Hetmany na {e1} i {e2} mogą się bić.')

    if visualise:
        visualiseFn(data_h=dane_h)

    return out


def main():
    vAll = False
    check_s(dane_s, visualise=vAll)
    check_g(dane_g, dane_h, visualise=vAll)
    check_w(dane_w, dane_h, visualise=vAll)
    check_h(dane_h, visualise=vAll)
    visualiseFn(data_g=dane_g, data_h=dane_h, data_s=dane_s, data_w=dane_w)


if __name__ == '__main__':
    main()
