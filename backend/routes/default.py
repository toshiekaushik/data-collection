from fastapi import APIRouter

router = APIRouter(prefix = "/default", tags = ["default"])

@router.get("/")
async def hello_world():
    return {"message": "Hello Lord Kaushik, This Data Accumulator for Equity data. This is coming from the routes folder and default.py."}