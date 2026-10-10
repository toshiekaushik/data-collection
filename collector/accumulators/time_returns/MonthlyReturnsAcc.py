from io import StringIO

from data.collector.accumulators.Accumulate import Accumulate
from data.collector.clients.tiingo.api.eod import EOD
from data.collector.clients.tiingo.api.endpoints import TiingoEndpoints
import pandas as pd
import os
from dotenv import load_dotenv
from data.collector.dal.db.postgress.TimeReturnsPG import TimeReturnsPG

load_dotenv()

TIINGO_TOKEN = os.getenv('TIINGO_TOKEN')
HEADERS = {
    'Content-Type': 'application/json'
}

class MonthlyReturnsAcc(Accumulate):

    def __init__(self, tickers: list[str]):
        self.tickers = tickers
        self.time_returns_pg = TimeReturnsPG()

    def execute(self) -> None:
        dfs = []
        for idx, ticker in enumerate(self.tickers):
            time_returns_req = self.buildRequest(ticker)
            resp = time_returns_req.getResponse()
            df = pd.read_csv(StringIO(resp.text))
            df["ticker"] = ticker
            dfs.append(df)
        new_df = pd.concat(dfs, ignore_index = True)
        self.time_returns_pg.read_df(new_df, "monthly_returns")
        self.time_returns_pg.close_connection()

    def buildRequest(self, ticker: str) -> EOD:
        time_returns = EOD(TiingoEndpoints.END_OF_DAY, HEADERS, {})
        time_returns.setTicker(ticker)
        time_returns.setFormat("csv")
        time_returns.setToken(TIINGO_TOKEN)
        time_returns.setFreq("monthly")
        time_returns.setStartDate("2014-12-01")
        return time_returns



