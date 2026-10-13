from fastapi import APIRouter, Depends, Request

from backend.clients.HomeApiClient import HomeApiClient
from backend.clients.request_models import InsertMonthlyReturnsTiingoRequest, HomeAPIMonthlyReturnsTiingoRequest
from backend.clients.response_models import MonthlyReturnsTiingoResp
from collector.accumulators.time_returns.MonthlyReturnsAcc import MonthlyReturnsAcc

stock_router = APIRouter(prefix = "/stocks", tags = ['stocks'])

def get_homeapi_client(req: Request) -> HomeApiClient:
    return req.app.state.homeapi

def get_monthly_returns_tiingo(req: Request) -> MonthlyReturnsAcc:
    return MonthlyReturnsAcc()

@stock_router.get("/")
async def stock_default_endpt():
    return {"message": "THIS IS STOCK DEFAULT ENDPOINT"}

@stock_router.post("/returns/tiingo/monthly")
async def monthly_returns_tiingo(
        req: InsertMonthlyReturnsTiingoRequest,
        homeapi: HomeApiClient = Depends(get_homeapi_client),
        acc: MonthlyReturnsAcc = Depends(get_monthly_returns_tiingo)
):
    tickers = req.tickers
    data = acc.execute(tickers = tickers)

    for (idx, row) in data.iterrows():
        req = HomeAPIMonthlyReturnsTiingoRequest(**row.to_dict())
        resp = await homeapi.insert_monthly_returns_tiingo(req)

    return {"message": "GRABBED AND INSERTED MONTHLY RETURNS"}
