from api.search import Search
from api.news import News
from api.fundamentals import Fundamentals, StatementData, DailyData
from api.endpoints import TiingoEndpoints as ENDPTS

TIINGO_TOKEN = "a2b70640dcb7265f5bc4c7653f52f4c9a6516b6f"

HEADERS = {
    'Content-Type': 'application/json'
}

def testSearchEndpt():
    params = {}
    search_req = Search(endpoint = ENDPTS.SEARCH,
                        headers = HEADERS,
                        params = params)
    search_req.setTicker("AAPL")
    search_req.setExactMatch(False)
    search_req.setToken(TIINGO_TOKEN)
    search_req.setLimit(5)
    resp = search_req.getResponse()
    print(resp.json())

def testNewsEndpt():
    params = {}
    news_req = News( endpoint = ENDPTS.NEWS,
                     headers = HEADERS,
                     params = params)
    news_req.setToken(TIINGO_TOKEN)
    news_req.setSources(['bloomberg.com'])
    news_req.setLimit(5)
    resp = news_req.getResponse()
    print(resp.json())

def testFundEndpt():
    params = {}
    fund_req = Fundamentals(endpoint = ENDPTS.FUNDAMENTAL_DEFINITION,
                     headers = HEADERS,
                     params = params)
    fund_req.setToken(TIINGO_TOKEN)
    fund_req.setTickers(["KO"])
    resp = fund_req.getResponse()
    print(resp.json())

def testStatementEndpt():
    params = {}
    stat_req = StatementData(endpt = ENDPTS.FUNDAMENTAL_STATEMENT,
                             headers = HEADERS,
                             params = params)
    stat_req.setTicker("msft")
    stat_req.setToken(TIINGO_TOKEN)
    resp = stat_req.getResponse()
    print(resp.json())

def testDailyFundEndpt():
    params = {}
    daily_fund_req = DailyData(endpt = ENDPTS.DAILY_FUNDAMENTAL,
                             headers = HEADERS,
                             params = params)
    daily_fund_req.setTicker("AAPL")
    daily_fund_req.setToken(TIINGO_TOKEN)
    daily_fund_req.setStartDate("2026-05-15")
    resp = daily_fund_req.getResponse()
    print(resp.json())

def main():
    testDailyFundEndpt()

main()