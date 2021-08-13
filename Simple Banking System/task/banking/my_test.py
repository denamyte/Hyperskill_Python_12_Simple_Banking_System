from utils import Utils


def check_luhn_calculation():
    card_num1 = '400000' + '123123123'
    checksum1 = 4
    print('checksum1 is valid:', checksum1 == Utils.calculate_luhn_checksum(card_num1))

    card_num2 = '400000' + '654654654'
    checksum2 = 9
    print('checksum2 is valid:', checksum2 == Utils.calculate_luhn_checksum(card_num2))


check_luhn_calculation()
