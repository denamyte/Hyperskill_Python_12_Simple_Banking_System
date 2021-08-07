import random
import string
from enum import Enum, auto
from typing import Dict, Callable, Set


class State(Enum):
    NONE = auto()
    MAIN_MENU = auto()
    CREATE_ACCOUNT = auto()
    ENTER_AND_CHECK_ACCOUNT_DETAILS = auto()
    WRONG_ACCOUNT_DETAILS = auto()
    LOGGED_IN = auto()
    ACCOUNT_MENU = auto()
    ACCOUNT_BALANCE = auto()
    ACCOUNT_LOG_OUT = auto()
    EXIT = auto()


class StateMachine:

    def __init__(self):
        self._state: State = State.MAIN_MENU

    def switch_state(self, choice: int = 0) -> State:
        if self._state == State.NONE:
            self._state = State.MAIN_MENU
        if self._state == State.MAIN_MENU:
            self._state = State.CREATE_ACCOUNT if choice == 1 \
                else State.ENTER_AND_CHECK_ACCOUNT_DETAILS if choice == 2 \
                else State.EXIT
        if self._state == State.ENTER_AND_CHECK_ACCOUNT_DETAILS:
            self._state = State.MAIN_MENU
        if self._state == State.ENTER_AND_CHECK_ACCOUNT_DETAILS:
            self._state = State.WRONG_ACCOUNT_DETAILS if choice == 0 else State.LOGGED_IN
        if self._state == State.WRONG_ACCOUNT_DETAILS:
            self._state = State.MAIN_MENU
        if self._state == State.LOGGED_IN:
            self._state = State.ACCOUNT_MENU
        if self._state == State.ACCOUNT_MENU:
            self._state = State.ACCOUNT_BALANCE if choice == 1 \
                else State.ACCOUNT_LOG_OUT if choice == 2 \
                else State.EXIT
        if self._state == State.ACCOUNT_BALANCE:
            self._state = State.ACCOUNT_MENU
        if self._state == State.ACCOUNT_LOG_OUT:
            self._state = State.MAIN_MENU
        return self._state

    @property
    def state(self):
        return self._state

    def going_on(self) -> bool:
        return self._state is not State.EXIT


class Utils:
    @staticmethod
    def get_random_digit_word(word_len: int) -> str:
        """Creates and returns a word of length word_len consisting of random digits"""
        return ''.join(random.choices(string.digits, k=word_len))


class BankingSystem:

    def __init__(self):
        self._unique_cards: Set[str] = set()
        self._card_dict: Dict[str, str] = {}
        self._state_machine = StateMachine()
        self._actions: Dict[State, Callable[[], int]] = {
            State.MAIN_MENU: self._main_menu,
            State.CREATE_ACCOUNT: self._create_account,
            State.ENTER_AND_CHECK_ACCOUNT_DETAILS: lambda: 0,
            State.WRONG_ACCOUNT_DETAILS: lambda: 0,
            State.LOGGED_IN: lambda: 0,
            State.ACCOUNT_MENU: lambda: 0,
            State.ACCOUNT_BALANCE: lambda: 0,
            State.ACCOUNT_LOG_OUT: lambda: 0,
            State.EXIT: lambda: 0,
        }

    def main_menu_cycle(self):
        choice = 0
        while self._state_machine.going_on():
            self._state_machine.switch_state(choice)
            choice = self._actions[self._state_machine.state]()
        else:
            print('\nBye!')

    @staticmethod
    def _main_menu() -> int:
        return int(input('''\
1. Create an account
2. Log into account
0. Exit
'''))

    def _create_account(self):
        card_number = ''
        while not card_number or card_number in self._card_dict:
            card_number = self.create_card_number()
        pin = Utils.get_random_digit_word(4)
        self._card_dict[card_number] = pin

        print(f'''
Your card has been created
Your card number:
{card_number}
Your card PIN:
{pin}
''')

    # todo: Add other methods

    @staticmethod
    def create_card_number():
        account_number = Utils.get_random_digit_word(9)
        return '400000' + account_number + Utils.get_random_digit_word(1)

    def _log_into_account(self):
        print('\nLogging into an account')


BankingSystem().main_menu_cycle()
