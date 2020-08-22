from datetime import datetime

from kickbase_api.models._transforms import parse_date, parse_key_value_array_to_dict
from kickbase_api.models.base_model import BaseModel


class LeagueMatchDayUserStats(BaseModel):
    season_id: str = None
    day: int = None
    placement: int = None
    points: int = None
   
    def __init__(self, d: dict = {}):
        self._json_transform = {
        }
        self._json_mapping = {
            "s": "season_id",
            "p": "placement",
            "pt": "points"
        }
        
        super().__init__(d)
