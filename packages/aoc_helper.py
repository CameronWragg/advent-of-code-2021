from typing import List, Union
from numpy import array_split, ndarray
from collections import deque
import re


class Input:
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
