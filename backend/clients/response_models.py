from pydantic import BaseModel

class DefaultResp(BaseModel):
    status: str

class MonthlyReturnsTiingoResp(BaseModel):
    status: str

class WeeklyReturnsTiingoResp(BaseModel):
    inserted: str

class PlayerInfoResp(BaseModel):
    id: int
    full_name: str
    first_name: str
    last_name: str
    is_active: bool