from pydantic import BaseModel
from datetime import date
from enum import Enum

class ReturnsPeriod(str, Enum):
    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"

class InsertReturnsTiingoRequest(BaseModel):
    tickers: list[str]
    period: ReturnsPeriod


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
    period: str