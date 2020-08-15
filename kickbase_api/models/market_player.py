from datetime import datetime
from enum import Enum

from kickbase_api.models._transforms import parse_date
from kickbase_api.models.base_model import BaseModel
from kickbase_api.models.feed_meta import FeedMeta
from kickbase_api.models.market_player_offer import MarketPlayerOffer
from kickbase_api.models.player import Player, _map_player_position, _map_player_status, PlayerPosition, PlayerStatus


class MarketPlayer(BaseModel):
    id: str = None
    first_name: str = None
    last_name: str = None
    average_points: int = None
    totalPoints: int = None
    market_value: int = None
    market_value_trend: int = None
    number: int = None
    position: PlayerPosition = None
    status: PlayerStatus = None
    team_id: str = None
    user_id: str = None

    profile_path: str = None
    profile_big_path: str = None
    team_path: str = None
    team_cover_path: str = None
    
    username: str = None
    user_profile_path: str = None
    price: int = None
    date: datetime = None
    expiry: int = None
    lus: int = None
    
    offers: [MarketPlayerOffer] = None
    
    def __init__(self, d: dict):
        self._json_transform = {
            "position": _map_player_position,
            "status": _map_player_status,
            "date": parse_date,
            "offers": lambda v: [MarketPlayerOffer(v_) for v_ in v]
        }
        self._json_mapping = {
            "firstName": "first_name",
            "lastName": "last_name",
            "averagePoints": "average_points",
            "marketValue": "market_value",
            "marketValueTrend": "market_value_trend",
            "teamId": "team_id",
            "profile": "profile_path",
            "profileBig": "profile_big_path",
            "team": "team_path",
            "teamCover": "team_cover_path",
            "userId": "user_id",
            
            "userProfile": "user_profile_path",
        }
        super().__init__(d)