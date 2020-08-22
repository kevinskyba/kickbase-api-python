from datetime import datetime

from kickbase_api.models._transforms import parse_date, parse_key_value_array_to_dict
from kickbase_api.models.base_model import BaseModel
from kickbase_api.models.league_user_profile_season_stats import LeagueUserProfileSeasonStats


class LeagueUserProfile(BaseModel):
    flags: int = None
    perms: [int] = None
    level_achieved: int = None
    current_season_id: int = None
    placement: int = None
    
    points_gk: int = None
    points_def: int = None
    points_mf: int = None
    points_fwd: int = None
    
    team_value: float = None
    bought: int = None
    sold: int = None
    highest_team_value: float = None
    
    seasons: [LeagueUserProfileSeasonStats] = None
    team_values: {datetime: float}
    
    def __init__(self, d: dict = {}):
        self._json_transform = {
            "teamValues": parse_key_value_array_to_dict(lambda o: parse_date(o["d"]), lambda o: o["v"]),
            "seasons": lambda v: [LeagueUserProfileSeasonStats(_d) for _d in v]
        }
        self._json_mapping = {
            "levelAchieved": "level_achieved",
            "currentSeasonId": "current_season_id",
            "pointsGK": "points_gk",
            "pointsDEF": "points_def",
            "pointsMF": "points_mf",
            "pointsFWD": "points_fwd",
            "teamValue": "team_value",
            "highestTeamValue": "highest_team_value",
            "teamValues": "team_values"
        }
        
        super().__init__(d)
