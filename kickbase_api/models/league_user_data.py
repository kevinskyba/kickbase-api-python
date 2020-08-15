from datetime import datetime

from kickbase_api.models._transforms import parse_date
from kickbase_api.models.base_model import BaseModel


class LeagueUserData(BaseModel):
    id: str = None
    email: str = None
    name: str = None
    profile_image_path: str = None
    cover_image_path: str = None
    status: int = None
    perms: [int] = None
    
    def __init__(self, d: dict):
        self._json_transform = {
        }
        self._json_mapping = {
            "profile": "profile_image_path",
            "cover": "cover_image_path"
        }
        
        super().__init__(d)
