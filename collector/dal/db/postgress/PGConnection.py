import os
from typing import Any
from dotenv import load_dotenv

import psycopg
from psycopg import Connection, Cursor
from sqlalchemy import create_engine

load_dotenv()

class PGConnection:
    def __init__(self, host: str,
                 dbname: str,
                 user: str,
                 password: str,
                 port: int):
        self.host = host
        self.dbname = dbname
        self.user = user
        self.password = password
        self.port = port
        self._conn = self.create_conn()
        self._cursor = self.conn.cursor()

    def create_conn(self) -> Connection:
        return psycopg.connect(
            host = self.host,
            dbname = self.dbname,
            user = self.user,
            password = self.password,
            port = self.port
        )

    def close(self):
        self._conn.close()
        self._cursor.close()

    def getEngine(self):
        return create_engine(os.getenv("PG_ENGINE"))

    @property
    def conn(self) -> Connection:
        return self._conn

    # @conn.setter
    # def conn(self):
    #     self.conn = psycopg.connect(
    #         host = self.host,
    #         dbname = self.dbname,
    #         user = self.user,
    #         password = self.password,
    #         port = self.port
    #     )

    @property
    def cursor(self) -> Cursor[Any]:
        return self._cursor
