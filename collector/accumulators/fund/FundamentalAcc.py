import os

from dotenv import load_dotenv

from data.collector.accumulators.Accumulate import Accumulate

load_dotenv()

API_KEY = os.getenv("TIINGO_TOKEN")
HEADERS = {
    'Content-Type': 'application/json'
}

class FundamentalAcc(Accumulate):
    def __init__(self, tickers: list[str]):
        self.tickers = tickers