from kickbase_api.models.base_model import BaseModel


class FeedMeta(BaseModel):
    average_points: int = None
    match_day: int = None
    maximum_points: int = None
    total_points: int = None
    
    buyer_picture: str = None
    buyer_id: str = None
    buyer_name: str = None
    buy_price: int = None
    
    seller_picture: str = None
    seller_id: str = None
    seller_name: str = None
    sell_price: int = None
    
    player_id: str = None
    player_first_name: str = None
    player_last_name: str = None
    player_known_name: str = None
    
    c: int = None
    e: int = None
    
    player_summary_r: int = None
    player_summary_y: int = None
    player_summary_yr: int = None
    assists: int = None
    game_time: int = None
    goals_shot: int = None
    match_type: int = None
    team_name: str = None
    opponent_team_id: int = None
    opponent_team_name: str = None
    goals_team_1: int = None
    goals_team_2: int = None
    
    founder_picture_path: str = None
    found_id: str = None
    founder_name: str = None
    league_name: str = None
    league_id: str = None
    
    inviter_profile_picture_path: str = None
    inviter_id: str = None
    inviter_name: str = None
    
    invited_name: str = None
    
    goal_keeper_points: int = None
    defenders_points: int = None
    midfielders_points: int = None
    forwarders_points: int = None
    total_points: int = None
    
    user_id: str = None
    user_name: str = None
    
    user_picture_path: str = None
    status_message: str = None
    
    news: str = None
    
    def __init__(self, d: dict = {}):
        self._json_transform = {
        }
        self._json_mapping = {
            "a": "average_points",
            "day": "match_day",
            "m": "maximum_points",
            "t": "total_points",
            "bi": "buyer_picture",
            "bid": "buyer_id",
            "bn": "buyer_name",
            "p": "buy_price",
            # "p": "sell_price",
            "sn": "seller_name",
            "pid": "player_id",
            "pln": "player_last_name",
            "pkn": "player_known_name",
            "cr": "player_summary_r",
            "cy": "player_summary_y",
            "cyr": "player_summary_yr",
            # "a": "assists",
            # "t": "game_time",
            "g": "goals_shot",
            "h": "match_type",
            "tn": "team_name",
            "oid": "opponent_team_id",
            "otn": "opponent_team_name",
            "r1": "goals_team_1",
            "r2": "goals_team_2",
            "fi": "founder_picture_path",
            "fid": "found_id",
            "fn": "founder_name",
            "ln": "league_name",
            "li": "league_id",
            "ii": "inviter_profile_picture_path",
            "iid": "inviter_id",
            "in": "inviter_name",
            # "tn": "invited_name",
            "pg": "goal_keeper_points",
            "pd": "defenders_points",
            "pm": "midfielders_points",
            "pf": "forwarders_points",
            "pfn": "player_first_name",
            "pt": "total_points",
            "uid": "user_id",
            "un": "user_name",
            "ui": "user_picture_path",
            "s": "status_message",
            "sid": "seller_id",
            "n": "news"
        }
        
        super().__init__(d)
        self.sell_price = self.buy_price
        self.game_time = self.total_points
        self.assists = self.average_points
        self.invited_name = self.team_name
