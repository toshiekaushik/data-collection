from data.collector.clients.tiingo.api.TiingoClient import TiingoClient


class EOD(TiingoClient):
    def __init__(self, endpt: str, headers: dict, params: dict):
        super().__init__(endpt, headers, params)

    def setTicker(self, ticker: str) -> None:
        self.setEndpoint(self.endpoint.format(ticker=ticker))

    # TODO: Need to set restrict cols to only ones that you can query (https://www.tiingo.com/documentation/end-of-day)
    def setColumns(self, cols: list[str]) -> None:
        self.params["columns"] = cols

    # TODO: Need to set restrict cols to only ones that you can query (https://www.tiingo.com/documentation/end-of-day)
    def setSort(self, col: str) -> None:
        self.params["sort"] = "-" + col

    # TODO: Need to set restrict freq to only ("daily", "weekly", "monthly", "annualy")
    def setFreq(self, freq: str) -> None:
        self.params["resampleFreq"] = freq

    # TODO: Enforce date format
    def setStartDate(self, startDate: str) -> None:
        self.params["startDate"] = startDate

    # TODO: Enforce date format
    def setEndDate(self, endDate: str) -> None:
        self.params["endDate"] = endDate

