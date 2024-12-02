#!/usr/bin/env python3

from zadanie_12 import check_s, check_w, check_h, check_g

import unittest
import sys
import os


class TestZadanie12(unittest.TestCase):
    def setUp(self):
        self._original_stdout = sys.stdout

        # disable printing
        sys.stdout = open(os.devnull, 'w')

    def tearDown(self):
        sys.stdout.close()
        sys.stdout = self._original_stdout

    def test_empty(self):
        assert check_s([(10, 10)]) == []
        assert check_g([], []) == []
        assert check_w([], []) == []
        assert check_h([(1, 1)]) == []

    def test_2_each_type(self):
        assert check_s([(5, 20), (4, 22)]) == [((5, 20), (4, 22))]
        assert check_g([(6, 18), (7, 19)], []) == [((6, 18), (7, 19))]
        assert check_w([(30, 20), (28, 20)], []) == [((30, 20), (28, 20))]
        assert check_h([(3, 3), (4, 4)]) == [((3, 3), (4, 4))]

    def test_3_each_type(self):
        assert check_s([(5, 20), (4, 22), (3, 24)]) == [
            ((5, 20), (4, 22)), ((4, 22), (3, 24))]
        assert check_g([(6, 18), (7, 19)], [(8, 20)]) == [
            ((6, 18), (8, 20)), ((6, 18), (7, 19)), ((7, 19), (8, 20))]
        assert check_w([(30, 20), (28, 20), (26, 20)], []) == [
            ((30, 20), (28, 20)), ((30, 20), (26, 20)), ((28, 20), (26, 20))]
        assert check_h([(3, 3), (4, 4), (3, 4)]) == [
            ((3, 3), (4, 4)), ((3, 3), (3, 4)), ((4, 4), (3, 4))]


if __name__ == '__main__':
    unittest.main()
