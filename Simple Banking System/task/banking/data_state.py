from typing import Tuple, Dict

from utils import Utils


class DataState:
    def __init__(self):
        self._card_dict: Dict[str, str] = {}

    def create_account(self) -> Tuple[str, str]:
        """Creates a new account, returns the card number and its pin"""

        card_number = ''
        while not card_number or card_number in self._card_dict:
            card_number = self._create_card_number()

        pin = Utils.get_random_digit_word(4)
        self._card_dict[card_number] = pin
        return card_number, pin

    @staticmethod
    def _create_card_number():
        account_number = Utils.get_random_digit_word(9)
        return '400000' + account_number + Utils.get_random_digit_word(1)

    def card_and_pin_are_correct(self, card_number: str, pin: str) -> bool:
        return card_number in self._card_dict and self._card_dict[card_number] == pin
