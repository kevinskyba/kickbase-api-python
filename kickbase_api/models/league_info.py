from kickbase_api.models.base_model import BaseModel


class LeagueInfo(BaseModel):
    activity_index: float = None
    total_transfers: int = None
    active_users: int = None
    max_users: int = None
    average_points: int = None
    
    rs: int = None
    us: int = None

    def __init__(self, d: dict):
        self._json_transform = {
        }
        self._json_mapping = {
            "ai": "activity_index",
            "t": "total_transfers",
            "au": "active_users",
            "mu": "max_users",
            "ap": "average_points"
        }
        
        super().__init__(d)
