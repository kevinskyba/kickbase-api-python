import os

import pytest

from kickbase_api.kickbase import Kickbase

@pytest.mark.online
def test_login():
    kickbase = Kickbase()
    assert not kickbase._is_token_valid()
    user, leagues = kickbase.login(os.environ["KKBS_TEST_USERNAME"], os.environ["KKBS_TEST_PASSWORD"])
    assert kickbase._is_token_valid()
    assert user is not None
    assert leagues is not None
    
    kickbase.post_chat_message("..", leagues[1])


@pytest.mark.online
def test_leagues(logged_in_kickbase):
    kickbase, user, leagues = logged_in_kickbase
    leagues_ = kickbase.leagues()
    assert leagues_ is not None
    assert len(leagues) == len(leagues_)
    
    
@pytest.mark.online
def test_league_me(logged_in_kickbase):
    kickbase, user, leagues = logged_in_kickbase
    league_me = kickbase.league_me(leagues[0])
    assert league_me is not None
    
    
@pytest.mark.online
def test_league_me(logged_in_kickbase):
    kickbase, user, leagues = logged_in_kickbase
    league_info = kickbase.league_me(leagues[0])
    assert league_info is not None
    

@pytest.mark.online
def test_league_stats(logged_in_kickbase):
    kickbase, user, leagues = logged_in_kickbase
    league_stats = kickbase.league_stats(leagues[0])
    assert league_stats is not None
    

@pytest.mark.online
def test_league_users(logged_in_kickbase):
    kickbase, user, leagues = logged_in_kickbase
    league_users = kickbase.league_users(leagues[0])
    assert league_users is not None


@pytest.mark.online
def test_league_user_stats(logged_in_kickbase):
    kickbase, user, leagues = logged_in_kickbase
    league_user_stats = kickbase.league_user_stats(leagues[0], user)
    assert league_user_stats is not None


@pytest.mark.online
def test_league_user_profile(logged_in_kickbase):
    kickbase, user, leagues = logged_in_kickbase
    league_user_profile = kickbase.league_user_profile(leagues[0], user)
    assert league_user_profile is not None


@pytest.mark.online
def test_league_feed(logged_in_kickbase):
    kickbase, user, leagues = logged_in_kickbase
    feed_items = kickbase.league_feed(0, leagues[0])
    assert feed_items is not None
  
  
@pytest.mark.online
def test_league_feed_comments(logged_in_kickbase):
    kickbase, user, leagues = logged_in_kickbase
    feed_items = kickbase.league_feed(0, leagues[0])
    feed_item_comments = kickbase.league_feed_comments(leagues[0], feed_items[0])
    assert feed_item_comments is not None


@pytest.mark.online
def test_league_user_players(logged_in_kickbase):
    kickbase, user, leagues = logged_in_kickbase
    players = kickbase.league_user_players(leagues[0], user)
    assert players is not None


@pytest.mark.online
def test_league_user_player_stats(logged_in_kickbase):
    kickbase, user, leagues = logged_in_kickbase
    stats = kickbase.league_user_player_stats(leagues[0], "44")
    assert stats is not None


@pytest.mark.online
def test_league_user_players_match_day(logged_in_kickbase):
    kickbase, user, leagues = logged_in_kickbase
    players = kickbase.league_user_players(leagues[0], user, 1)
    assert players is not None

@pytest.mark.online
def test_league_user_players_match_day(logged_in_kickbase):
    kickbase, user, leagues = logged_in_kickbase
    gift = kickbase.league_current_gift(leagues[0])
    assert gift is not None

@pytest.mark.online
def test_search_player(logged_in_kickbase):
    kickbase, user, leagues = logged_in_kickbase
    players = kickbase.search_player(search_query="Lewandowski")
    assert players is not None


@pytest.mark.online
def test_search_player(logged_in_kickbase):
    kickbase, user, leagues = logged_in_kickbase
    players = kickbase.team_players(40)
    assert players is not None
    

@pytest.mark.online
def test_top_25_players(logged_in_kickbase):
    kickbase, user, leagues = logged_in_kickbase
    players = kickbase.top_25_players()
    assert players is not None


@pytest.mark.online
def test_line_up(logged_in_kickbase):
    kickbase, user, leagues = logged_in_kickbase
    line_up = kickbase.line_up(leagues[0])
    assert line_up is not None
    

@pytest.mark.online
def test_market(logged_in_kickbase):
    kickbase, user, leagues = logged_in_kickbase
    market = kickbase.market(leagues[0])
    assert market is not None


@pytest.mark.online
def test_chat_messages(logged_in_kickbase):
    kickbase, user, leagues = logged_in_kickbase
    chat_messages, next_page_token = kickbase.chat_messages(leagues[0])
    assert chat_messages is not None