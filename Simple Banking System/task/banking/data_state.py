from typing import Tuple, Dict, Set

from utils import Utils


class DataState:
    def __init__(self):
        self._card_dict: Dict[str, str] = {}
        self._unique_accounts: Set[str] = set()

    def create_account(self) -> Tuple[str, str]:
        """Creates a new account, returns the card number and its pin"""

        card_number = self._create_card_number()
        pin = Utils.get_random_digit_word(4)
        self._card_dict[card_number] = pin
        return card_number, pin

    def _create_card_number(self):
        account_number = ''
        while not account_number or account_number in self._unique_accounts:
            account_number = Utils.get_random_digit_word(9)

        _15_digits = '400000' + account_number
        return _15_digits + str(Utils.calculate_luhn_checksum(_15_digits))

    def card_and_pin_are_correct(self, card_number: str, pin: str) -> bool:
        return card_number in self._card_dict and self._card_dict[card_number] == pin

    def card_balance(self, card_number: str) -> int:
        return 0
