import datetime

from pandas.core.interchange.dataframe_protocol import DataFrame


class FactorRepo():
    def get_momentum_weekly(self, startDate: datetime, endDate: datetime, tickers: str) -> DataFrame:
        pass

    def get_reversal_weekly(self, startDate: datetime, endDate: datetime, tickers: str) -> DataFrame:
        pass

    def get_volatility_20_days(self, startDate: datetime, endDate: datetime, tickers: str) -> DataFrame:
        pass

    # def add_factor(self):