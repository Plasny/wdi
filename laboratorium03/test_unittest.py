#!/usr/bin/env python3

import unittest

from zadanie_15 import Matrix


class TestZadanie15(unittest.TestCase):
    def test_empty(self):
        m = Matrix(2)
        self.assertNotEqual(m.arr2d, [[0, 0], [0, 0]])
        self.assertEqual(m.arr2d, [[0, 0, 0], [0, 0, 0], [0, 0, 0]])

    def test_wrong_n(self):
        with self.assertRaises(BaseException):
            Matrix(0)

    def test_edges(self):
        m = Matrix(2)
        m.edges(1)
        self.assertEqual(m.arr2d, [[1, 1, 1], [1, 0, 1], [1, 1, 1]])

    def test_edges_pattern(self):
        m = Matrix(2)
        m.edges_pattern(1)
        self.assertEqual(m.arr2d, [[1, 0, 1], [0, 0, 0], [1, 0, 1]])

        m = Matrix(2)
        m.edges_pattern(1, start_with_zero=True)
        self.assertEqual(m.arr2d, [[0, 1, 0], [1, 0, 1], [0, 1, 0]])

    def test_diagonal(self):
        m = Matrix(2)
        m.diagonal(0, 1)
        self.assertEqual(m.arr2d, [[1, 0, 0], [0, 1, 0], [0, 0, 1]])

        m = Matrix(2)
        m.diagonal(1, 1)
        self.assertEqual(m.arr2d, [[0, 0, 1], [0, 1, 0], [1, 0, 0]])

    def test_cross(self):
        m = Matrix(2)
        m.diagonal(2, 1)
        self.assertEqual(m.arr2d, [[1, 0, 1], [0, 1, 0], [1, 0, 1]])


if __name__ == '__main__':
    unittest.main()
