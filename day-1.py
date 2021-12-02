from typing import List
from packages.aoc_helper import Input
from functools import reduce
from operator import add


def part1(_input: List[str]) -> int:
    _answer = reduce(add, map(lambda i: i[1] > i[0], zip(_input, _input[1:])))
    return _answer


def part2(_input: List[str]) -> int:
    _answer = part1(list(map(sum, zip(_input, _input[1:], _input[2:]))))
    return _answer


if __name__ == "__main__":
    _input = Input.readto_list("./data/d1", to_int=True)
    print(f"Part 1: {part1(_input)}")
    print(f"Part 2: {part2(_input)}")
