import yfinance as yf

class Ticker(yf.Ticker):
    def __init__(self, ticker: str):
        super().__init__(ticker)

