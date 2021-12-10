from typing import List, Tuple

from packages.aoc_helper import Input

brace_dict = {"(": ")", "[": "]", "{": "}", "<": ">"}
score_dict = {")": 3, "]": 57, "}": 1197, ">": 25137}
score_dict_p2 = {")": 1, "]": 2, "}": 3, ">": 4}


def check_syntax(line: str) -> str:
    open_braces = []
    for brace in line:
        if brace in brace_dict.keys():
            open_braces.append(brace)
        elif brace in brace_dict.values():
            if brace_dict[open_braces.pop(-1)] != brace:
                return brace
            else:
                continue
    return None


def fix_syntax(line: str) -> str:
    line_score = 0
    remaining_braces = []
    for brace in line:
        if brace in brace_dict.keys():
            remaining_braces.append(brace)
        elif brace in brace_dict.values():
            del remaining_braces[-1]
    for open_brace in reversed(remaining_braces):
        line_score += ((line_score * 5) + score_dict_p2[brace_dict[open_brace]])
    return line_score


def part1(lines: List[str]) -> Tuple[int, List[str]]:
    score = 0
    for line in lines:
        invalid = check_syntax(line)
        if invalid:
            score += score_dict[invalid]
            del lines[lines.index(line)]
    return score, lines


def part2(lines: List[str]) -> int:
    line_scores = []
    for line in lines:
        line_scores.append(fix_syntax(line))
    line_scores.sort()
    return line_scores[int(len(line_scores) / 2)]


if __name__ == "__main__":
    _input = Input.readto_list("./data/d10-test")
    p1_score, _input = part1(_input)
    print(f"Part 1: {p1_score}")
    print(f"Part 2: {part2(_input)}")
