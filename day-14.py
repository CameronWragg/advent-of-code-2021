from collections import Counter
from operator import methodcaller as mc
from typing import Dict, Tuple

from packages.aoc_helper import Input


def readto_string_dict() -> Tuple[str, Dict[str, str]]:
    _input = Input.readto_list("./data/d14")
    _starter, _ = _input.pop(0), _input.pop(0)
    _insertion_rules = dict(map(mc("split", " -> "), _input))
    return _starter, _insertion_rules


def max_minus_min(mono_counter: Counter) -> int:
    _values = mono_counter.values()
    return max(_values) - min(_values)


def part1and2(poly_starter_rules: Tuple[str, Dict[str, str]], steps: int) -> int:
    monomer_counter = Counter(poly_starter_rules[0])
    polymer_counter = Counter(
        map(
            lambda monomer: monomer[0] + monomer[1],
            zip(poly_starter_rules[0], poly_starter_rules[0][1:]),
        )
    )
    for _ in range(steps):
        tmp_counter = Counter()
        for key, value in polymer_counter.items():
            tmp_counter[key[0] + poly_starter_rules[1][key]] += value
            tmp_counter[poly_starter_rules[1][key] + key[1]] += value
            monomer_counter[poly_starter_rules[1][key]] += value
        polymer_counter = tmp_counter
    return max_minus_min(monomer_counter)


if __name__ == "__main__":
    print(f"Part 1: {part1and2(readto_string_dict(), 10)}")
    print(f"Part 2: {part1and2(readto_string_dict(), 40)}")
