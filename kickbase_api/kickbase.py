from datetime import datetime, timedelta
from typing import Union

import requests
import json

from kickbase_api.exceptions import KickbaseLoginException, KickbaseException
from kickbase_api.models._transforms import parse_date
from kickbase_api.models.feed_item import FeedItem
from kickbase_api.models.feed_item_comment import FeedItemComment
from kickbase_api.models.league_data import LeagueData
from kickbase_api.models.league_info import LeagueInfo
from kickbase_api.models.league_me import LeagueMe
from kickbase_api.models.league_user_data import LeagueUserData
from kickbase_api.models.league_user_profile import LeagueUserProfile
from kickbase_api.models.league_user_stats import LeagueUserStats
from kickbase_api.models.lineup import LineUp
from kickbase_api.models.market import Market
from kickbase_api.models.market_player import MarketPlayer
from kickbase_api.models.player import Player
from kickbase_api.models.response.league_stats_response import LeagueStatsResponse
from kickbase_api.models.user import User


class Kickbase:
    base_url: str = None
    token: str = None
    token_expire: datetime = None

    _username: str = None
    _password: str = None

    def __init__(self, base_url: str = 'https://api.kickbase.com'):
        self.base_url = base_url

    def login(self, username: str, password: str) -> (User, [LeagueData]):
        data = {
            "email": username,
            "password": password,
            "ext": False
        }

        r = self._do_post("/user/login", data, False)

        if r.status_code == 200:
            j = r.json()
            self.token = j["token"]
            self.token_expire = parse_date(j["tokenExp"])

            self._username = username
            self._password = password

            user = User(j["user"])
            league_data = [LeagueData(d) for d in j["leagues"]]
            return user, league_data

        elif r.status_code == 401:
            raise KickbaseLoginException()
        else:
            raise KickbaseException()

    def _is_token_valid(self):
        if self.token is None or self.token_expire is None:
            return False
        return self.token_expire > datetime.now() - timedelta(days=1)

    def leagues(self) -> [LeagueData]:
        r =  self._do_get("/leagues/", True)

        if r.status_code == 200:
            j = r.json()
            return [LeagueData(d) for d in j["leagues"]]
        else:
            raise KickbaseException()

    def league_me(self, league: Union[str, LeagueData]) -> LeagueMe:
        league_id = self._get_league_id(league)

        r = self._do_get("/leagues/{}/me".format(league_id), True)

        if r.status_code == 200:
            return LeagueMe(r.json())
        else:
            raise KickbaseException()

    def league_info(self, league: Union[str, LeagueData]) -> LeagueInfo:
        league_id = self._get_league_id(league)

        r = self._do_get("/leagues/{}/info".format(league_id), True)

        if r.status_code == 200:
            return LeagueInfo(r.json())
        else:
            raise KickbaseException()

    def league_stats(self, league: Union[str, LeagueData]) -> LeagueStatsResponse:
        league_id = self._get_league_id(league)
        
        r = self._do_get("/leagues/{}/stats".format(league_id), True)

        if r.status_code == 200:
            return LeagueStatsResponse(r.json())
        else:
            raise KickbaseException()

    def league_users(self, league: Union[str, LeagueData]) -> [LeagueUserData]:
        league_id = self._get_league_id(league)

        r = self._do_get("/leagues/{}/users".format(league_id), True)

        if r.status_code == 200:
            return [LeagueUserData(d) for d in r.json()["users"]]
        else:
            raise KickbaseException()

    def league_user_stats(self, league: Union[str, LeagueData], user: Union[str, User]) -> LeagueUserStats:
        league_id = self._get_league_id(league)
        user_id = self._get_user_id(user)

        r = self._do_get("/leagues/{}/users/{}/stats".format(league_id, user_id), True)

        if r.status_code == 200:
            return LeagueUserStats(r.json())
        else:
            raise KickbaseException()

    def league_user_profile(self, league: Union[str, LeagueData], user: Union[str, User]) -> LeagueUserProfile:
        league_id = self._get_league_id(league)
        user_id = self._get_user_id(user)
        
        r = self._do_get("/leagues/{}/users/{}/profile".format(league_id, user_id), True)

        if r.status_code == 200:
            return LeagueUserProfile(r.json())
        else:
            raise KickbaseException()

    def league_feed(self, start_index: int, league: Union[str, LeagueData]) -> [FeedItem]:
        league_id = self._get_league_id(league)

        r = self._do_get("/leagues/{}/feed?start={}".format(league_id, start_index), True)

        if r.status_code == 200:
            return [FeedItem(v) for v in r.json()["items"]]
        else:
            raise KickbaseException()

    def post_feed_item(self, comment: str, league: Union[str, LeagueData]):
        league_id = self._get_league_id(league)

        data = {
            "comment": comment
        }

        r = self._do_post("/leagues/{}/feed".format(league_id), data, True)

        if r.status_code == 200:
            return
        else:
            raise KickbaseException()

    def league_feed_comments(self, league: Union[str, LeagueData], feed_item: Union[str, FeedItem]) -> [FeedItemComment]:
        league_id = self._get_league_id(league)
        feed_item_id = self._get_feed_item_id(feed_item)

        r = self._do_get("/leagues/{}/feed/{}/comments".format(league_id, feed_item_id), True)

        if r.status_code == 200:
            return [FeedItemComment(v) for v in r.json()["comments"]]
        else:
            raise KickbaseException()

    def post_feed_comment(self, comment: str, league: Union[str, LeagueData], feed_item: Union[str, FeedItem]):
        league_id = self._get_league_id(league)
        feed_item_id = self._get_feed_item_id(feed_item)

        data = {
            "comment": comment
        }

        r = self._do_post("/leagues/{}/feed/{}/comments".format(league_id, feed_item_id), data, True)

        if r.status_code == 200:
            return
        else:
            raise KickbaseException()

    def league_user_players(self, league: Union[str, LeagueData], user: Union[str, User], match_day: int = 0) -> [
        Player]:
        league_id = self._get_league_id(league)
        user_id = self._get_user_id(user)

        r = self._do_get("/leagues/{}/users/{}/players?matchDay={}".format(league_id, user_id, match_day), True)

        if r.status_code == 200:
            return [Player(v) for v in r.json()["players"]]
        else:
            raise KickbaseException()

    def search_player(self, search_query: str) -> [Player]:
        r = self._do_get("/competition/search?t={}".format(search_query))

        if r.status_code == 200:
            return [Player(v) for v in r.json()["p"]]
        else:
            raise KickbaseException()

    def team_players(self, team_id: str) -> [Player]:
        r = self._do_get("/competition/teams/{}/players".format(team_id))

        if r.status_code == 200:
            return [Player(v) for v in r.json()["p"]]
        else:
            raise KickbaseException()

    def top_25_players(self) -> [Player]:
        r = self._do_get("/competition/best?position=0")

        if r.status_code == 200:
            return [Player(v) for v in r.json()["p"]]
        else:
            raise KickbaseException()

    def line_up(self, league: Union[str, LeagueData]) -> LineUp:
        league_id = self._get_league_id(league)

        r = self._do_get("/leagues/{}/lineup".format(league_id), True)

        if r.status_code == 200:
            return LineUp(r.json())
        else:
            raise KickbaseException()

    def set_line_up(self, line_up: LineUp, league: Union[str, LeagueData]) -> LineUp:
        league_id = self._get_league_id(league)

        if not self._is_token_valid:
            self.login(self._username, self._password)

        data = {
            "type": line_up.type,
            "players": line_up.players
        }

        r = self._do_post("/leagues/{}/lineup".format(league_id), data, True)

        if r.status_code == 200:
            return LineUp(r.json())
        else:
            raise KickbaseException()

    def market(self, league: Union[str, LeagueData]) -> Market:
        league_id = self._get_league_id(league)

        r = self._do_get("/leagues/{}/market".format(league_id), True)

        if r.status_code == 200:
            return Market(r.json())
        else:
            raise KickbaseException()

    def add_to_market(self, price: int, player: Union[str, Player, MarketPlayer], league: Union[str, LeagueData]):
        player_id = self._get_player_id(player)
        league_id = self._get_league_id(league)

        data = {
            "playerId": player_id,
            "price": price
        }

        r = self._do_post("/leagues/{}/market".format(league_id), data, True)

        if r.status_code == 200:
            return
        else:
            raise KickbaseException()

    def remove_from_market(self, player: Union[str, Player, MarketPlayer], league: Union[str, LeagueData]):
        player_id = self._get_player_id(player)
        league_id = self._get_league_id(league)

        r = self._do_delete("/leagues/{}/market/{}".format(league_id, player_id), True)

        if r.status_code == 200:
            return
        else:
            raise KickbaseException()

    def update_price(self, price: int, player: Union[str, Player, MarketPlayer], league: Union[str, LeagueData]):
        player_id = self._get_player_id(player)
        league_id = self._get_league_id(league)

        data = {
            "price": price
        }

        r = self._do_put("/leagues/{}/market/{}".format(league_id, player_id), data, True)

        if r.status_code == 200:
            return
        else:
            raise KickbaseException()

    def make_offer(self, price: int, player: Union[str, Player, MarketPlayer], league: Union[str, LeagueData]):
        player_id = self._get_player_id(player)
        league_id = self._get_league_id(league)

        data = {
            "price": price
        }

        r = self._do_post("/leagues/{}/market/{}/offers".format(league_id, player_id), data, True)

        if r.status_code == 200:
            return
        else:
            raise KickbaseException()

    def remove_offer(self, offer_id: str, player: Union[str, Player, MarketPlayer], league: Union[str, LeagueData]):
        player_id = self._get_player_id(player)
        league_id = self._get_league_id(league)

        r = self._do_delete("/leagues/{}/market/{}/offers/{}".format(league_id, player_id, offer_id), True)

        if r.status_code == 200:
            return
        else:
            raise KickbaseException()

    def accept_offer(self, offer_id: str, player: Union[str, Player, MarketPlayer], league: Union[str, LeagueData]):
        player_id = self._get_player_id(player)
        league_id = self._get_league_id(league)

        r = self._do_post("/leagues/{}/market/{}/offers/{}/accept".format(league_id, player_id, offer_id), {}, True)

        if r.status_code == 200:
            return
        else:
            raise KickbaseException()

    def decline_offer(self, offer_id: str, player: Union[str, Player, MarketPlayer], league: Union[str, LeagueData]):
        player_id = self._get_player_id(player)
        league_id = self._get_league_id(league)

        r = self._do_post("/leagues/{}/market/{}/offers/{}/decline".format(league_id, player_id, offer_id), {}, True)

        if r.status_code == 200:
            return
        else:
            raise KickbaseException()

    def _get_league_id(self, league: any):
        if isinstance(league, str):
            return league
        if isinstance(league, LeagueData):
            return league.id
        raise KickbaseException("league must be either type of str or LeagueData")

    def _get_player_id(self, player: any):
        if isinstance(player, str):
            return player
        if isinstance(player, Player):
            return player.id
        if isinstance(player, MarketPlayer):
            return player.id
        raise KickbaseException("player must be either type of str, Player or MarketPlayer")

    def _get_user_id(self, user: any):
        if isinstance(user, str):
            return user
        if isinstance(user, User):
            return user.id
        raise KickbaseException("user must be either type of str or User")
    
    def _get_feed_item_id(self, feed_item: any):
        if isinstance(feed_item, str):
            return feed_item
        if isinstance(feed_item, FeedItem):
            return feed_item.id
        raise KickbaseException("feed_item must be either type of str or FeedItem")

    def _url_for_endpoint(self, endpoint: str):
        return self.base_url + endpoint

    def _auth_cookie(self):
        return "kkstrauth={}".format(self.token)

    def _do_get(self, endpoint: str, authenticated: bool = False):
        if not self._is_token_valid:
            self.login(self._username, self._password)

        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        if authenticated:
            headers["Cookie"] = self._auth_cookie()

        return requests.get(self._url_for_endpoint(endpoint), headers=headers)

    def _do_post(self, endpoint: str, data: dict, authenticated: bool = False):
        if not self._is_token_valid:
            self.login(self._username, self._password)

        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        if authenticated:
            headers["Cookie"] = self._auth_cookie()

        return requests.post(self._url_for_endpoint(endpoint), data=json.dumps(data), headers=headers)

    def _do_put(self, endpoint: str, data: dict, authenticated: bool = False):
        if not self._is_token_valid:
            self.login(self._username, self._password)

        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        if authenticated:
            headers["Cookie"] = self._auth_cookie()

        return requests.put(self._url_for_endpoint(endpoint), data=json.dumps(data), headers=headers)

    def _do_delete(self, endpoint: str, authenticated: bool = False):
        if not self._is_token_valid:
            self.login(self._username, self._password)

        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        if authenticated:
            headers["Cookie"] = self._auth_cookie()

        return requests.delete(self._url_for_endpoint(endpoint), headers=headers)
