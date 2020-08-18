from datetime import datetime

from kickbase_api.models._transforms import parse_date


class ChatItem:
    id: str = None
    league_id: str = None
    message: str = None
    date: datetime = None
    user_id: str = None
    username: str = None
    seen_by: [str] = []

    def __init__(self, d: dict):
        if "name" in d:
            self.id = d["name"]
        if "fields" in d:
            fields = d["fields"]
            if "leagueId" in fields:
                self.league_id = fields["leagueId"]["stringValue"]
            if "message" in fields:
                self.message = fields["message"]["stringValue"]
            if "date" in fields:
                self.date = parse_date(fields["date"]["stringValue"])
            if "userId" in fields:
                self.user_id = fields["userId"]["stringValue"]
            if "username" in fields:
                self.username = fields["username"]["stringValue"]
            if "seenBy" in fields:
                array = fields["seenBy"]["arrayValue"]["values"]
                for ar in array:
                    self.seen_by.append(ar["stringValue"])
