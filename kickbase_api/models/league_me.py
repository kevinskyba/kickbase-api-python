from datetime import datetime

from kickbase_api.models._transforms import parse_date
from kickbase_api.models.base_model import BaseModel


class LeagueMe(BaseModel):
    budget: float = None
    team_value: float = None
    placement: int = None
    points: int = None
    ttm: int = None
    cmd: int = None
    flags: int = None
    se: bool = None
    csid: int = None
    nt: bool = None
    ntv: float = None
    nb: float = None
    ga: bool = None
    un: int = None
    
    def __init__(self, d: dict):
        self._json_transform = {
        }
        self._json_mapping = {
            "teamValue": "team_value"
        }
        
        super().__init__(d)
