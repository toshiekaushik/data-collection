import httpx

from backend.clients.request_models import HomeAPIReturnsTiingoRequest
from backend.clients.response_models import DefaultResp, MonthlyReturnsTiingoResp, WeeklyReturnsTiingoResp


class HomeApiClient():
    def __init__(self, http: httpx.AsyncClient):
        self._http = http

    async def health_check(self) -> DefaultResp:
        resp = await self._http.get("/health")
        resp.raise_for_status()
        return DefaultResp.model_validate(resp.json())

    async def insert_monthly_returns_tiingo(
            self,
            ret: HomeAPIReturnsTiingoRequest
    ) -> MonthlyReturnsTiingoResp:
        resp = await self._http.post(
            url = "/equity/returns/tiingo/monthly",
            json = ret.model_dump(mode = 'json')
        )

        return MonthlyReturnsTiingoResp.model_validate(resp.json())

    async def insert_weekly_returns_tiingo(
            self,
            ret: HomeAPIReturnsTiingoRequest
    ) -> WeeklyReturnsTiingoResp:
        resp = await self._http.post(
            url = "/equity/returns/tiingo/weekly",
            json = ret.model_dump(mode = 'json')
        )