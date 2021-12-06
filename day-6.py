from collections import Counter
from typing import List
from packages.aoc_helper import Input


def part1and2(_school: List[int], _days_to_simulate: int) -> None:
    _group_fish_by_state = Counter(_school)
    _fish_state_index = [_group_fish_by_state[i] for i in range(9)]

    for _ in range(_days_to_simulate):
        _fish_state_index = [
            _fish_state_index[1],
            _fish_state_index[2],
            _fish_state_index[3],
            _fish_state_index[4],
            _fish_state_index[5],
            _fish_state_index[6],
            _fish_state_index[0] + _fish_state_index[7],
            _fish_state_index[8],
            _fish_state_index[0],
        ]

    return sum(_fish_state_index)


if __name__ == "__main__":
    _input = Input.readto_list("./data/d6", to_int=True, separator=",")
    print(f"Part 1: {part1and2(_input, 80)}")
    print(f"Part 2: {part1and2(_input, 256)}")
