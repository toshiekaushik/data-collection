import yfinance as yf

class Basket(yf.Tickers):
    def __init__(self, tickers: list[str], sector: str):
        super().__init__(tickers)
        self._sector = sector

    @property
    def sector(self) -> str:
        return self._sector

