from collector.clients.nba.NbaApi import NbaApi
from nba_api.stats.static import players

class Player(NbaApi):

    def __init__(self):
        self._all_players = players.get_players()

    def get_player_info(self, name: str):
        return [p for p in self._all_players if p["full_name"] == name]

