import string
import random
from itertools import cycle


class Utils:
    @staticmethod
    def get_random_digit_word(word_len: int) -> str:
        """Creates and returns a word of length word_len consisting of random digits"""
        return ''.join(random.choices(string.digits, k=word_len))

    @staticmethod
    def calculate_luhn_checksum(num_str: str) -> int:
        """
        Calculates the Luhn checksum (a single digit) for a string of digits.
        At the end of the string passed there should be no symbol of the string checksum.
        """
        s = sum(i if i < 10 else i - 9 for i in (x * y for x, y in zip(map(int, num_str[::-1]), cycle([2, 1]))))
        remainder = s % 10
        return 0 if not remainder else 10 - remainder
