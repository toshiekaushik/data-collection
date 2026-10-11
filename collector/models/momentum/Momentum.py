import datetime
import pandas as pd
import pandera.pandas as pa
from pandera.typing import DataFrame, Series

class Momentum(pa.DataFrameModel):
    ticker: Series[str]
    date: Series[datetime]
    mom_4_1: Series[float]

    class Config:
        coerce = True