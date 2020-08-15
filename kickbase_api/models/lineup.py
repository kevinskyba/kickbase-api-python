from kickbase_api.models.base_model import BaseModel


class LineUp(BaseModel):
    type: str = None
    players: [str] = None

    def __init__(self, d: dict):
        self._json_transform = {
        }
        self._json_mapping = {
        }
        super().__init__(d)
