from data.collector.accumulators.time_returns.DailyReturnsAcc import DailyReturnsAcc
from data.collector.accumulators.time_returns.MonthlyReturnsAcc import MonthlyReturnsAcc
from data.collector.accumulators.time_returns.WeeklyReturnsAcc import WeeklyReturnsAcc

CLASS_REGISTRY = {
    "DAILY_RETURNS": DailyReturnsAcc,
    "WEEKLY_RETURNS": WeeklyReturnsAcc,
    "MONTHLY_RETURNS": MonthlyReturnsAcc
}
