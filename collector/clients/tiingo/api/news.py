from .TiingoClient import TiingoClient

class News(TiingoClient):
    def __init__(self, endpoint: str, headers: dict, params: dict):
        super().__init__(endpoint, headers, params)

    def setSources(self, sources: list[str]) -> None:
        self.params['source'] = sources

    def setStartDate(self, startDate: str) -> None:
        self.params['startDate'] = startDate

    def setEndDate(self, endDate: str) -> None:
        self.params['endDate'] = endDate

    def setLimit(self, limit: int) -> None:
        self.params['limit'] = limit

    # TODO: Create Enum File to enforce parameter can only two values ("publishedDate", "crawlDate")
    def setSort(self, val: str) -> None:
        self.params['sortBy'] = val