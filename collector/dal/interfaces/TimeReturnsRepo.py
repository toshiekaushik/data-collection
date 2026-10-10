from pandas import DataFrame

from ..models.TimeReturns import TimeReturns
import datetime

class TimeReturnsRepo():
    def add_returns(self, returns: TimeReturns):
        pass

    def get_returns(self, startDate: datetime, endDate: datetime, tickers: list[str]):
        pass

    def delete_stock_entries(self, startDate: datetime, endDate: datetime, ticker: str) -> None:
        pass

    def get_daily_returns(self, startDate: datetime, endDate: datetime, tickers: list[str]):
        pass

    def read_csv(self, path: str, table: str, cols):
        pass

    def read_df(self, df: DataFrame, table_name: str):
        pass