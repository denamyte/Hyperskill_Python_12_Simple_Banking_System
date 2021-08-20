from typing import Tuple, Dict, Set
from utils import Utils
from card import Card
from db_layer import DBLayer


# todo: remove this class (replace it with DBLayer)
class DataState:
    def __init__(self, db_layer: DBLayer):
        self._db_layer = db_layer
        self._card_dict: Dict[str, str] = {}
        self._card_dict2: Dict[str, Card] = {}
        self._unique_accounts: Set[str] = set()

    # todo: transfer this method to utils
    def create_account(self) -> Tuple[str, str]:
        """Creates a new account, returns the card number and its pin"""

        card_number = self._create_card_number()
        pin = Utils.get_random_digit_word(4)
        self._card_dict[card_number] = pin
        return card_number, pin

    # todo: transfer this method to utils
    def _create_card_number(self):
        account_number = ''
        while not account_number or account_number in self._unique_accounts:
            account_number = Utils.get_random_digit_word(9)

        _15_digits = '400000' + account_number
        return _15_digits + str(Utils.calculate_luhn_checksum(_15_digits))

    # todo: transfer this method to db_layer (select from db and check if result exists)
    def card_and_pin_are_correct(self, card_number: str, pin: str) -> bool:
        return card_number in self._card_dict and self._card_dict[card_number] == pin

    # todo: transfer this method to db_layer
    def card_balance(self, card_number: str) -> int:
        return 0
