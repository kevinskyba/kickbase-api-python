from datetime import datetime

from kickbase_api.models._transforms import parse_date
from kickbase_api.models.base_model import BaseModel


class FeedItemComment(BaseModel):
    comment: str = None
    date: datetime = None
    user_id: str = None
    user_name: str = None
    user_profile_path: str = None

    def __init__(self, d: dict):
        self._json_transform = {
            "date": parse_date
        }
        self._json_mapping = {
            "userId": "user_id",
            "userName": "user_name",
            "userProfileUrl": "user_profile_path",
        }
        super().__init__(d)
