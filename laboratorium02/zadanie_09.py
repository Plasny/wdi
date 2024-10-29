#!/usr/bin/env python3

from typing import List


def fill(lt: List[int]) -> List[int]:
    nlt = [lt[0]]
    for n in range(len(lt) - 1):
        if lt[n] > lt[n + 1]:
            nlt.extend([x for x in range(lt[n] - 1, lt[n + 1] - 1, -1)])
        elif lt[n] < lt[n + 1]:
            nlt.extend([x for x in range(lt[n] + 1, lt[n + 1] + 1, 1)])
        else:
            nlt.append(lt[n])

    return nlt


def main():
    lt = [5, 1, 4]
    print(lt)
    print(fill(lt), end='\n\n')
    assert fill(lt) == [5, 4, 3, 2, 1, 2, 3, 4]

    lt = [11, -1, -1, 4]
    print(lt)
    print(fill(lt), end='\n\n')
    assert fill(lt) == [11, 10, 9, 8, 7, 6,
                        5, 4, 3, 2, 1, 0, -1, -1, 0, 1, 2, 3, 4,]

    lt = [10, 0, 3, 2, 5]
    print(lt)
    print(fill(lt), end='\n\n')
    assert fill(lt) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2,
                        3, 2, 3, 4, 5]

    lt = [0, 7, 13, 8, 12]
    print(lt)
    print(fill(lt), end='\n\n')
    assert fill(lt) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                        11, 12, 13, 12, 11, 10, 9, 8, 9, 10, 11, 12]

    lt = [1, 1, 1, 2, 3]
    print(lt)
    print(fill(lt), end='\n\n')
    assert fill(lt) == lt


if __name__ == "__main__":
    main()