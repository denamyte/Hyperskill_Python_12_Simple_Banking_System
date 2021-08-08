from state_machine import StateMachine
from data_state import DataState
from bank_cli import BankCLI


class Controller:
    def __init__(self):
        self._state_machine = StateMachine()
        self._bank_cli = BankCLI(DataState())

    def run(self):
        choice = 0
        while self._state_machine.going_on():
            self._state_machine.switch_state(choice)
            choice = self._bank_cli.show_menu(self._state_machine.state)
        else:
            print('\nBye!')
