import sqlite3 as sql
from typing import Union
from card import Card


class DBLayer:
    DB_NAME = 'card.s3db'
    TABLE_NAME = 'card'

    def __init__(self):
        self.conn: Union[None, sql.Connection] = None
        self.connection()
        self.create_db()

    def connection(self):
        self.conn = sql.connect(self.DB_NAME)

    def create_db(self):
        cursor = self.conn.cursor()
        cursor.execute(f'''
CREATE TABLE IF NOT EXISTS {self.TABLE_NAME} (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    number TEXT,
    pin TEXT,
    balance INTEGER DEFAULT 0
);''')
        self.conn.commit()
        cursor.close()

    def save_card(self, card: Card):
        cursor = self.conn.cursor()
        cursor.execute(f'''
INSERT INTO {self.TABLE_NAME}(number, pin, balance)
VALUES ({Card.number}, {card.pin}, {card.balance});''')
        self.conn.commit()
        cursor.close()
