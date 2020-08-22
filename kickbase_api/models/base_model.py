class BaseModel:
    _json_mapping = {
    }

    _json_transform = {
    }

    def __init__(self, d: dict = {}):
        for key in d.keys():
            value = d[key]

            # Transform if necessary
            if key in self._json_transform:
                value = self._json_transform[key](value)

            if key in self._json_mapping.keys():
                setattr(self, self._json_mapping[key], value)
            setattr(self, key, value)
