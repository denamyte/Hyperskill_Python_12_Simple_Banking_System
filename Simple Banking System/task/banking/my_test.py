from utils import Utils
from db_layer import DBLayer
from data_state import DataState


def check_luhn_calculation():
    card_num1 = '400000' + '123123123'
    checksum1 = 4
    print('checksum1 is valid:', checksum1 == Utils.calculate_luhn_checksum(card_num1))

    card_num2 = '400000' + '654654654'
    checksum2 = 9
    print('checksum2 is valid:', checksum2 == Utils.calculate_luhn_checksum(card_num2))


def check_db_card():
    db_layer = DBLayer()
    data_state = DataState(db_layer)

    print('Account exists (expect False):', data_state.account_exists('1234123412341238'))
    account = data_state.create_account()
    print('Account created:', account)
    print(f'Account exists ({account.number}; expect True):', data_state.account_exists(account.number))


# check_luhn_calculation()
check_db_card()
