from .TiingoClient import TiingoClient

class Search(TiingoClient):
    def __init__(self, endpoint: str, headers: dict, params: dict):
        super().__init__(endpoint, headers, params)

    def setTicker(self, ticker: str) -> None:
        self.params["query"] = ticker

    def setExactMatch(self, match: bool) -> None:
        self.params["exactTickerMatch"] = str(match).lower()

    def setLimit(self, limit: int) -> None:
        self.params["limit"] = limit
