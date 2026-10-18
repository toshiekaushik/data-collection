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

class TiingoReturnsAcc(Accumulate):

    def execute(self,
        tickers: list[str],
        params: defaultdict[str]
    ) -> None:
        dfs = []

        for idx, ticker in enumerate(tickers):
            returns_req = self.buildRequest(ticker, params)
            resp = returns_req.getResponse()
            df = pd.read_csv(StringIO(resp.text))
            df["ticker"] = ticker
            dfs.append(df)

        new_df = pd.concat(dfs, ignore_index = True)
        return new_df

    def buildRequest(self,
        ticker: str,
        params: defaultdict
    ) -> EOD:

        print("THIS IS PARAMS: ", params)
        returns = EOD(TiingoEndpoints.END_OF_DAY, HEADERS, params)
        returns.setToken(TIINGO_TOKEN)

        # Required For Use Case
        returns.setTicker(ticker)
        returns.setFormat(params['format'])
        returns.setFreq(params['period'])

        # Optional Params
        if 'start_date' in params: returns.setStartDate(params['start_date'])
        if 'end_date' in params: returns.setEndDate(params['end_date'])
        return returns
