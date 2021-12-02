from packages.aoc_helper import Input
from typing import List, Union


def part1(_commands: List[List[Union[str, int]]]) -> int:
    _h_d = [0, 0]

    for command in _commands:
        match command[0]:
            case "forward":
                _h_d[0] += command[1]
            case "down":
                _h_d[1] += command[1]
            case "up":
                _h_d[1] -= command[1]

    return _h_d[0] * _h_d[1]


def part2(_commands: List[List[Union[str, int]]]) -> int:
    _h_d_a = [0, 0, 0]

    for command in _commands:
        match command[0]:
            case "forward":
                _h_d_a[0] += int(command[1])
                _h_d_a[1] += (_h_d_a[2] * int(command[1]))
            case "down":
                _h_d_a[2] += int(command[1])
            case "up":
                _h_d_a[2] -= int(command[1])

    return _h_d_a[0] * _h_d_a[1]


if __name__ == "__main__":
    _input = [l.split(" ") for l in Input.readto_list("./data/d2")]
    print(f"Part 1: {part1(_input)}")
    print(f"Part 2: {part2(_input)}")
