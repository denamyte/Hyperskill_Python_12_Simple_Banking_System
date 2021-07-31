import random
import string
from enum import Enum
from typing import Dict, Callable


class State(Enum):
    MainMenu = 1


class Utils:
    @staticmethod
    def get_random_digit_word(word_len: int) -> str:
        """Creates and returns a word of length word_len consisting of random digits"""
        return ''.join(random.choices(string.digits, k=word_len))


class BankingSystem:

    def __init__(self):
        self._state: State = State.MainMenu
        self._main_menu_actions: Dict[str, Callable[[], None]] = {
            '1': self._create_account,
            '2': self._log_into_account
        }

    def main_menu_cycle(self):
        inp = self._get_main_menu_input()
        while inp != '0':

            # todo:
            #  - convert the loop into "wile 1" one
            #  - get the code from main menu actions
            #  - check if the code == '0' (either from input or from an action execution), and break if so

            self._main_menu_actions.get(inp)()
            inp = self._get_main_menu_input()
        else:
            print('\nBye!')

    @staticmethod
    def _get_main_menu_input() -> str:
        return input('''\
1. Create an account
2. Log into account
0. Exit
''')

    def _create_account(self):
        account_number = Utils.get_random_digit_word(9)
        card_number = '400000' + account_number + Utils.get_random_digit_word(1)
        pin = Utils.get_random_digit_word(4)

        # todo go on here:
        #  uniqueness of an account number
        #  save the card number and the pin
        print('\nCreating an account')

    def _log_into_account(self):
        print('\nLogging into an account')


BankingSystem().main_menu_cycle()
