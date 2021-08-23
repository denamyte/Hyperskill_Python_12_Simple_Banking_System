class Account:

    def __init__(self, id: int, number: str, pin: str, balance: int = 0):
        self._id = id
        self._number = number
        self._pin = pin
        self._balance = balance

    @property
    def id(self):
        return self._id

    @property
    def number(self):
        return self._number

    @property
    def pin(self):
        return self._pin

    @property
    def balance(self):
        return self._balance

    def change_balance(self, amount: int):
        if self._balance + amount > 0:
            self._balance += amount

    def __str__(self):
        return f'Account: id {self.id}, number {self.number}, pin {self.pin}, balance {self.balance}'
