#!/usr/bin/env python3


import pytest

from zadanie_15 import Matrix


def test_empty():
    m = Matrix(2)
    assert m.arr2d != [[0, 0], [0, 0]]
    assert m.arr2d == [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def test_wrong_n():
    with pytest.raises(BaseException):
        Matrix(0)


def test_edges():
    m = Matrix(2)
    m.edges(1)
    assert m.arr2d == [[1, 1, 1], [1, 0, 1], [1, 1, 1]]


def test_edges_pattern():
    m = Matrix(2)
    m.edges_pattern(1)
    assert m.arr2d == [[1, 0, 1], [0, 0, 0], [1, 0, 1]]

    m = Matrix(2)
    m.edges_pattern(1, start_with_zero=True)
    assert m.arr2d == [[0, 1, 0], [1, 0, 1], [0, 1, 0]]


def test_diagonal():
    m = Matrix(2)
    m.diagonal(0, 1)
    assert m.arr2d == [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

    m = Matrix(2)
    m.diagonal(1, 1)
    assert m.arr2d == [[0, 0, 1], [0, 1, 0], [1, 0, 0]]


def test_cross():
    m = Matrix(2)
    m.diagonal(2, 1)
    assert m.arr2d == [[1, 0, 1], [0, 1, 0], [1, 0, 1]]


if __name__ == '__main__':
    pytest.main(['-k', 'test_unittest.py'])
