from curl_cffi import Request
from fastapi import APIRouter, Depends

from backend.clients.HomeApiClient import HomeApiClient
from backend.clients.request_models import PlayerInfoInput
from backend.clients.response_models import PlayerInfoResp
from collector.clients.nba.NbaApi import NbaApi
from collector.clients.nba.Player import Player

nba_router = APIRouter(
    prefix = "/nba",
    tags = ['nba']
)

def get_homeapi_client(req: Request) -> HomeApiClient:
    return req.app.state.homeapi

def get_player_client() -> Player:
    return Player()

@nba_router.get("/player")
async def get_player_info(
        player_info_input: PlayerInfoInput,
        player_api: Player = Depends(get_player_client)
) -> PlayerInfoResp:
    player_info = player_api.get_player_info(player_info_input.name)[0]

    print(player_info)

    return PlayerInfoResp(
        id = player_info["id"],
        full_name = player_info["full_name"],
        first_name = player_info["first_name"],
        last_name = player_info["last_name"],
        is_active = player_info["is_active"]
    )
