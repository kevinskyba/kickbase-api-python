from kickbase_api.models.base_model import BaseModel


class PlayerStats(BaseModel):
    market_value_change: int = None
    market_value_change_percent: float = None

    def __init__(self, d: dict = {}):
        self._json_transform = {
        }
        self._json_mapping = {
            "marketValueChange": "market_value_change",
            "marketValueChangePercent": "market_value_change_percent"
        }
        super().__init__(d)
