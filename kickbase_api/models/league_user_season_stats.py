from datetime import datetime

from kickbase_api.models._transforms import parse_date, parse_key_value_array_to_dict
from kickbase_api.models.base_model import BaseModel


class LeagueUserSeasonStats(BaseModel):
    season_id: str = None
    season: str = None
    
    points: int = None
    average_points: int = None
    max_points: int = None
    min_points: int = None
    
    wins: int = None
    bought: int = None
    sold: int = None
    
    points_goal_keeper: int = None
    points_defenders: int = None
    points_mid_fielers: int = None
    points_forwards: int = None
    
    average_goal_keeper: int = None
    average_defenders: int = None
    average_mid_fielders: int = None
    average_forwards: int = None
    
    def __init__(self, d: dict = {}):
        self._json_transform = {
        }
        self._json_mapping = {
            "seasonId": "season_id",
            "averagePoints": "average_points",
            "maxPoints": "max_points",
            "minPoints": "min_points",
            "pointsGoalKeeper": "points_goal_keeper",
            "pointsDefenders": "points_defenders",
            "pointsMidFielders": "points_mid_fielers",
            "pointsForwards": "points_forwards",
            "averageGoalKeeper": "average_goal_keeper",
            "averageDefenders": "average_defenders",
            "averageMidFielders": "average_mid_fielders",
            "averageForwards": "average_forwards"
        }
        
        super().__init__(d)
