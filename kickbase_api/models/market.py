from datetime import datetime
from enum import Enum

from kickbase_api.models._transforms import parse_date
from kickbase_api.models.base_model import BaseModel
from kickbase_api.models.feed_meta import FeedMeta
from kickbase_api.models.market_player import MarketPlayer
from kickbase_api.models.market_player_offer import MarketPlayerOffer
from kickbase_api.models.player import Player, _map_player_position, _map_player_status, PlayerPosition, PlayerStatus


class Market(BaseModel):
    closed: bool = None
    players: [MarketPlayer] = None
    
    def __init__(self, d: dict):
        self._json_transform = {
            "players": lambda v: [MarketPlayer(v_) for v_ in v]
        }
        self._json_mapping = {
            "c": "closed"
        }
        super().__init__(d)