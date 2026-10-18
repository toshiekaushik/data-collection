import pandas as pd
from fastapi import APIRouter, Depends, Request

from backend.clients.HomeApiClient import HomeApiClient
from backend.clients.ReturnsDataByPeriod import ReturnsDataByPeriod
from backend.clients.request_models import InsertReturnsTiingoRequest, HomeAPIReturnsTiingoRequest
from collector.accumulators.time_returns.DailyReturnsAcc import DailyReturnsAcc
from collector.accumulators.time_returns.MonthlyReturnsAcc import MonthlyReturnsAcc
from collector.accumulators.time_returns.TiingoReturnsAcc import TiingoReturnsAcc
from collector.accumulators.time_returns.WeeklyReturnsAcc import WeeklyReturnsAcc

stock_router = APIRouter(prefix = "/stocks", tags = ['stocks'])

def get_homeapi_client(req: Request) -> HomeApiClient:
    return req.app.state.homeapi

def get_monthly_returns_tiingo(req: Request) -> MonthlyReturnsAcc:
    return MonthlyReturnsAcc()

def get_weekly_returns_tiingo(req: Request) -> MonthlyReturnsAcc:
    return WeeklyReturnsAcc()

def get_daily_returns_tiingo(req: Request) -> DailyReturnsAcc:
    return DailyReturnsAcc()

def get_tiingo_returns(req: Request) -> TiingoReturnsAcc:
    return TiingoReturnsAcc()

@stock_router.get("/")
async def stock_default_endpt():
    return {"message": "THIS IS STOCK DEFAULT ENDPOINT"}

@stock_router.post("/returns/tiingo/monthly")
async def monthly_returns_tiingo(
        req: InsertReturnsTiingoRequest,
        homeapi: HomeApiClient = Depends(get_homeapi_client),
        acc: MonthlyReturnsAcc = Depends(get_monthly_returns_tiingo)
):
    tickers = req.tickers
    data = acc.execute(tickers = tickers)

    for (idx, row) in data.iterrows():
        req = HomeAPIReturnsTiingoRequest(**row.to_dict())
        resp = await homeapi.insert_monthly_returns_tiingo(req)

    return {"message": "GRABBED AND INSERTED MONTHLY RETURNS"}

@stock_router.post("/returns/tiingo/weekly")
async def weekly_returns_tiingo(
        req: InsertReturnsTiingoRequest,
        homeapi: HomeApiClient = Depends(get_homeapi_client),
        acc: WeeklyReturnsAcc = Depends(get_weekly_returns_tiingo)
):
    tickers = req.tickers
    data = acc.execute(tickers = tickers)

    for (idx, row) in data.iterrows():
        req = HomeAPIReturnsTiingoRequest(**row.to_dict())
        resp = await homeapi.insert_weekly_returns_tiingo(req)

    return {"message": "GRABBED AND INSERTED MONTHLY RETURNS"}

def get_returns_data_by_period(
    daily_acc: DailyReturnsAcc = Depends(get_daily_returns_tiingo),
    weekly_acc: WeeklyReturnsAcc = Depends(get_weekly_returns_tiingo),
    monthly_acc: MonthlyReturnsAcc = Depends(get_monthly_returns_tiingo),
    tiingo_acc: TiingoReturnsAcc = Depends(get_tiingo_returns)
) -> ReturnsDataByPeriod:
    return ReturnsDataByPeriod(
        daily_acc=daily_acc,
        weekly_acc=weekly_acc,
        monthly_acc=monthly_acc,
        tiingo_acc = tiingo_acc
    )

@stock_router.post("/returns/tiingo")
async def get_returns_tiingo(
        req: InsertReturnsTiingoRequest,
        homeapi: HomeApiClient = Depends(get_homeapi_client),
        returns_service: ReturnsDataByPeriod = Depends(get_returns_data_by_period),
):
    data = returns_service.execute_v2(req)

    for (idx, row) in data.iterrows():
        req = HomeAPIReturnsTiingoRequest(
            **{**row.to_dict(), "period": req.period}
        )
        resp = await homeapi.insert_returns_tiingo(req)

    return {"message": "GRABBED AND INSERTED MONTHLY RETURNS"}
