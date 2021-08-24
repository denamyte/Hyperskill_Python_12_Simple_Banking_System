from typing import Tuple, Dict, Set
from utils import Utils
from account import Account
from db_layer import DBLayer


class DataState:
    def __init__(self, db_layer: DBLayer):
        self._db_layer = db_layer

    def create_account(self) -> Account:
        """Creates a new account, returns an Account instance"""

        account = Account(0, self._create_card_number(),
                          Utils.get_random_digit_word(4))
        self._db_layer.create_account(account)
        return account

    def account_exists(self, number: str) -> bool:
        return bool(self._db_layer.get_account_by_number(number))

    def _create_card_number(self):
        card_number = ''
        while not card_number or self.account_exists(card_number):
            account_number = Utils.get_random_digit_word(9)
            _15_digits = '400000' + account_number
            card_number = _15_digits + str(Utils.calculate_luhn_checksum(_15_digits))

        return card_number

    def card_and_pin_are_correct(self, number: str, pin: str) -> bool:
        acc = self._db_layer.get_account_by_number(number)
        return acc and acc.pin == pin

    def card_balance(self, number: str) -> int:
        acc = self._db_layer.get_account_by_number(number)
        return 0 if not acc else acc.balance
