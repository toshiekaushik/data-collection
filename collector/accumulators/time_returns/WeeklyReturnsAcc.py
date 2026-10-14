from io import StringIO

from dotenv import load_dotenv
import os
import pandas as pd

from backend.clients.HomeApiClient import HomeApiClient
from collector.accumulators.Accumulate import Accumulate
from collector.clients.tiingo.api.endpoints import TiingoEndpoints
from collector.clients.tiingo.api.eod import EOD
load_dotenv()

API_KEY = os.getenv("TIINGO_TOKEN")
HEADERS = {
    'Content-Type': 'application/json'
}

class WeeklyReturnsAcc(Accumulate):

    def __init__(self):
        super()

    def execute(self, tickers: list[str]) -> pd.DataFrame:
        dfs = []
        for idx, ticker in enumerate(tickers):
            daily_returns_req = self.buildRequest(ticker)
            resp = daily_returns_req.getResponse()
            df = pd.read_csv(StringIO(resp.text))
            df["ticker"] = ticker
            dfs.append(df)
        new_df = pd.concat(dfs, ignore_index = True)
        return new_df

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