from os import lseek
from packages.aoc_helper import Input
from typing import List
from collections import Counter


def rows_to_cols(_input: List[str]) -> List[List[int]]:
    _columns = [[] for _ in range(len(_input[0]))]
    for l in _input:
        _col = 0
        for n in l:
            _columns[_col].append(int(n))
            _col += 1
    return _columns


def most_common(_input: Counter) -> int:
    if _input[0] > _input[1]:
        return 0
    else:
        return 1


def least_common(_input: Counter) -> int:
    if _input[0] > _input[1]:
        return 1
    else:
        return 0

    
def get_false_indexes(col: List[int], common: int) -> List[int]:
    false_indexes = []
    for index in range(len(col)):
        if col[index] != common:
            false_indexes.append(index)
        else:
            continue
    return false_indexes


def del_false_index(col: List[int], false_index: int) -> List[int]:
    del col[false_index]
    return col


def part1(_input: List[int]) -> None:
    _columns = rows_to_cols(_input)
    _frequency = [Counter(_col) for _col in _columns]
    _gamma_epsilon = ["",""]
    for counter in _frequency:
        if counter[0] > counter[1]:
            _gamma_epsilon[0] += "0"
            _gamma_epsilon[1] += "1"
        else:
            _gamma_epsilon[0] += "1"
            _gamma_epsilon[1] += "0"
    return int(_gamma_epsilon[0], base=2) * int(_gamma_epsilon[1], base=2)


def part2(_input: List[int]) -> None:
    _columns = rows_to_cols(_input)
    _in_range = True
    _col = 0
    try:
        while _in_range:
            _false_indexes = get_false_indexes(_columns[_col], most_common(Counter(_columns[_col])))
            for column in _columns:
                for index in sorted(_false_indexes, reverse=True):
                    del column[index]
            _col += 1
    except IndexError:
        _in_range = False
    _oxy_gen = ""
    for col in _columns:
        _oxy_gen += str(col[0])
    
    _columns = rows_to_cols(_input)
    _in_range = True
    _col = 0
    try:
        while _in_range:
            if len(_columns[0]) == 1:
                break
            else:
                _false_indexes = get_false_indexes(_columns[_col], least_common(Counter(_columns[_col])))
                for column in _columns:
                    for index in sorted(_false_indexes, reverse=True):
                        del column[index]
                _col += 1
    except IndexError:
        _in_range = False
    print(_columns)
    _co2_scr = ""
    for col in _columns:
        _co2_scr += str(col[0])
    
    return int(_oxy_gen, base=2) * int(_co2_scr, base=2)


if __name__ == "__main__":
    _input = Input.readto_list("./data/d3")
    print(f"Part 1: {part1(_input)}")
    print(f"Part 2: {part2(_input)}")
