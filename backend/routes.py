from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Hello Lord Kaushik, This Data Accumulator for Equity data. This is coming from the routes file and router."}
