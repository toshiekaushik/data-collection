from fastapi import APIRouter, Depends, Request

from backend.clients.HomeApiClient import HomeApiClient

router = APIRouter(prefix = "/default", tags = ["default"])

def get_homeapi_client(req: Request) -> HomeApiClient:
    return req.app.state.homeapi

@router.get("/")
async def hello_world():
    return {"message": "Hello Lord Kaushik, This Data Accumulator for Equity data. This is coming from the routes folder and default.py."}

@router.get("/homeapi/health")
async def check_health(
        homapi: HomeApiClient = Depends(get_homeapi_client)
):
    return await homapi.health_check()
