# Kickbase_API
[Kickbase](https://www.kickbase.com/) API for Python 3.  This work is unofficial and not related to kickbase in any way. All of this was done for scientific reasons only and you should not use it for anything else but for your personal learning!

## Installation
- From pypi:
`pip3 install kickbase_api`

## Requirements
- [requests](https://github.com/kennethreitz/requests)

## Usage
```python
from kickbase_api.kickbase import Kickbase
kickbase = Kickbase()
user, leagues = kickbase.login("username", "password")
```

## API
This library is based on [Kickbase API Doc](https://github.com/kevinskyba/kickbase-api-doc).

## License

[MIT License](LICENSE.md)