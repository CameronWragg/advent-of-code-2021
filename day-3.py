from packages.aoc_helper import Input
from typing import List
from collections import Counter
from copy import deepcopy


def get_common(col: List[int], most: bool) -> int:
    _counter = Counter(col)
    if _counter[0] > _counter[1]:
        return 0 if most else 1
    else:
        return 1 if most else 0


def get_false_indexes(col: List[int], most: bool) -> List[int]:
    _common = get_common(col, most)
    false_indexes = []
    for index in range(len(col)):
        if col[index] != _common:
            false_indexes.append(index)
        else:
            continue
    return sorted(false_indexes, reverse=True)


def part_2_logic(_columns: List[List[int]], most: bool) -> int:
    _col = 0
    while len(_columns[0]) != 1:
        _false_indexes = get_false_indexes(_columns[_col], most)
        for column in _columns:
            for index in _false_indexes:
                del column[index]
        _col += 1
    return int("".join([str(col[0]) for col in _columns]), base=2)


def part1(_columns: List[List[int]]) -> int:
    _gamma, _epsilon = "", ""
    for counter in [Counter(_col) for _col in _columns]:
        if counter[0] > counter[1]:
            _gamma += "0"
            _epsilon += "1"
        else:
            _gamma += "1"
            _epsilon += "0"
    return int(_gamma, base=2) * int(_epsilon, base=2)


def part2(_columns: List[List[int]]) -> int:
    _oxy_gen = part_2_logic(deepcopy(_columns), True)
    _co2_scr = part_2_logic(_columns, False)
    return _oxy_gen * _co2_scr


if __name__ == "__main__":
    _input = Input.readto_columns("./data/d3")
    print(f"Part 1: {part1(_input)}")
    print(f"Part 2: {part2(_input)}")
