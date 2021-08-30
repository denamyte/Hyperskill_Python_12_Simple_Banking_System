from enum import Enum, auto


class Stage(Enum):
    NONE = auto()
    MAIN_MENU = auto()
    CREATE_ACCOUNT = auto()
    LOG_INTO_ACCOUNT = auto()

    ACCOUNT_MENU = auto()
    ACCOUNT_BALANCE = auto()
    ACCOUNT_ADD_INCOME = auto()

    ACCOUNT_TRANSFER_CARD_1_ENTER = auto()
    ACCOUNT_TRANSFER_CARD_2_SAME_ACCOUNT = auto()
    ACCOUNT_TRANSFER_CARD_3_LUHN = auto()
    ACCOUNT_TRANSFER_CARD_4_CARD_EXISTENCE = auto()
    ACCOUNT_TRANSFER_SUM_1_ENTER = auto()
    ACCOUNT_TRANSFER_SUM_2_CHECK_SUM = auto()
    ACCOUNT_TRANSFER_SUM_3_TRANSFER = auto()

    ACCOUNT_CLOSE = auto()
    ACCOUNT_LOG_OUT = auto()
    EXIT = auto()


class StateMachine:

    def __init__(self):
        self._state: Stage = Stage.NONE

    def switch_state(self, choice: int = 0) -> Stage:
        if self._state == Stage.NONE:
            self._state = Stage.MAIN_MENU

        elif self._state == Stage.MAIN_MENU:
            self._state = Stage.CREATE_ACCOUNT if choice == 1 \
                else Stage.LOG_INTO_ACCOUNT if choice == 2 \
                else Stage.EXIT

        elif self._state == Stage.CREATE_ACCOUNT:
            self._state = Stage.MAIN_MENU

        elif self._state == Stage.LOG_INTO_ACCOUNT:
            self._state = Stage.ACCOUNT_MENU if choice == 1 \
                else Stage.MAIN_MENU

        elif self._state == Stage.ACCOUNT_MENU:
            self._state = Stage.ACCOUNT_BALANCE if choice == 1 \
                else Stage.ACCOUNT_ADD_INCOME if choice == 2 \
                else Stage.ACCOUNT_TRANSFER_CARD_1_ENTER if choice == 3 \
                else Stage.ACCOUNT_CLOSE if choice == 4 \
                else Stage.ACCOUNT_LOG_OUT if choice == 5 \
                else Stage.EXIT

        elif self._state == Stage.ACCOUNT_BALANCE \
                or self._state == Stage.ACCOUNT_ADD_INCOME:
            self._state = Stage.ACCOUNT_MENU

        elif self._state == Stage.ACCOUNT_TRANSFER_CARD_1_ENTER:
            self._state = Stage.ACCOUNT_TRANSFER_CARD_2_SAME_ACCOUNT

        elif self._state == Stage.ACCOUNT_TRANSFER_CARD_2_SAME_ACCOUNT:
            self._state = Stage.ACCOUNT_TRANSFER_CARD_3_LUHN if choice == 1 \
                else Stage.ACCOUNT_MENU

        elif self._state == Stage.ACCOUNT_TRANSFER_CARD_3_LUHN:
            self._state = Stage.ACCOUNT_TRANSFER_CARD_4_CARD_EXISTENCE if choice == 1 \
                else Stage.ACCOUNT_MENU

        elif self._state == Stage.ACCOUNT_TRANSFER_CARD_4_CARD_EXISTENCE:
            self._state = Stage.ACCOUNT_TRANSFER_SUM_1_ENTER if choice == 1 \
                else Stage.ACCOUNT_MENU

        elif self._state == Stage.ACCOUNT_TRANSFER_SUM_1_ENTER:
            self._state = Stage.ACCOUNT_TRANSFER_SUM_2_CHECK_SUM

        elif self._state == Stage.ACCOUNT_TRANSFER_SUM_2_CHECK_SUM:
            self._state = Stage.ACCOUNT_TRANSFER_SUM_3_TRANSFER if choice == 1 \
                else Stage.ACCOUNT_MENU

        elif self._state == Stage.ACCOUNT_TRANSFER_SUM_3_TRANSFER:
            self._state = Stage.ACCOUNT_MENU

        elif self._state == Stage.ACCOUNT_LOG_OUT \
                or self._state == Stage.ACCOUNT_CLOSE:
            self._state = Stage.MAIN_MENU

        return self._state

    def going_on(self) -> bool:
        return self._state is not Stage.EXIT
