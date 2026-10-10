
class Stock:
    def __init__(self, ticker: str):
        self._ticker = ticker

    @property
    def ticker(self) -> str:
        return self._ticker