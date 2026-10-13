from contextlib import asynccontextmanager, AsyncExitStack

import httpx

from fastapi import FastAPI

from backend.clients.HomeApiClient import HomeApiClient
from .routes import default, stock
from .endpts import HOMEAPI_BASE_URL

# App Instantiation
app = FastAPI()

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with AsyncExitStack() as stack:
        homeapi_http = await stack.enter_async_context(
            httpx.AsyncClient(
                base_url = HOMEAPI_BASE_URL,
                timeout = httpx.Timeout(5.0, connect = 1.0)
            )
        )

        app.state.homeapi = HomeApiClient(homeapi_http)

        yield

app = FastAPI(lifespan = lifespan)

# Router Set-Up
app.include_router(default.router)
app.include_router(stock.stock_router)