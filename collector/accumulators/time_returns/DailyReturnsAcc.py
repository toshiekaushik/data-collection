from io import StringIO

from data.collector.accumulators.Accumulate import Accumulate
from data.collector.clients.tiingo.api.eod import EOD
from data.collector.clients.tiingo.api.endpoints import TiingoEndpoints
import pandas as pd
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from data.collector.dal.db.postgress.TimeReturnsPG import TimeReturnsPG

load_dotenv()

TIINGO_TOKEN = os.getenv('TIINGO_TOKEN')
HEADERS = {
    'Content-Type': 'application/json'
}

class DailyReturnsAcc(Accumulate):

    def __init__(self, tickers: list[str]):
        self.tickers = tickers
        self.time_returns_db = TimeReturnsPG()

    def execute(self) -> None:
        dfs = []
        for idx, ticker in enumerate(self.tickers):
            daily_returns_req = self.buildRequest(ticker)
            resp = daily_returns_req.getResponse()
            df = pd.read_csv(StringIO(resp.text))
            df["ticker"] = ticker
            dfs.append(df)
        new_df = pd.concat(dfs, ignore_index = True)
        self.time_returns_db.read_df(new_df, "daily_returns")
        self.time_returns_db.close_connection()

    def buildRequest(self, ticker: str) -> EOD:
        daily_returns = EOD(TiingoEndpoints.END_OF_DAY, HEADERS, {})
        daily_returns.setTicker(ticker)
        daily_returns.setFormat("csv")
        daily_returns.setToken(TIINGO_TOKEN)
        daily_returns.setStartDate("2026-01-01")
        return daily_returns



