from state_machine import StateMachine
from data_layer import DataLayer
from bank_cli import BankCLI
from db_layer import DBLayer


class Controller:
    def __init__(self):
        self._state_machine = StateMachine()
        db_layer = DBLayer()
        data_state = DataLayer(db_layer)
        self._bank_cli = BankCLI(data_state)

    def run(self):
        user_input = 0
        while self._state_machine.going_on():
            state = self._state_machine.switch_state(user_input)
            user_input = self._bank_cli.show_menu(state)
