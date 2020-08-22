from kickbase_api.models.base_model import BaseModel


class LeagueMatchDayStatsData(BaseModel):
    user_id: str = None
    day_earnings: float = None
    day_points: int = None
    day_placement: int = None
    day_tendency: int = None
    team_value: int = None
    points: int = None
    placement: int = None
    tendency: int = None
    flags: int = None
    
    def __init__(self, d: dict = {}):
        self._json_transform = {
        }
        self._json_mapping = {
            "dayEarnings": "day_earnings",
            "dayPoints": "day_points",
            "dayPlacement": "day_placement",
            "dayTendency": "day_tendency",
            "teamValue": "team_value"
        }
        
        super().__init__(d)
