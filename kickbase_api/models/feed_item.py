from datetime import datetime
from enum import Enum

from kickbase_api.models._transforms import parse_date
from kickbase_api.models.base_model import BaseModel
from kickbase_api.models.feed_meta import FeedMeta


class FeedType(Enum):
    BUY = 12
    FEED_AD_BANNER = 15
    FEED_COMMENT = 14
    MATCH_DAY_SUMMARY = 8
    NEWS = 1
    NEW_PLAYER_ON_TM = 3
    PLAYER_MATCH_DAY_SUMMARY = 10
    SALE = 2
    STATUS_MESSAGE = 9
    TYPE_EMPTY = 20
    USER_FOUNDED_LEAGUE = 6
    USER_INVITED_OTHER_TO_LEAGUE = 7
    USER_JOINED_LEAGUE = 5
    USER_LEFT_LEAGUE = 13
    USER_MATCH_DAY_SUMMARY = 11
    UNKNOWN = 9999999999


def _map_feed_type(v):
    try:
        return FeedType(v)
    except:
        return FeedType.UNKNOWN


class FeedItem(BaseModel):
    id: str = None
    comments: int = None
    date: datetime = None
    age: int = None
    type: FeedType = None
    source: int = None
    meta: FeedMeta = None
    season_id: int = None

    def __init__(self, d: dict):
        self._json_transform = {
            "date": parse_date,
            "meta": FeedMeta,
            "type": _map_feed_type
        }
        self._json_mapping = {
            "seasonId": "season_id"
        }
        super().__init__(d)
