from enum import IntEnum

from kickbase_api.models.base_model import BaseModel


class PlayerStatus(IntEnum):
    NONE = 0
    INJURED = 1
    STRICKEN = 2
    REHAB = 4
    RED_CARD = 8
    YELLOW_RED_CARD = 16
    FIFTH_YELLOW_CARD = 32
    NOT_IN_TEAM = 64
    NOT_IN_LEAGUE = 128
    ABSENT = 256
    UNKNOWN = 9999999999


def _map_player_status(v):
    try:
        return PlayerStatus(v)
    except:
        return PlayerStatus.UNKNOWN


class PlayerPosition(IntEnum):
    GOAL_KEEPER = 1
    DEFENDER = 2
    MIDFIELDER = 3
    FORWARD = 4
    UNKNOWN = 9999999999


def _map_player_position(v):
    try:
        return PlayerPosition(v)
    except:
        return PlayerPosition.UNKNOWN
    
    
class Player(BaseModel):
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

    def __init__(self, d: dict = {}):
        self._json_transform = {
            "position": _map_player_position,
            "status": _map_player_status
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
            "userId": "user_id"
        }
        super().__init__(d)
