import sqlite3 as sql
from typing import Union, Optional
from account import Account


class DBLayer:
    DB_NAME = 'card.s3db'
    TABLE_NAME = 'card'
    QUERY_CREATE_DB = f'''
        CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            number TEXT,
            pin TEXT,
            balance INTEGER DEFAULT 0
        );'''
    QUERY_INSERT_CARD = f'''
        INSERT INTO {TABLE_NAME}(number, pin, balance)
            VALUES (?, ?, ?);'''
    QUERY_COUNT_CARD = f'''
        SELECT COUNT(*) AS cnt 
        FROM {TABLE_NAME};'''
    QUERY_CARD_BY_NUMBER = f'''
        SELECT id, number, pin, balance
        FROM {TABLE_NAME}
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
        cursor = self.conn.cursor().execute(self.QUERY_CARD_BY_NUMBER, {"num": number})
        fetch = cursor.fetchone()
        acc = None if not fetch else Account(*fetch)
        cursor.close()
        return acc
