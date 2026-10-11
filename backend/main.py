import uvicorn

from fastapi import FastAPI
from .routes import default, stock

app = FastAPI()
app.include_router(default.router)
app.include_router(stock.stock_router)

if __name__ == "__main__":
    uvicorn.run(app, host = "127.0.0.1", port = 3003)