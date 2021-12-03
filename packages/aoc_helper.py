from dotenv import load_dotenv
from typing import List, Union
from numpy import array_split, ndarray
from collections import deque
from urllib.request import Request, urlopen
from os import getenv
import re

load_dotenv()


class Input:
    @staticmethod
    def readfrom_url(day: int, session_id: str = getenv("SESSION_ID")) -> None:
        _req = Request(f"https://adventofcode.com/2021/day/{str(day)}/input")
        _req.add_header("Cookie", f"session={session_id}")
        _res = urlopen(_req, timeout=900)
        with open(f"./data/d{day}", "w") as _file:
            print(_res.read().decode("utf-8"), end="", file=_file)

    @staticmethod
    def readto_string(file: str) -> str:
        return open(file).read().rstrip("\n")

    @staticmethod
    def readto_list(file: str, to_int: bool = False) -> Union[List[str], List[int]]:
        _list = Input.readto_string(file).split("\n")
        if not to_int:
            return _list
        else:
            return list(map(lambda l: int(l.rstrip("\n")), _list))

    @staticmethod
    def readto_columns(file: str) -> List[List[int]]:
        _list = Input.readto_list(file)
        _columns = [[] for _ in range(len(_list[0]))]
        for l in _list:
            _col = 0
            for n in l:
                _columns[_col].append(int(n))
                _col += 1
        return _columns

    @staticmethod
    def readto_deque(file: str, to_int: bool = False) -> Union[deque[str], deque[int]]:
        _list = Input.readto_string(file).split("\n")
        if not to_int:
            return deque(_list)
        else:
            return deque(map(lambda l: int(l.rstrip("\n")), _list))

    @staticmethod
    def readto_matrix(file: str, cols: int) -> List[ndarray]:
        _list = Input.readto_list(file, to_int=True)
        return array_split(_list, cols)

    @staticmethod
    def readto_list_re(file: str, re_pattern: str, max_split: int = None) -> List[str]:
        _string = Input.readto_string(file)
        if not max_split:
            return re.split(re_pattern, _string)
        else:
            return re.split(re_pattern, _string, max_split)
