import datetime

import pandas as pd
from pandas import DataFrame

from data.collector.dal.db.postgress.PGConnection import PGConnection
from data.collector.dal.interfaces.FactorRepo import FactorRepo
from data.collector.dal.models.momentum.Momentum import Momentum


class FactorPG(FactorRepo):

    def __init__(self):
        self.pgdb = PGConnection(
            host = "localhost",
            dbname = "equity",
            user = "postgres",
            password = "password",
            port = 5432
        )

    def get_momentum_weekly(
            self,
            startDate: datetime,
            endDate: datetime,
            tickers: list[str]
    ) -> DataFrame:
        query = """
            SELECT ticker, date, mom_4_1, mom_12_1
            FROM weekly_momentum_factor
            WHERE ticker = ANY(%s)
              AND date BETWEEN %s AND %s
        """

        raw_df = pd.read_sql(
            query,
            con=self.pgdb.conn,
            params=(tickers, startDate, endDate)
        )

        return raw_df

    def get_reversal_weekly(
            self,
            startDate: datetime,
            endDate: datetime,
            tickers: list[str]
    ) -> DataFrame:
        query = """
            SELECT ticker, date, reversal_chg
            FROM weekly_reversal_factor
            WHERE ticker = ANY(%s)
              AND date BETWEEN %s AND %s
        """

        raw_df = pd.read_sql(
            query,
            con=self.pgdb.conn,
            params=(tickers, startDate, endDate)
        )

        return raw_df

    def get_volatility_20_days(
            self,
            startDate: datetime,
            endDate: datetime,
            tickers: list[str]
    ) -> DataFrame:
        query = """
            SELECT ticker, date, volatility
            FROM volatility_20_days
            WHERE ticker = ANY(%s)
              AND date BETWEEN %s AND %s
        """

        raw_df = pd.read_sql(
            query,
            con=self.pgdb.conn,
            params=(tickers, startDate, endDate)
        )

        return raw_df