from typing import Dict, Callable
from data_layer import DataLayer
from state_machine import Stage


class BankCLI:

    def __init__(self, data_state: DataLayer):
        self._data_layer = data_state
        self._actions: Dict[Stage, Callable[[], int]] = {
            Stage.MAIN_MENU: self._main_menu,
            Stage.CREATE_ACCOUNT: self._create_account,
            Stage.LOG_INTO_ACCOUNT: self._log_into_account,
            Stage.ACCOUNT_MENU: self._account_menu,
            Stage.ACCOUNT_BALANCE: self._account_balance,
            Stage.ACCOUNT_ADD_INCOME: self._account_add_income,

            Stage.ACCOUNT_TRANSFER_CARD_1_ENTER: self._account_transfer_enter_card,
            Stage.ACCOUNT_TRANSFER_CARD_2_SAME_ACCOUNT: self._account_transfer_check_same_account,
            Stage.ACCOUNT_TRANSFER_CARD_3_LUHN: self._account_transfer_check_luhn,
            Stage.ACCOUNT_TRANSFER_CARD_4_CARD_EXISTENCE: self._account_transfer_check_card_existence,
            Stage.ACCOUNT_TRANSFER_SUM_1_ENTER: self._account_transfer_enter_sum,
            Stage.ACCOUNT_TRANSFER_SUM_2_CHECK_SUM: self._account_transfer_check_sum,
            Stage.ACCOUNT_TRANSFER_SUM_3_TRANSFER: self._account_transfer_do_transfer,

            Stage.ACCOUNT_CLOSE: self._account_close,
            Stage.ACCOUNT_LOG_OUT: self._account_logout,
            Stage.EXIT: self._exit,
        }
        self._card_number = ''
        self._card_number_to_transfer_to = ''
        self._sum = 0

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
        acc = self._data_layer.create_account()
        print(f'''
Your card has been created
Your card number:
{acc.number}
Your card PIN:
{acc.pin}''')

    def _log_into_account(self) -> int:
        self._card_number = input('\nEnter your card number:\n')
        pin = input('Enter your PIN:\n')
        correct = self._data_layer.card_and_pin_are_correct(self._card_number, pin)
        print('\nYou have successfully logged in!' if correct else '\nWrong card number or PIN!')
        return correct

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
        print(f'\nBalance: {self._data_layer.card_balance(self._card_number)}')

    def _account_add_income(self) -> int:
        income = int(input('\nEnter income:\n'))
        self._data_layer.add_income(self._card_number, income)
        print('Income was added!')
        return 0

    def _account_transfer_enter_card(self) -> int:
        self._card_number_to_transfer_to = input('''
Transfer
Enter card number:
''')
        return 0

    def _account_transfer_check_same_account(self) -> int:
        return self._check_and_print_error(lambda: self._card_number != self._card_number_to_transfer_to,
                                           "You can't transfer money to the same account!")

    def _account_transfer_check_luhn(self) -> int:
        return self._check_and_print_error(
            lambda: self._data_layer.luhn_checksum_correct(self._card_number_to_transfer_to),
            'Probably you made a mistake in the card number. Please try again!')

    def _account_transfer_check_card_existence(self) -> int:
        return self._check_and_print_error(lambda: self._data_layer.card_exists(self._card_number_to_transfer_to),
                                           'Such a card does not exist.')

    def _account_transfer_enter_sum(self) -> int:
        self._sum = int(input('Enter how much money you want to transfer:\n'))
        return 0

    def _account_transfer_check_sum(self) -> int:
        return self._check_and_print_error(lambda: self._data_layer.account_has_money(self._card_number, self._sum),
                                           'Not enough money!')

    @staticmethod
    def _check_and_print_error(condition: Callable[[], bool], err: str) -> int:
        if not condition():
            print(err)
            return 0
        return 1

    def _account_transfer_do_transfer(self) -> int:
        self._data_layer.transfer_money(self._card_number, self._card_number_to_transfer_to, self._sum)
        print('Success!')
        return 0

    def _account_close(self) -> int:
        self._data_layer.delete_account(self._card_number)
        print('\nThe account has been closed!')
        return 0

    @staticmethod
    def _account_logout() -> int:
        print('\nYou have successfully logged out!')
        return 0

    @staticmethod
    def _exit() -> int:
        print('\nBye!')
        return 0
