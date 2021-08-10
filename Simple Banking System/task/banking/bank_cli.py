from typing import Dict, Callable
from data_state import DataState
from state_machine import Stage


class BankCLI:
    _SIMPLE_MESSAGES: Dict[Stage, str] = {
        Stage.LOG_IN_FAILED: '\nWrong card number or PIN!',
        Stage.LOGGED_IN: '\nYou have successfully logged in!',
        Stage.ACCOUNT_LOG_OUT: '\nYou have successfully logged out!',
        Stage.EXIT: '\nBye!'
    }

    def __init__(self, data_state: DataState):
        self._data_state = data_state
        self._actions: Dict[Stage, Callable[[], int]] = {
            Stage.MAIN_MENU: self._main_menu,
            Stage.CREATE_ACCOUNT: self._create_account,
            Stage.LOG_INTO_ACCOUNT: self._log_into_account,
            Stage.LOG_IN_FAILED: lambda: print(self._SIMPLE_MESSAGES.get(Stage.LOG_IN_FAILED)),
            Stage.LOGGED_IN: lambda: print(self._SIMPLE_MESSAGES.get(Stage.LOGGED_IN)),
            Stage.ACCOUNT_MENU: self._account_menu,
            Stage.ACCOUNT_BALANCE: self._account_balance,
            Stage.ACCOUNT_LOG_OUT: lambda: print(self._SIMPLE_MESSAGES.get(Stage.ACCOUNT_LOG_OUT)),
            Stage.EXIT: lambda: print(self._SIMPLE_MESSAGES.get(Stage.EXIT)),
        }
        self.card_number = ''

    def show_menu(self, stage: Stage) -> int:
        return self._actions[stage]()

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
        self.card_number = input('\nEnter your card number:\n')
        pin = input('Enter your PIN:\n')
        return 1 if self._data_state.card_and_pin_are_correct(self.card_number, pin) else 0

    @staticmethod
    def _account_menu() -> int:
        return int(input('''
1. Balance
2. Log out
0. Exit
'''))

    def _account_balance(self):
        print(f'\nBalance: {self._data_state.card_balance(self.card_number)}')
