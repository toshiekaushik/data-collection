from pydantic import BaseModel
from datetime import date

class InsertReturnsTiingoRequest(BaseModel):
    tickers: list[str]

class HomeAPIReturnsTiingoRequest(BaseModel):
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