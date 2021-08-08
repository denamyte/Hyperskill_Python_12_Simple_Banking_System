from typing import Dict, Callable
from data_state import DataState
from state_machine import Stage


class BankCLI:

    def __init__(self, data_state: DataState):
        self._data_state = data_state
        self._actions: Dict[Stage, Callable[[], int]] = {
            Stage.MAIN_MENU: self._main_menu,
            Stage.CREATE_ACCOUNT: self._create_account,
            Stage.LOG_INTO_ACCOUNT: self._log_into_account,
            Stage.WRONG_ACCOUNT_DETAILS: self._log_in_fail,
            Stage.LOGGED_IN: self._log_in_success,
            Stage.ACCOUNT_MENU: lambda: 0,
            Stage.ACCOUNT_BALANCE: lambda: 0,
            Stage.ACCOUNT_LOG_OUT: lambda: 0,
            Stage.EXIT: lambda: 0,
        }

    def show_menu(self, state: Stage) -> int:
        return self._actions[state]()

    @staticmethod
    def _main_menu() -> int:
        return int(input('''
1. Create an account
2. Log into account
0. Exit
'''))

    def _create_account(self):
        card_number, pin = self._data_state.create_account()
        print(f'''
Your card has been created
Your card number:
{card_number}
Your card PIN:
{pin}''')

    def _log_into_account(self) -> int:
        card_number = input('\nEnter your card number:\n')
        pin = input('Enter your PIN:\n')
        return 1 if self._data_state.card_and_pin_are_correct(card_number, pin) else 0

    @staticmethod
    def _log_in_fail():
        print('\nWrong card number or PIN!')

    @staticmethod
    def _log_in_success():
        print('\nYou have successfully logged in!')
        input('no more menus, sorry')

    # todo: Add other methods

