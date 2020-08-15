from kickbase_api.models.base_model import BaseModel


class User(BaseModel):
    id: str = None
    email: str = None
    name: str = None
    notifications: int = None
    profile_image_path: str = None
    
    def __init__(self, d: dict):
        self._json_mapping = {
            "profile": "profile_image_path"
        }
        super().__init__(d)
