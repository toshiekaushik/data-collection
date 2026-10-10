import datetime
import os

import pandas as pd
from pandas import DataFrame
from sqlalchemy import create_engine

from data.collector.dal.db.postgress.PGConnection import PGConnection
from data.collector.dal.interfaces.TimeReturnsRepo import TimeReturnsRepo

class TimeReturnsPG(TimeReturnsRepo):
    def __init__(self):
        self.pgdb = PGConnection(
            host = "localhost",
            dbname = "equity",
            user = "postgres",
            password = "password",
            port = 5432
        )

    def infer_pg_type(self, dtype):
        if pd.api.types.is_integer_dtype(dtype):
            return "BIGINT"
        elif pd.api.types.is_float_dtype(dtype):
            return "DOUBLE PRECISION"
        elif pd.api.types.is_bool_dtype(dtype):
            return "BOOLEAN"
        elif pd.api.types.is_datetime64_any_dtype(dtype):
            return "TIMESTAMP"
        else:
            return "TEXT"

    def create_table(self, table: str, cols) -> None:
        columns = []
        for col in cols:
            col_type = self.infer_pg_type(col.dtype)
            columns.append(f'"{col}" {col_type}')

        cols_sql = ",\n    ".join(cols)

        return f"""
            CREATE TABLE IF NOT EXISTS {table} (
                {cols_sql}
            );
            """

    def read_csv(self, path: str, table: str, cols) -> None:
        conn, curr = self.pgdb.conn, self.pgdb.cursor

        create_sql = self.create_table(table, cols)
        curr.execute(create_sql)
        conn.commit()

        with open(path, "r") as f:
            with curr.copy(
                    f"COPY {table} FROM STDIN WITH CSV HEADER"
            ) as copy:
                copy.write(f.read())

        conn.commit()

    def read_df(self, data: DataFrame, table_name: str):
        engine = self.pgdb.getEngine()

        data.to_sql(
            table_name,
            con = engine,
            if_exists = "replace",
            index=False
        )

    def execute_query(self, query: str) -> DataFrame:
        print("Query being executed: ")
        print(query)
        conn = self.pgdb.conn
        with conn.cursor() as curr:
            curr.execute(query)
            rows = curr.fetchall()
            columns = [desc.name for desc in curr.description]
        return DataFrame(rows, columns = columns)

    def get_returns(self, startDate: datetime, endDate: datetime, tickers: list[str]) -> DataFrame:
        query = "SELECT ticker, date, open, high, low, close, volume FROM weekly_returns WHERE ticker = ANY(%s) AND date BETWEEN %s AND %s"
        raw_df = pd.read_sql(query, con = self.pgdb.conn, params = (tickers, startDate, endDate))
        return raw_df

    def get_returns_v2(self, startDate: datetime, endDate: datetime, tickers: list[str], table: str) -> DataFrame:
        query = "SELECT ticker, date, open, high, low, close, volume FROM alpha_tester_v1 WHERE ticker = ANY(%s) AND date BETWEEN %s AND %s"
        raw_df = pd.read_sql(query, con = self.pgdb.conn, params = (tickers, startDate, endDate))
        return raw_df

    def get_daily_returns(self, startDate: datetime, endDate: datetime, tickers: list[str]) -> DataFrame:
        query = "SELECT ticker, date, open, high, low, close, volume FROM daily_returns WHERE ticker = ANY(%s) AND date BETWEEN %s AND %s"
        raw_df = pd.read_sql(query, con=self.pgdb.conn, params=(tickers, startDate, endDate))
        return raw_df

    def upsert_df_columns(self, data: DataFrame, table_name: str) -> None:
        conn, curr = self.pgdb.conn, self.pgdb.cursor

        # 1. Ensure table exists first (if it doesn't, create it with all columns)
        cols_def = []
        for col in data.columns:
            col_type = self.infer_pg_type(data[col].dtype)
            cols_def.append(f'"{col}" {col_type}')

        create_sql = f"""
            CREATE TABLE IF NOT EXISTS {table_name} (
                {",\n    ".join(cols_def)}
            );
        """
        curr.execute(create_sql)
        conn.commit()

        # 2. Get existing columns from PostgreSQL database
        curr.execute("""
            SELECT column_name 
            FROM information_schema.columns 
            WHERE table_name = %s;
        """, (table_name,))
        existing_cols = {row[0] for row in curr.fetchall()}

        # 3. Find columns in DataFrame that are missing from the SQL table
        df_cols = set(data.columns)
        missing_cols = df_cols - existing_cols

        # 4. Alter the SQL table to add missing columns
        for col in missing_cols:
            col_type = self.infer_pg_type(data[col].dtype)
            alter_sql = f'ALTER TABLE {table_name} ADD COLUMN "{col}" {col_type};'
            curr.execute(alter_sql)
            print(f"Added missing column to PostgreSQL: {col} ({col_type})")

        conn.commit()

        # 5. Push data to SQL (using append or your preferred method via pandas/SQLAlchemy)
        engine = self.pgdb.getEngine()
        data.to_sql(
            table_name,
            con=engine,
            if_exists="append",
            index=False
        )

    def close_connection(self) -> None:
        self.pgdb.close()



