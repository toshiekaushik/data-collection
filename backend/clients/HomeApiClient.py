import httpx
from pydantic import BaseModel

class DefaultResp(BaseModel):
    status: str

class HomeApiClient:
    def __init__(self, http: httpx.AsyncClient):
        self._http = http

    async def health_check(self) -> DefaultResp:
        resp = await self._http.get("/health")
        resp.raise_for_status()
        return DefaultResp.model_validate(resp.json())