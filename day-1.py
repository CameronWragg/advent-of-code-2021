from typing import Literal
from packages.aoc_helper import Input
from collections import deque
from functools import reduce
from operator import add


def _is_higher(input: int) -> Literal[1, 0]:
    return input[1] > input[0]


def part1(file: str) -> int:
    _input = Input.readto_list(file, to_int=True)
    _answer = reduce(add, map(_is_higher, zip(_input, _input[1:])))
    return _answer


def part2(file: str) -> int:
    _input = Input.readto_deque(file, to_int=True)
    _answer = 0
    _b = deque([_input.popleft() for _ in range(3)])
    _a = sum(_b)
    while True:
        try:
            _b.popleft()
            _b.append(_input.popleft())
            _answer += _is_higher([_a, sum(_b)])
            _a = sum(_b)
        except IndexError:
            return _answer


if __name__ == "__main__":
    print(f"Part 1: {part1('./data/d1')}")
    print(f"Part 2: {part2('./data/d1')}")
