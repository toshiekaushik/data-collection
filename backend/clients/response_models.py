from pydantic import BaseModel

class DefaultResp(BaseModel):
    status: str

class MonthlyReturnsTiingoResp(BaseModel):
    status: str

class WeeklyReturnsTiingoResp(BaseModel):
    inserted: str