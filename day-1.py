from typing import Literal, Tuple
from packages.aoc_helper import Input
from functools import reduce
from operator import add


def _is_higher(input: Tuple[int]) -> Literal[1, 0]:
    return input[1] > input[0]


def _sum_three(input: Tuple[int]) -> int:
    return sum(input)


def part1(file: str, input_list: list = None) -> int:
    _input = Input.readto_list(file, to_int=True) if not input_list else input_list
    _answer = reduce(add, map(_is_higher, zip(_input, _input[1:])))
    return _answer


def part2(file: str) -> int:
    _input = Input.readto_list(file, to_int=True)
    _answer = part1(None, list(map(_sum_three, zip(_input, _input[1:], _input[2:]))))
    return _answer


if __name__ == "__main__":
    print(f"Part 1: {part1('./data/d1')}")
    print(f"Part 2: {part2('./data/d1')}")
