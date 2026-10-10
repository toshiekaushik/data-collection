from io import StringIO

from dotenv import load_dotenv
import os
import pandas as pd

from data.collector.accumulators.Accumulate import Accumulate
from data.collector.clients.tiingo.api.endpoints import TiingoEndpoints
from data.collector.clients.tiingo.api.eod import EOD
from data.collector.dal.db.postgress.TimeReturnsPG import TimeReturnsPG
load_dotenv()

API_KEY = os.getenv("TIINGO_TOKEN")
HEADERS = {
    'Content-Type': 'application/json'
}

class WeeklyReturnsAcc(Accumulate):

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
        self.time_returns_db.read_df(new_df, "alpha_tester_v1")
        self.time_returns_db.close_connection()

    # def get_recent_returns(self) -> None:
    #     dfs = []
    #     for idx, ticker in enumerate(self.tickers):
    #         daily_returns_req = self.buildRequest(ticker)
    #         resp = daily_returns_req.getResponse()
    #         df = pd.read_csv(StringIO(resp.text))
    #         df["ticker"] = ticker
    #         dfs.append(df)


    def buildRequest(self, ticker: str) -> EOD:
        weekly_returns = EOD(TiingoEndpoints.END_OF_DAY, HEADERS, {})
        weekly_returns.setTicker(ticker)
        weekly_returns.setFormat("csv")
        weekly_returns.setToken(API_KEY)
        weekly_returns.setFreq("weekly")
        weekly_returns.setStartDate("2014-8-07")
        return weekly_returns