import datetime
import pandas as pd
import pandera.pandas as pa
from pandera.typing import DataFrame, Series

class TimeReturns(pa.DataFrameModel):
    ticker: Series[str]
    date: Series[datetime]
    open: Series[float]
    high: Series[float]
    low: Series[float]
    close: Series[float]
    volume: Series[int]

    class Config:
        # Automatically coerce types if your DB returns mismatched data types (e.g. strings to datetimes)
        coerce = True

    @property
    def date(self) -> datetime:
        return self._date

    @property
    def open(self) -> float:
        return self._open

    @property
    def high(self) -> float:
        return self._high

    @property
    def low(self) -> float:
        return self._low

    @property
    def close(self) -> float:
        return self._close

    @property
    def volume(self) -> int:
        return self._volume