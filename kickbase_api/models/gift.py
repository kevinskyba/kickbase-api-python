from kickbase_api.models.base_model import BaseModel


class Gift(BaseModel):
    is_available: bool = None
    amount: int = None
    level: int = None
    
    def __init__(self, d: dict = {}):
        self._json_mapping = {
            "isAvailable": "is_available"
        }
        super().__init__(d)
