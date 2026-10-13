import httpx

from backend.clients.request_models import HomeAPIMonthlyReturnsTiingoRequest
from backend.clients.response_models import DefaultResp, MonthlyReturnsTiingoResp
from collector.accumulators.time_returns.MonthlyReturnsAcc import MonthlyReturnsAcc


class HomeApiClient():
    def __init__(self, http: httpx.AsyncClient):
        self._http = http

    async def health_check(self) -> DefaultResp:
        resp = await self._http.get("/health")
        resp.raise_for_status()
        return DefaultResp.model_validate(resp.json())

    async def insert_monthly_returns_tiingo(
            self,
            ret: HomeAPIMonthlyReturnsTiingoRequest
    ) -> MonthlyReturnsTiingoResp:
        resp = await self._http.post(
            url="/equity/returns/tiingo/monthly",
            json=ret.model_dump(mode='json')  # 1. Use 'json=' instead of 'data=' for JSON payloads
        )

        return MonthlyReturnsTiingoResp.model_validate(resp.json())