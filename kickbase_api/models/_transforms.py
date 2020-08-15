from array import array
from datetime import datetime
from typing import Callable


def parse_date(s: str) -> datetime:
    return datetime.strptime(s, "%Y-%m-%dT%H:%M:%SZ")


def parse_key_value_array_to_dict(key: Callable[[array], any], value: Callable[[array], any]):
    def _int(a: []) -> dict: 
        ret = {}
        for v in a:
            ret[key(v)] = value(v)
        return ret
    return _int
