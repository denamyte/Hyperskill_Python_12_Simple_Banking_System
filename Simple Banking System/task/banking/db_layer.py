import sqlite3 as sql
from typing import Union, Optional
from account import Account


class DBLayer:
    DB_NAME = 'card.s3db'
    QUERY_CREATE_DB = f'''
        CREATE TABLE IF NOT EXISTS card (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            number TEXT,
            pin TEXT,
            balance INTEGER DEFAULT 0
        );'''
    QUERY_INSERT_CARD = f'''
        INSERT INTO card(number, pin, balance)
            VALUES (?, ?, ?);'''
    QUERY_COUNT_CARD = f'''
        SELECT COUNT(*) AS cnt 
        FROM card;'''
    QUERY_CARD_BY_NUMBER = f'''
        SELECT id, number, pin, balance
        FROM card
        WHERE number = :num;'''
    QUERY_ADD_INCOME = f'''
        UPDATE card
        SET balance = balance + :inc
        WHERE number = :num;'''

    def __init__(self):
        self.conn: Union[None, sql.Connection] = None
        self._connection()
        self._create_db()

    def _connection(self):
        self.conn = sql.connect(self.DB_NAME)

    def _create_db(self):
        cursor = self.conn.cursor()
        cursor.execute(self.QUERY_CREATE_DB)
        self.conn.commit()
        cursor.close()

    def create_account(self, acc: Account):
        cursor = self.conn.cursor()
        cursor.execute(self.QUERY_INSERT_CARD, (acc.number, acc.pin, acc.balance))
        self.conn.commit()
        cursor.close()

    def get_account_by_number(self, number: str) -> Optional[Account]:
        cursor = self.conn.cursor().execute(self.QUERY_CARD_BY_NUMBER, {'num': number})
        fetch = cursor.fetchone()
        acc = None if not fetch else Account(*fetch)
        cursor.close()
        return acc

    def add_income(self, number: str, income: int):
        cursor = self.conn.cursor().execute(self.QUERY_ADD_INCOME, {'num': number, 'inc': income})
        self.conn.commit()
        cursor.close()
