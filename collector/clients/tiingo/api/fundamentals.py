from .TiingoClient import TiingoClient

class Fundamentals(TiingoClient):
    def __init__(self, endpoint: str, headers: dict, params: dict):
        super().__init__(endpoint, headers, params)

    def setTickers(self, tickers: list[str]) -> None:
        self.params["tickers"] = tickers

class StatementData(TiingoClient):
    def __init__(self, endpt: str, headers: dict, params: dict):
        super().__init__(endpt, headers, params)

    def setTicker(self, ticker: str) -> None:
        self.endpoint = self.endpoint.format(ticker = ticker)

    # TODO: enforce startDate as Date
    def setStartDate(self, startDate: str) -> None:
        self.params["startDate"] = startDate

class DailyData(StatementData):
    def __init__(self, endpt: str, headers: dict, params: dict):
        super().__init__(endpt, headers, params)
