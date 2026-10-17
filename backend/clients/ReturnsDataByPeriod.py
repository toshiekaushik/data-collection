from backend.clients.request_models import InsertReturnsTiingoRequest, ReturnsPeriod
from collector.accumulators.time_returns.DailyReturnsAcc import DailyReturnsAcc
from collector.accumulators.time_returns.MonthlyReturnsAcc import MonthlyReturnsAcc
from collector.accumulators.time_returns.WeeklyReturnsAcc import WeeklyReturnsAcc

import pandas as pd

class ReturnsDataByPeriod:
    def __init__(
        self,
        daily_acc: DailyReturnsAcc,
        weekly_acc: WeeklyReturnsAcc,
        monthly_acc: MonthlyReturnsAcc,
    ):
        self.daily_acc = daily_acc
        self.weekly_acc = weekly_acc
        self.monthly_acc = monthly_acc

    def execute(self, req: InsertReturnsTiingoRequest) -> pd.DataFrame:
        match req.period:
            case ReturnsPeriod.DAILY:
                return self.daily_acc.execute(tickers=req.tickers)
            case ReturnsPeriod.WEEKLY:
                return self.weekly_acc.execute(tickers=req.tickers)
            case ReturnsPeriod.MONTHLY:
                return self.monthly_acc.execute(tickers=req.tickers)