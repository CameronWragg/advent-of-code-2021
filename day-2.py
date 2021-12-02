from packages.aoc_helper import Input
from typing import List
from operator import methodcaller as mc


def part1(commands: List[List[str]], part2: bool = False) -> int:
    h, d, a = 0, 0, 0
    for command in commands:
        _dist = int(command[1])
        match command[0]:
            case "forward":
                h += _dist
                d += (a * _dist) if part2 is True else 0
            case "down":
                d += _dist if part2 is False else 0
                a += _dist if part2 is True else 0
            case "up":
                d -= _dist if part2 is False else 0
                a -= _dist if part2 is True else 0
    return h * d


if __name__ == "__main__":
    _input = list(map(mc("split", " "), Input.readto_list("./data/d2")))
    print(f"Part 1: {part1(_input)}")
    print(f"Part 2: {part1(_input, part2=True)}")
