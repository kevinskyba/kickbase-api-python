from datetime import datetime

from kickbase_api.models._transforms import parse_date, parse_key_value_array_to_dict
from kickbase_api.models.base_model import BaseModel
from kickbase_api.models.league_match_day_user_stats import LeagueMatchDayUserStats


class LeagueUserProfileSeasonStats(BaseModel):
    season_id: str = None
    season: str = None
    
    points: int = None
    average_points: int = None
    max_points: int = None    
    wins: int = None
    
    match_days: [LeagueMatchDayUserStats] = None
   
    def __init__(self, d: dict = {}):
        self._json_transform = {
            "matchDays": lambda v: [LeagueMatchDayUserStats(_d) for _d in v]
        }
        self._json_mapping = {
            "seasonId": "season_id",
            "averagePoints": "average_points",
            "maxPoints": "max_points",
            "matchDays": "match_days"
        }
        
        super().__init__(d)
