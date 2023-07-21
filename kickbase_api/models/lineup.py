from kickbase_api.models.base_model import BaseModel

from typing import List


class LineUp(BaseModel):
    type: str = None
    players: List[str] = None

    def __init__(self, d: dict = {}):
        self._json_transform = {
        }
        self._json_mapping = {
        }
        super().__init__(d)
