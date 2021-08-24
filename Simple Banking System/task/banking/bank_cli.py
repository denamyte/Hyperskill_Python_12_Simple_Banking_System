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
            Stage.LOG_IN_FAILED: self._fn_message(Stage.LOG_IN_FAILED),
            Stage.LOGGED_IN: self._fn_message(Stage.LOGGED_IN),
            Stage.ACCOUNT_MENU: self._account_menu,
            Stage.ACCOUNT_BALANCE: self._account_balance,
            Stage.ACCOUNT_LOG_OUT: self._fn_message(Stage.ACCOUNT_LOG_OUT),
            Stage.EXIT: self._fn_message(Stage.EXIT),
        }
        self.card_number = ''

    def _fn_message(self, stage: Stage) -> Callable[[], None]:
        return lambda: print(self._SIMPLE_MESSAGES.get(stage))

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
        acc = self._data_state.create_account()
        print(f'''
Your card has been created
Your card number:
{acc.number}
Your card PIN:
{acc.pin}''')

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
