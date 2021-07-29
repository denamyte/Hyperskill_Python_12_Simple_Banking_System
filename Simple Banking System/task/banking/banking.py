from enum import Enum


class State(Enum):
    MainMenu = 1


class BankingSystem:

    def __init__(self):
        self.state: State = State.MainMenu

    @staticmethod
    def get_main_menu_input() -> str:
        return input('''\
1. Create an account
2. Log into account
0. Exit
''')


