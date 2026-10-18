from pydantic import BaseModel, ConfigDict


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

# HAD CHATGPT GENERATE THIS MODEL FOR ME
class PlayerCareerTraditionalStats(BaseModel):
    model_config = ConfigDict(extra="ignore")

    PLAYER_ID: int
    SEASON_ID: str
    LEAGUE_ID: str
    TEAM_ID: int
    TEAM_ABBREVIATION: str
    PLAYER_AGE: float | None = None

    GP: int
    GS: int
    MIN: float

    FGM: float
    FGA: float
    FG_PCT: float
    FG3M: float
    FG3A: float
    FG3_PCT: float
    FTM: float
    FTA: float
    FT_PCT: float

    OREB: float
    DREB: float
    REB: float
    AST: float
    STL: float
    BLK: float
    TOV: float
    PF: float
    PTS: float
