from datetime import time

from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.static.players import get_active_players

from backend.clients.request_models import TraditionalCareerStatsReq
from backend.clients.response_models import PlayerCareerTraditionalStats
from collector.clients.nba.NbaApi import NbaApi
from nba_api.stats.static import players

import pandas as pd

class Player(NbaApi):

    def __init__(self):
        self._all_players = players.get_players()

    def get_player_info(self, name: str) -> list[dict]:
        return [p for p in self._all_players if p["full_name"] == name]

    def get_active_players(self):
        return [p for p in self._all_players if p["is_active"]]

    def get_active_players_traditional_career_stats(
            self,
            params: dict
    ) -> PlayerCareerTraditionalStats:
        active_players = get_active_players()

        all_stats = []

        for idx, player in enumerate(active_players):
            player_id, player_name = player["id"], player["full_name"]

            try:
                career = playercareerstats.PlayerCareerStats(
                    player_id = player_id,
                    per_mode36 = params["per_mode36"],
                    timeout=60
                )

                df = career.season_totals_regular_season.get_data_frame()

                if not df.empty:
                    df["PLAYER_NAME"] = player_name
                    all_stats.append(df)

                print(f"[{idx}/{len(active_players)}] Retrieved {player_name}")
            except Exception as exc:
                (print(f"Failed for {player_name} ({player_id}): {exc}"))

            break
            time.sleep(5)

        if not all_stats: return pd.DataFrame()

        all_stats = pd.concat(all_stats, ignore_index=True)

        stats = [
            PlayerCareerTraditionalStats.model_validate(row)
            for row in all_stats.to_dict(orient="records")
        ]

        return stats
