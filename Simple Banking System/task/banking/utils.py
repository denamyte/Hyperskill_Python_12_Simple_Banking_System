import string
import random


class Utils:
    @staticmethod
    def get_random_digit_word(word_len: int) -> str:
        """Creates and returns a word of length word_len consisting of random digits"""
        return ''.join(random.choices(string.digits, k=word_len))
