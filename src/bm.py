from typing import Dict


def make_km_table(pattern: str) -> Dict[str, int]:
    table = dict()
    pattern_length = len(pattern)

    for i in range(pattern_length - 1):
        table[pattern[i]] = pattern_length - i - 1

    if pattern[-1] not in table:
        table[pattern[-1]] = pattern_length

    return table


class Bm:
    def __init__(self, text: str, pattern: str) -> None:
        self.__text = text
        self.__pattern = pattern
        self.__pattern_length = len(pattern)
        self.__table = make_km_table(pattern)

    def search(self) -> int:
        text_index = self.__pattern_length - 1
        while text_index < len(self.__text):
            if self.__is_match(text_index):
                return text_index - self.__pattern_length + 1
            text_index += self.__decide_slide_width(self.__text[text_index])
        return -1

    def __is_match(self, text_index: int) -> bool:
        for offset in range(self.__pattern_length):
            if self.__text[text_index - offset] != self.__pattern[self.__pattern_length - offset - 1]:
                return False
        return True

    def __decide_slide_width(self, c: str) -> int:
        if len(c) != 1:
            raise ValueError("Parameter c should be single character.")
        if c in self.__table:
            return self.__table[c]
        return len(self.__pattern)
