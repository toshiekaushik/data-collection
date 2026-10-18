from collections import defaultdict

from backend.clients.request_models import InsertReturnsTiingoRequest, ReturnsPeriod
from collector.accumulators.time_returns.DailyReturnsAcc import DailyReturnsAcc
from collector.accumulators.time_returns.MonthlyReturnsAcc import MonthlyReturnsAcc
from collector.accumulators.time_returns.TiingoReturnsAcc import TiingoReturnsAcc
from collector.accumulators.time_returns.WeeklyReturnsAcc import WeeklyReturnsAcc

import pandas as pd

class ReturnsDataByPeriod:
    def __init__(
        self,
        daily_acc: DailyReturnsAcc,
        weekly_acc: WeeklyReturnsAcc,
        monthly_acc: MonthlyReturnsAcc,
        tiingo_acc: TiingoReturnsAcc
    ):
        self.daily_acc = daily_acc
        self.weekly_acc = weekly_acc
        self.monthly_acc = monthly_acc
        self.tiingo_acc = tiingo_acc

    def execute(self, req: InsertReturnsTiingoRequest) -> pd.DataFrame:
        match req.period:
            case ReturnsPeriod.DAILY:
                return self.daily_acc.execute(tickers = req.tickers)
            case ReturnsPeriod.WEEKLY:
                return self.weekly_acc.execute(tickers = req.tickers)
            case ReturnsPeriod.MONTHLY:
                return self.monthly_acc.execute(tickers = req.tickers)

    def execute_v2(self, req: InsertReturnsTiingoRequest) -> pd.DataFrame:
        params = self._createTiingoParamsFromReq(req)
        return self.tiingo_acc.execute(
            tickers = req.tickers,
            params = params
        )

    def _createTiingoParamsFromReq(self, req: InsertReturnsTiingoRequest) -> defaultdict:
        params = defaultdict(str)
        if req.start_date: params['start_date'] = req.start_date
        if req.end_date: params['end_date'] = req.end_date
        return params
