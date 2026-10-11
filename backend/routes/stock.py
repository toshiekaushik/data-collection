from fastapi import APIRouter

stock_router = APIRouter(prefix = "/stocks", tags = ['stocks'])

@stock_router.get("/")
async def stock_default_endpt():
    return {"message": "THIS IS STOCK DEFAULT ENDPOINT"}