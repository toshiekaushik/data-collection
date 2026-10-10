from CoreConsts import TECH_TICKERS
from data.collector.accumulators.time_returns.DailyReturnsAcc import DailyReturnsAcc
from data.collector.accumulators.time_returns.MonthlyReturnsAcc import MonthlyReturnsAcc
from data.collector.accumulators.time_returns.WeeklyReturnsAcc import WeeklyReturnsAcc


# acc = MonthlyReturnsAcc(tickers = ["MSFT", "AMZN", "GOOG", "AAPL", "NFLX"])
# acc = WeeklyReturnsAcc(tickers = TECH_TICKERS)
acc = DailyReturnsAcc(tickers = TECH_TICKERS)
acc.execute()