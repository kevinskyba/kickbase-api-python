from datetime import datetime

from kickbase_api.models._transforms import parse_date
from kickbase_api.models.base_model import BaseModel


class LeagueData(BaseModel):
    id: str = None
    name: str = None
    
    creator: str = None
    creator_id: int = None
    creation_date: datetime = None

    activity_index: float = None
    total_transfers: int = None
    active_users: int = None
    max_users: int = None
    average_points: int = None
    
    pub: bool = None
    gm: int = None
    
    player_limit_active: bool = None
    player_limit: bool = None
    
    image_path: str = None
    
    def __init__(self, d: dict = {}):
        self._json_transform = {
            "creation": parse_date
        }
        self._json_mapping = {
            "creatorId": "creator_id",
            "creation": "creation_date",
            "mpl": "player_limit_active",
            "pl": "player_limit",
            "ci": "image_path",
            "ai": "activity_index",
            "t": "total_transfers",
            "au": "active_users",
            "mu": "max_users",
            "ap": "average_points"
        }
        
        super().__init__(d)
