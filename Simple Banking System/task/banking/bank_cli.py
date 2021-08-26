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
            Stage.ACCOUNT_ADD_INCOME: self._account_add_income,
            Stage.ACCOUNT_TRANSFER_CARD_1_ENTER: self._account_transfer_enter_card,

            Stage.ACCOUNT_TRANSFER_CARD_2_SAME_ACCOUNT: self._account_transfer_check_same_account,
            Stage.ACCOUNT_TRANSFER_CARD_3_LUHN: self._account_transfer_check_luhn,
            Stage.ACCOUNT_TRANSFER_CARD_4_CARD_EXISTENCE: self._account_transfer_check_card_existence,

            Stage.ACCOUNT_TRANSFER_SUM_1_ENTER: self._account_transfer_enter_sum,

            Stage.ACCOUNT_CLOSE: self._account_close,
            Stage.ACCOUNT_LOG_OUT: self._fn_message(Stage.ACCOUNT_LOG_OUT),
            Stage.EXIT: self._fn_message(Stage.EXIT),
        }
        self._card_number = ''
        self._card_number_to_transfer_to = ''
        self._sum = 0

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
        self._card_number = input('\nEnter your card number:\n')
        pin = input('Enter your PIN:\n')
        return 1 if self._data_state.card_and_pin_are_correct(self._card_number, pin) else 0

    @staticmethod
    def _account_menu() -> int:
        return int(input('''
1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit
'''))

    def _account_balance(self):
        print(f'\nBalance: {self._data_state.card_balance(self._card_number)}')

    def _account_add_income(self) -> int:
        income = int(input('\nEnter income:\n'))
        self._data_state.add_income(self._card_number, income)
        print('Income was added!')
        return 0

    def _account_transfer_enter_card(self) -> int:
        self._card_number_to_transfer_to = input('''
Transfer
Enter card number:
''')
        return 0

    def _account_transfer_check_same_account(self) -> int:
        distinct = self._card_number != self._card_number_to_transfer_to
        if not distinct:
            print("You can't transfer money to the same account!")
        return distinct

    def _account_transfer_check_luhn(self) -> int:
        correct = self._data_state.luhn_checksum_correct(self._card_number_to_transfer_to)
        if not correct:
            print('Probably you made a mistake in the card number. Please try again!')
        return correct

    def _account_transfer_check_card_existence(self) -> int:
        exists = self._data_state.card_exists(self._card_number_to_transfer_to)
        if not exists:
            print('Such a card does not exist.')
        return exists

    def _account_transfer_enter_sum(self) -> int:
        self._sum = int(input('Enter how much money you want to transfer:\n'))
        return 0

    # todo: check there is enough money to transfer the sum given

    @staticmethod
    def _account_close() -> int:
        print('Close account(4) menu')
        return 0
