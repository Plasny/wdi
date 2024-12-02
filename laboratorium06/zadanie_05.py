#!/usr/bin/env python3

import random

MIN = 1
MAX = 10
MAX_DEPTH = 10
MAX_EL_NUM = 3


def generate():
    def gen_list_or_int(list, depth=0):
        for _ in range(random.randint(1, MAX_EL_NUM)):
            chance = random.randint(1, 2)

            if depth == MAX_DEPTH or chance < 2:
                list.append(random.randint(MIN, MAX))
            elif chance == 2:
                list.append(gen_list_or_int([], depth + 1))

        return list

    return gen_list_or_int([])


def sum(list, out=0):
    for e in list:
        if isinstance(e, type([])):
            out = sum(e, out)
        else:
            out += e

    return out


assert 10 == sum([1, 2, 3, 4])
assert 10 == sum([1, [2], [[3, 4]]])
assert 53 == sum([[[[2, 3]], [[[[10], [2, 4], [5]]], [9, 7], [9]], [2]]])
assert 16 == sum([[6], 7, 3])

list = generate()
print(list)
print(sum(list))
