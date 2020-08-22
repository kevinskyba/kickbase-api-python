from datetime import datetime

from kickbase_api.models._transforms import parse_date
from kickbase_api.models.base_model import BaseModel


class MarketPlayerOffer(BaseModel):
    id: str = None
    price: int = None
    date: datetime = None
    valid_until_date: datetime = None

    def __init__(self, d: dict = {}):
        self._json_transform = {
            "date": parse_date,
            "validUntilDate": parse_date
        }
        self._json_mapping = {
            "validUntilDate": "valid_until_date"
        }
        super().__init__(d)
