from typing import List, Union
from re import split as re_split
from packages.aoc_helper import Input

#  --- BINGO BOARD ---
# [ 0,  1,  2,  3,  4,
#   5,  6,  7,  8,  9,
#  10, 11, 12, 13, 14,
#  15, 16, 17, 18, 19,
#  20, 21, 22, 23, 24 ]


def update_boards(_game_boards: List[List[int]], _current_number: int) -> List[List[int]]:
    _current_number = int(0) if _current_number == None else _current_number
    for _board in _game_boards:
        try:
            _board[_board.index(_current_number)] = 1000
        except ValueError:
            continue
    return _game_boards


def bingo_check(_game_boards: List[List[int]]) -> Union[List[int], None]:
    for _game_board in _game_boards:
        for idx in range(5):
            if sum([_game_board[idx], _game_board[idx + 5], _game_board[idx + 10], _game_board[idx + 15], _game_board[idx + 20]]) == 5000:
                return _game_board
        for idx in range(0, 21, 5):
            if sum([_game_board[idx], _game_board[idx + 1], _game_board[idx + 2], _game_board[idx + 3], _game_board[idx + 4]]) == 5000:
                return _game_board

def generate_bingo_boards(_input: List[str]) -> List[List[int]]:
    all_boards = []
    while len(_input) > 0:
        try:
            all_boards.append([int(num) if num else 0 for _ in range(5) for num in re_split("\s+", _input.pop(0))])
        except Exception as exc:
            print(exc)

    return all_boards

def part1(_sequence: List[int], _game_boards: List[List[int]]) -> int:
    while len(_sequence) > 0:
        _current_number = _sequence.pop(0)
        _winner = bingo_check(update_boards(_game_boards, _current_number))
        if _winner:
            return sum([num if num < 1000 else 0 for num in _winner]) * _current_number



def part2() -> None:
    pass


if __name__ == "__main__":
    _input = list(filter(None, Input.readto_list("./data/d4")))
    _numbers_drawn = [int(num) for num in _input.pop(0).split(",")]
    print(f"Part 1: {part1(_numbers_drawn, generate_bingo_boards(_input))}")
    print(f"Part 2: {part2()}")
