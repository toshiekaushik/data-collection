from pydantic import BaseModel
from datetime import date

class InsertMonthlyReturnsTiingoRequest(BaseModel):
    tickers: list[str]

class HomeAPIMonthlyReturnsTiingoRequest(BaseModel):
    date: date
    ticker: str
    close: float
    high: float
    low: float
    open: float
    volume: int
    adjClose: float
    adjHigh: float
    adjLow: float
    adjOpen: float
    adjVolume: int
    divCash: float
    splitFactor: float