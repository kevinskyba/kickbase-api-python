from datetime import datetime

from kickbase_api.models._transforms import parse_date, parse_key_value_array_to_dict
from kickbase_api.models.base_model import BaseModel
from kickbase_api.models.league_user_season_stats import LeagueUserSeasonStats


class LeagueUserStats(BaseModel):
    name: str = None
    profile_image_path: str = None
    cover_image_path: str = None
    flags: int = None
    placement: int = None
    points: int = None
    team_value: float = None
    
    seasons: [LeagueUserSeasonStats] = None
    team_values: {datetime: float}
    
    def __init__(self, d: dict):
        self._json_transform = {
            "teamValues": parse_key_value_array_to_dict(lambda o: parse_date(o["d"]), lambda o: o["v"]),
            "seasons": lambda v: [LeagueUserSeasonStats(_d) for _d in v]
        }
        self._json_mapping = {
            "profileUrl": "profile_image_path",
            "coverUrl": "cover_image_path",
            "teamValue": "team_value",
            "teamValues": "team_values"
        }
        
        super().__init__(d)
