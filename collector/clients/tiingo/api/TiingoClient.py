from collections import defaultdict
import requests
from requests import Response

class TiingoClient:
    def __init__(self, endpoint = "", headers = {}, params = {}):
        self.endpoint = endpoint
        self.headers = headers
        self.params = params

    def setHeaders(self, headers: defaultdict) -> None:
        self.headers = headers

    def setEndpoint(self, endpoint: str) -> None:
        self.endpoint = endpoint

    def setToken(self, token: str) -> None:
        self.params["token"] = token

    # TODO: Create Enums to enforce format return type ("json", "csv")
    def setFormat(self, format: str) -> None:
        self.params["format"] = format

    def getResponse(self) -> Response:
        print(self.params)
        print("endpoint: ", self.endpoint)
        return requests.get(
            url = self.endpoint,
            params = self.params,
            headers = self.headers
        )


