from kickbase_api.models.base_model import BaseModel
from kickbase_api.models.market_player import MarketPlayer

from typing import List


class Market(BaseModel):
    closed: bool = None
    players: List[MarketPlayer] = None
    
    def __init__(self, d: dict = {}):
        self._json_transform = {
            "players": lambda v: [MarketPlayer(v_) for v_ in v]
        }
        self._json_mapping = {
            "c": "closed"
        }
        super().__init__(d)