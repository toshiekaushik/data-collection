from collections import defaultdict
from io import StringIO

from collector.accumulators.Accumulate import Accumulate
from collector.clients.tiingo.api.eod import EOD
from collector.clients.tiingo.api.endpoints import TiingoEndpoints
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

TIINGO_TOKEN = os.getenv('TIINGO_TOKEN')
HEADERS = {
    'Content-Type': 'application/json'
}

class DailyReturnsAcc(Accumulate):

    def execute(self, tickers: list[str]) -> None:
        dfs = []
        for idx, ticker in enumerate(tickers):
            daily_returns_req = self.buildRequest(ticker)
            resp = daily_returns_req.getResponse()
            df = pd.read_csv(StringIO(resp.text))
            df["ticker"] = ticker
            dfs.append(df)
        new_df = pd.concat(dfs, ignore_index = True)
        return new_df

    def buildRequest(self, ticker: str) -> EOD:
        daily_returns = EOD(TiingoEndpoints.END_OF_DAY, HEADERS, {})
        daily_returns.setTicker(ticker)
        daily_returns.setFormat("csv")
        daily_returns.setToken(TIINGO_TOKEN)
        daily_returns.setStartDate("2026-01-01")
        return daily_returns



