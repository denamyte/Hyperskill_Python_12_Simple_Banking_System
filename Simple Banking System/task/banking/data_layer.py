from typing import Tuple, Dict, Set
from utils import Utils
from account import Account
from db_layer import DBLayer


class DataLayer:
    def __init__(self, db_layer: DBLayer):
        self._db_layer = db_layer

    def create_account(self) -> Account:
        account = Account(0, self._create_card_number(),
                          Utils.get_random_digit_word(4))
        self._db_layer.create_account(account)
        return account

    def account_exists(self, card_number: str) -> bool:
        return bool(self._db_layer.get_account_by_number(card_number))

    def _create_card_number(self):
        card_number = ''
        while not card_number or self.account_exists(card_number):
            account_number = Utils.get_random_digit_word(9)
            _15_digits = '400000' + account_number
            card_number = _15_digits + str(Utils.calculate_luhn_checksum(_15_digits))

        return card_number

    @staticmethod
    def luhn_checksum_correct(card_number: str) -> bool:
        last_digit = card_number[-1]
        checksum = str(Utils.calculate_luhn_checksum(card_number[:-1]))
        return last_digit == checksum

    def card_exists(self, card_number: str) -> bool:
        return bool(self._db_layer.get_account_by_number(card_number))

    def card_and_pin_are_correct(self, card_number: str, pin: str) -> bool:
        acc = self._db_layer.get_account_by_number(card_number)
        return acc and acc.pin == pin

    def card_balance(self, card_number: str) -> int:
        acc = self._db_layer.get_account_by_number(card_number)
        return 0 if not acc else acc.balance

    def add_income(self, card_number: str, income: int):
        self._db_layer.add_income(card_number, income)

    def account_has_money(self, card_number: str, money: int) -> bool:
        account = self._db_layer.get_account_by_number(card_number)
        return bool(account and account.balance >= money)

    def transfer_money(self, card_from: str, card_to: str, money: int):
        self._db_layer.add_income(card_from, -money)
        self._db_layer.add_income(card_to,    money)

    def delete_account(self, card_number: str):
        self._db_layer.delete_account(card_number)

