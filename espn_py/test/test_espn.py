import xml.dom.minidom
import pytest
import sys
sys.path.append("..")

from espn import *


API_KEY = 'vcyenmchrh2ea3b5gqtaybwr'

# Tests for HeadlinesAPI Class
# Tests for each available function within the class that returns JSON data
def test_sports_headlines_json():
	espn_api = HeadlinesAPI(API_KEY, format='json')
	data = espn_api.sports_headlines()
	assert data['status'] == 'success'

def test_city_sites_headlines_json():
	espn_api = HeadlinesAPI(API_KEY, format='json')
	data = espn_api.city_sites_headlines()
	assert data['status'] == 'success'

def test_espnw_headlines_json():
	espn_api = HeadlinesAPI(API_KEY, format='json')
	data = espn_api.espnw_headlines()
	assert data['status'] == 'success'

def test_fantasy_headlines_json():
	espn_api = HeadlinesAPI(API_KEY, format='json')
	data = espn_api.fantasy_headlines()
	assert data['status'] == 'success'

def test_espn_mag_headlines_json():
	espn_api = HeadlinesAPI(API_KEY, format='json')
	data = espn_api.espn_mag_headlines()
	assert data['status'] == 'success'

# Tests for each available function within the class that returns XML data
def test_sports_headlines_xml():
	espn_api = HeadlinesAPI(API_KEY, format='xml')
	data = espn_api.sports_headlines()
	status = data.getElementsByTagName('status')
	assert status[0].firstChild.nodeValue == 'success'

def test_city_sites_headlines_xml():
	espn_api = HeadlinesAPI(API_KEY, format='xml')
	data = espn_api.city_sites_headlines()
	status = data.getElementsByTagName('status')
	assert status[0].firstChild.nodeValue == 'success'

def test_espnw_headlines_xml():
	espn_api = HeadlinesAPI(API_KEY, format='xml')
	data = espn_api.espnw_headlines()
	status = data.getElementsByTagName('status')
	assert status[0].firstChild.nodeValue == 'success'

def test_fantasy_headlines_xml():
	espn_api = HeadlinesAPI(API_KEY, format='xml')
	data = espn_api.fantasy_headlines()
	status = data.getElementsByTagName('status')
	assert status[0].firstChild.nodeValue == 'success'

def test_espn_mag_headlines_xml():
	espn_api = HeadlinesAPI(API_KEY, format='xml')
	data = espn_api.espn_mag_headlines()
	status = data.getElementsByTagName('status')
	assert status[0].firstChild.nodeValue == 'success'


# Tests for AthletesAPI Class
# Tests for each available function within the class that returns JSON data
def test_baseball_athletes_json():
	espn_api = AthletesAPI(API_KEY, format='json')
	data = espn_api.baseball_athletes()
	assert data['status'] == 'success'

def test_mlb_athletes_json():
	espn_api = AthletesAPI(API_KEY, format='json')
	data = espn_api.mlb_athletes()
	assert data['status'] == 'success'

# This test will need to be updated once requested data is supported by ESPN
def test_mens_colg_baseball_athletes_json():
	with pytest.raises(Exception):
		espn_api = AthletesAPI(API_KEY, format='json')
		data = espn_api.mens_colg_baseball_athletes()

def test_basketball_athletes_json():
	espn_api = AthletesAPI(API_KEY, format='json')
	data = espn_api.basketball_athletes()
	assert data['status'] == 'success'

def test_nba_athletes_json():
	espn_api = AthletesAPI(API_KEY, format='json')
	data = espn_api.nba_athletes()
	assert data['status'] == 'success'

def test_wnba_athletes_json():
	espn_api = AthletesAPI(API_KEY, format='json')
	data = espn_api.wnba_athletes()
	assert data['status'] == 'success'

def test_mens_colg_basketball_athletes_json():
	espn_api = AthletesAPI(API_KEY, format='json')
	data = espn_api.mens_colg_basketball_athletes()
	assert data['status'] == 'success'

def test_womens_colg_basketball_athletes_json():
	espn_api = AthletesAPI(API_KEY, format='json')
	data = espn_api.womens_colg_basketball_athletes()
	assert data['status'] == 'success'

def test_football_athletes_json():
	espn_api = AthletesAPI(API_KEY, format='json')
	data = espn_api.football_athletes()
	assert data['status'] == 'success'

def test_nfl_athletes_json():
	espn_api = AthletesAPI(API_KEY, format='json')
	data = espn_api.nfl_athletes()
	assert data['status'] == 'success'

def test_colg_football_athletes_json():
	espn_api = AthletesAPI(API_KEY, format='json')
	data = espn_api.colg_football_athletes()
	assert data['status'] == 'success'

def test_hockey_athletes_json():
	espn_api = AthletesAPI(API_KEY, format='json')
	data = espn_api.hockey_athletes()
	assert data['status'] == 'success'

def test_nhl_athletes_json():
	espn_api = AthletesAPI(API_KEY, format='json')
	data = espn_api.nhl_athletes()
	assert data['status'] == 'success'

# This test will need to be updated once requested data is supported by ESPN
def test_mens_colg_hockey_athletes_json():
	with pytest.raises(Exception):
		espn_api = AthletesAPI(API_KEY, format='json')
		data = espn_api.mens_colg_hockey_athletes()

# This test will need to be updated once requested data is supported by ESPN
def test_womens_colg_hockey_athletes_json():
	with pytest.raises(Exception):
		espn_api = AthletesAPI(API_KEY, format='json')
		data = espn_api.womens_colg_hockey_athletes()

def test_golf_athletes_json():
	espn_api = AthletesAPI(API_KEY, format='json')
	data = espn_api.golf_athletes()
	assert data['status'] == 'success'

def test_euro_tour_golf_athletes_json():
	espn_api = AthletesAPI(API_KEY, format='json')
	data = espn_api.euro_tour_golf_athletes()
	assert data['status'] == 'success'

# This test will need to be updated once requested data is supported by ESPN
def test_lpga_golf_athletes_json():
	with pytest.raises(Exception):
		espn_api = AthletesAPI(API_KEY, format='json')
		data = espn_api.lpga_golf_athletes()

def test_pga_golf_athletes_json():
	espn_api = AthletesAPI(API_KEY, format='json')
	data = espn_api.pga_golf_athletes()
	assert data['status'] == 'success'

def test_sga_golf_athletes_json():
	espn_api = AthletesAPI(API_KEY, format='json')
	data = espn_api.sga_golf_athletes()
	assert data['status'] == 'success'

def test_racing_athletes_json():
	espn_api = AthletesAPI(API_KEY, format='json')
	data = espn_api.racing_athletes()
	assert data['status'] == 'success'

def test_indycar_athletes_json():
	espn_api = AthletesAPI(API_KEY, format='json')
	data = espn_api.indycar_athletes()
	assert data['status'] == 'success'

def test_sprint_cup_athletes_json():
	espn_api = AthletesAPI(API_KEY, format='json')
	data = espn_api.sprint_cup_athletes()
	assert data['status'] == 'success'

def test_nationwide_athletes_json():
	espn_api = AthletesAPI(API_KEY, format='json')
	data = espn_api.nationwide_athletes()
	assert data['status'] == 'success'

def test_camping_world_truck_athletes_json():
	espn_api = AthletesAPI(API_KEY, format='json')
	data = espn_api.camping_world_truck_athletes()
	assert data['status'] == 'success'

def test_f1_athletes_json():
	espn_api = AthletesAPI(API_KEY, format='json')
	data = espn_api.f1_athletes()
	assert data['status'] == 'success'

def test_soccer_athletes_json():
	espn_api = AthletesAPI(API_KEY, format='json')
	data = espn_api.soccer_athletes()
	assert data['status'] == 'success'

def test_mls_athletes_json():
	espn_api = AthletesAPI(API_KEY, format='json')
	data = espn_api.mls_athletes()
	assert data['status'] == 'success'

def test_la_liga_athletes_json():
	espn_api = AthletesAPI(API_KEY, format='json')
	data = espn_api.la_liga_athletes()
	assert data['status'] == 'success'

def test_premier_league_athletes_json():
	espn_api = AthletesAPI(API_KEY, format='json')
	data = espn_api.premier_league_athletes()
	assert data['status'] == 'success'

def test_tennis_athletes_json():
	espn_api = AthletesAPI(API_KEY, format='json')
	data = espn_api.tennis_athletes()
	assert data['status'] == 'success'

def test_atp_athletes_json():
	espn_api = AthletesAPI(API_KEY, format='json')
	data = espn_api.atp_athletes()
	assert data['status'] == 'success'

def test_wta_athletes_json():
	espn_api = AthletesAPI(API_KEY, format='json')
	data = espn_api.wta_athletes()
	assert data['status'] == 'success'

# Tests for each available function within the class that returns XML data
def test_baseball_athletes_xml():
	espn_api = AthletesAPI(API_KEY, format='xml')
	data = espn_api.baseball_athletes()
	status = data.getElementsByTagName('status')
	assert status[0].firstChild.nodeValue == 'success'

def test_mlb_athletes_xml():
	espn_api = AthletesAPI(API_KEY, format='xml')
	data = espn_api.mlb_athletes()
	status = data.getElementsByTagName('status')
	assert status[0].firstChild.nodeValue == 'success'

# This test will need to be updated once requested data is supported by ESPN
def test_mens_colg_baseball_athletes_xml():
	with pytest.raises(Exception):
		espn_api = AthletesAPI(API_KEY, format='xml')
		data = espn_api.mens_colg_baseball_athletes()

def test_basketball_athletes_xml():
	espn_api = AthletesAPI(API_KEY, format='xml')
	data = espn_api.basketball_athletes()
	status = data.getElementsByTagName('status')
	assert status[0].firstChild.nodeValue == 'success'

def test_nba_athletes_xml():
	espn_api = AthletesAPI(API_KEY, format='xml')
	data = espn_api.nba_athletes()
	status = data.getElementsByTagName('status')
	assert status[0].firstChild.nodeValue == 'success'

def test_wnba_athletes_xml():
	espn_api = AthletesAPI(API_KEY, format='xml')
	data = espn_api.wnba_athletes()
	status = data.getElementsByTagName('status')
	assert status[0].firstChild.nodeValue == 'success'

def test_mens_colg_basketball_athletes_xml():
	espn_api = AthletesAPI(API_KEY, format='xml')
	data = espn_api.mens_colg_basketball_athletes()
	status = data.getElementsByTagName('status')
	assert status[0].firstChild.nodeValue == 'success'

def test_womens_colg_basketball_athletes_xml():
	espn_api = AthletesAPI(API_KEY, format='xml')
	data = espn_api.womens_colg_basketball_athletes()
	status = data.getElementsByTagName('status')
	assert status[0].firstChild.nodeValue == 'success'

def test_football_athletes_xml():
	espn_api = AthletesAPI(API_KEY, format='xml')
	data = espn_api.football_athletes()
	status = data.getElementsByTagName('status')
	assert status[0].firstChild.nodeValue == 'success'

def test_nfl_athletes_xml():
	espn_api = AthletesAPI(API_KEY, format='xml')
	data = espn_api.nfl_athletes()
	status = data.getElementsByTagName('status')
	assert status[0].firstChild.nodeValue == 'success'

def test_colg_football_athletes_xml():
	espn_api = AthletesAPI(API_KEY, format='xml')
	data = espn_api.colg_football_athletes()
	status = data.getElementsByTagName('status')
	assert status[0].firstChild.nodeValue == 'success'

def test_hockey_athletes_xml():
	espn_api = AthletesAPI(API_KEY, format='xml')
	data = espn_api.hockey_athletes()
	status = data.getElementsByTagName('status')
	assert status[0].firstChild.nodeValue == 'success'

def test_nhl_athletes_xml():
	espn_api = AthletesAPI(API_KEY, format='xml')
	data = espn_api.nhl_athletes()
	status = data.getElementsByTagName('status')
	assert status[0].firstChild.nodeValue == 'success'

# This test will need to be updated once requested data is supported by ESPN
def test_mens_colg_hockey_athletes_xml():
	with pytest.raises(Exception):
		espn_api = AthletesAPI(API_KEY, format='xml')
		data = espn_api.mens_colg_hockey_athletes()

# This test will need to be updated once requested data is supported by ESPN
def test_womens_colg_hockey_athletes_xml():
 	with pytest.raises(Exception):
		espn_api = AthletesAPI(API_KEY, format='xml')
		data = espn_api.womens_colg_hockey_athletes()

def test_golf_athletes_xml():
	espn_api = AthletesAPI(API_KEY, format='xml')
	data = espn_api.golf_athletes()
	status = data.getElementsByTagName('status')
	assert status[0].firstChild.nodeValue == 'success'

def test_euro_tour_golf_athletes_xml():
	espn_api = AthletesAPI(API_KEY, format='xml')
	data = espn_api.euro_tour_golf_athletes()
	status = data.getElementsByTagName('status')
	assert status[0].firstChild.nodeValue == 'success'

# This test will need to be updated once requested data is supported by ESPN
def test_lpga_golf_athletes_xml():
 	with pytest.raises(Exception):
		espn_api = AthletesAPI(API_KEY, format='xml')
		data = espn_api.lpga_golf_athletes()

def test_pga_golf_athletes_xml():
	espn_api = AthletesAPI(API_KEY, format='xml')
	data = espn_api.pga_golf_athletes()
	status = data.getElementsByTagName('status')
	assert status[0].firstChild.nodeValue == 'success'

def test_sga_golf_athletes_xml():
	espn_api = AthletesAPI(API_KEY, format='xml')
	data = espn_api.sga_golf_athletes()
	status = data.getElementsByTagName('status')
	assert status[0].firstChild.nodeValue == 'success'

def test_racing_athletes_xml():
	espn_api = AthletesAPI(API_KEY, format='xml')
	data = espn_api.racing_athletes()
	status = data.getElementsByTagName('status')
	assert status[0].firstChild.nodeValue == 'success'

def test_indycar_athletes_xml():
	espn_api = AthletesAPI(API_KEY, format='xml')
	data = espn_api.indycar_athletes()
	status = data.getElementsByTagName('status')
	assert status[0].firstChild.nodeValue == 'success'

def test_sprint_cup_athletes_xml():
	espn_api = AthletesAPI(API_KEY, format='xml')
	data = espn_api.sprint_cup_athletes()
	status = data.getElementsByTagName('status')
	assert status[0].firstChild.nodeValue == 'success'

def test_nationwide_athletes_xml():
	espn_api = AthletesAPI(API_KEY, format='xml')
	data = espn_api.nationwide_athletes()
	status = data.getElementsByTagName('status')
	assert status[0].firstChild.nodeValue == 'success'

def test_camping_world_truck_athletes_xml():
	espn_api = AthletesAPI(API_KEY, format='xml')
	data = espn_api.camping_world_truck_athletes()
	status = data.getElementsByTagName('status')
	assert status[0].firstChild.nodeValue == 'success'

def test_f1_athletes_xml():
	espn_api = AthletesAPI(API_KEY, format='xml')
	data = espn_api.f1_athletes()
	status = data.getElementsByTagName('status')
	assert status[0].firstChild.nodeValue == 'success'

def test_soccer_athletes_xml():
	espn_api = AthletesAPI(API_KEY, format='xml')
	data = espn_api.soccer_athletes()
	status = data.getElementsByTagName('status')
	assert status[0].firstChild.nodeValue == 'success'

def test_mls_athletes_xml():
	espn_api = AthletesAPI(API_KEY, format='xml')
	data = espn_api.mls_athletes()
	status = data.getElementsByTagName('status')
	assert status[0].firstChild.nodeValue == 'success'

def test_la_liga_athletes_xml():
	espn_api = AthletesAPI(API_KEY, format='xml')
	data = espn_api.la_liga_athletes()
	status = data.getElementsByTagName('status')
	assert status[0].firstChild.nodeValue == 'success'

def test_premier_league_athletes_xml():
	espn_api = AthletesAPI(API_KEY, format='xml')
	data = espn_api.premier_league_athletes()
	status = data.getElementsByTagName('status')
	assert status[0].firstChild.nodeValue == 'success'

def test_tennis_athletes_xml():
	espn_api = AthletesAPI(API_KEY, format='xml')
	data = espn_api.tennis_athletes()
	status = data.getElementsByTagName('status')
	assert status[0].firstChild.nodeValue == 'success'

def test_atp_athletes_xml():
	espn_api = AthletesAPI(API_KEY, format='xml')
	data = espn_api.atp_athletes()
	status = data.getElementsByTagName('status')
	assert status[0].firstChild.nodeValue == 'success'

def test_wta_athletes_xml():
	espn_api = AthletesAPI(API_KEY, format='xml')
	data = espn_api.wta_athletes()
	status = data.getElementsByTagName('status')
	assert status[0].firstChild.nodeValue == 'success'


# Tests for TeamsAPI Class
# Tests for each available function within the class that returns JSON data
def test_baseball_leagues_json():
	espn_api = TeamsAPI(API_KEY, format='json')
	data = espn_api.baseball_leagues()
	assert data['status'] == 'success'

def test_mlb_teams_json():
	espn_api = TeamsAPI(API_KEY, format='json')
	data = espn_api.mlb_teams()
	assert data['status'] == 'success'

# This test will need to be updated once requested data is supported by ESPN
def test_mens_colg_baseball_teams_json():
	with pytest.raises(Exception):
		espn_api = TeamsAPI(API_KEY, format='json')
		data = espn_api.mens_colg_baseball_teams()

def test_basketball_leagues_json():
	espn_api = TeamsAPI(API_KEY, format='json')
	data = espn_api.basketball_leagues()
	assert data['status'] == 'success'

def test_nba_teams_json():
	espn_api = TeamsAPI(API_KEY, format='json')
	data = espn_api.nba_teams()
	assert data['status'] == 'success'

def test_wnba_teams_json():
	espn_api = TeamsAPI(API_KEY, format='json')
	data = espn_api.wnba_teams()
	assert data['status'] == 'success'

def test_mens_colg_basketball_teams_json():
	espn_api = TeamsAPI(API_KEY, format='json')
	data = espn_api.mens_colg_basketball_teams()
	assert data['status'] == 'success'

def test_womens_colg_basketball_teams_json():
	espn_api = TeamsAPI(API_KEY, format='json')
	data = espn_api.womens_colg_basketball_teams()
	assert data['status'] == 'success'

def test_football_leagues_json():
	espn_api = TeamsAPI(API_KEY, format='json')
	data = espn_api.football_leagues()
	assert data['status'] == 'success'

def test_nfl_teams_json():
	espn_api = TeamsAPI(API_KEY, format='json')
	data = espn_api.nfl_teams()
	assert data['status'] == 'success'

def test_colg_football_teams_json():
	espn_api = TeamsAPI(API_KEY, format='json')
	data = espn_api.colg_football_teams()
	assert data['status'] == 'success'

def test_hockey_leagues_json():
	espn_api = TeamsAPI(API_KEY, format='json')
	data = espn_api.hockey_leagues()
	assert data['status'] == 'success'

def test_nhl_teams_json():
	espn_api = TeamsAPI(API_KEY, format='json')
	data = espn_api.nhl_teams()
	assert data['status'] == 'success'

# This test will need to be updated once requested data is supported by ESPN
def test_mens_colg_hockey_teams_json():
	with pytest.raises(Exception):
		espn_api = TeamsAPI(API_KEY, format='json')
		data = espn_api.mens_colg_hockey_teams()

# This test will need to be updated once requested data is supported by ESPN
def test_womens_colg_hockey_teams_json():
	with pytest.raises(Exception):
		espn_api = TeamsAPI(API_KEY, format='json')
		data = espn_api.womens_colg_hockey_teams()

# Tests for each available function within the class that returns XML data
def test_baseball_leagues_xml():
	espn_api = TeamsAPI(API_KEY, format='xml')
	data = espn_api.baseball_leagues()
	status = data.getElementsByTagName('status')
	assert status[0].firstChild.nodeValue == 'success'

def test_mlb_teams_xml():
	espn_api = TeamsAPI(API_KEY, format='xml')
	data = espn_api.mlb_teams()
	status = data.getElementsByTagName('status')
	assert status[0].firstChild.nodeValue == 'success'

# This test will need to be updated once requested data is supported by ESPN
def test_mens_colg_baseball_teams_xml():
	with pytest.raises(Exception):
		espn_api = TeamsAPI(API_KEY, format='xml')
		data = espn_api.mens_colg_baseball_teams()

def test_basketball_leagues_xml():
	espn_api = TeamsAPI(API_KEY, format='xml')
	data = espn_api.basketball_leagues()
	status = data.getElementsByTagName('status')
	assert status[0].firstChild.nodeValue == 'success'

def test_nba_teams_xml():
	espn_api = TeamsAPI(API_KEY, format='xml')
	data = espn_api.nba_teams()
	status = data.getElementsByTagName('status')
	assert status[0].firstChild.nodeValue == 'success'

def test_wnba_teams_xml():
	espn_api = TeamsAPI(API_KEY, format='xml')
	data = espn_api.wnba_teams()
	status = data.getElementsByTagName('status')
	assert status[0].firstChild.nodeValue == 'success'

def test_mens_colg_basketball_teams_xml():
	espn_api = TeamsAPI(API_KEY, format='xml')
	data = espn_api.mens_colg_basketball_teams()
	status = data.getElementsByTagName('status')
	assert status[0].firstChild.nodeValue == 'success'

def test_womens_colg_basketball_teams_xml():
	espn_api = TeamsAPI(API_KEY, format='xml')
	data = espn_api.womens_colg_basketball_teams()
	status = data.getElementsByTagName('status')
	assert status[0].firstChild.nodeValue == 'success'

def test_football_leagues_xml():
	espn_api = TeamsAPI(API_KEY, format='xml')
	data = espn_api.football_leagues()
	status = data.getElementsByTagName('status')
	assert status[0].firstChild.nodeValue == 'success'

def test_nfl_teams_xml():
	espn_api = TeamsAPI(API_KEY, format='xml')
	data = espn_api.nfl_teams()
	status = data.getElementsByTagName('status')
	assert status[0].firstChild.nodeValue == 'success'

def test_colg_football_teams_xml():
	espn_api = TeamsAPI(API_KEY, format='xml')
	data = espn_api.colg_football_teams()
	status = data.getElementsByTagName('status')
	assert status[0].firstChild.nodeValue == 'success'

def test_hockey_leagues_xml():
	espn_api = TeamsAPI(API_KEY, format='xml')
	data = espn_api.hockey_leagues()
	status = data.getElementsByTagName('status')
	assert status[0].firstChild.nodeValue == 'success'

def test_nhl_teams_xml():
	espn_api = TeamsAPI(API_KEY, format='xml')
	data = espn_api.nhl_teams()
	status = data.getElementsByTagName('status')
	assert status[0].firstChild.nodeValue == 'success'

# This test will need to be updated once requested data is supported by ESPN
def test_mens_colg_hockey_teams_xml():
	with pytest.raises(Exception):
		espn_api = TeamsAPI(API_KEY, format='xml')
		data = espn_api.mens_colg_hockey_teams()

# This test will need to be updated once requested data is supported by ESPN
def test_womens_colg_hockey_teams_xml():
	with pytest.raises(Exception):
		espn_api = TeamsAPI(API_KEY, format='xml')
		data = espn_api.basketball_athletes()


# Tests for EspnNowAPI Class
# Tests for each available function within the class that returns JSON data
def test_most_recent_news_json():
	espn_api = EspnNowAPI(API_KEY, format='json')
	data = espn_api.most_recent_news()
	assert data['status'] == 'success'

def test_top_news_json():
	espn_api = EspnNowAPI(API_KEY, format='json')
	data = espn_api.top_news()
	assert data['status'] == 'success'

def test_most_popular_news_json():
	espn_api = EspnNowAPI(API_KEY, format='json')
	data = espn_api.most_popular_news()
	assert data['status'] == 'success'

# Tests for each available function within the class that returns XML data
def test_most_recent_news_xml():
	espn_api = EspnNowAPI(API_KEY, format='xml')
	data = espn_api.most_recent_news()
	status = data.getElementsByTagName('status')
	assert status[0].firstChild.nodeValue == 'success'

def test_top_news_xml():
	espn_api = EspnNowAPI(API_KEY, format='xml')
	data = espn_api.top_news()
	status = data.getElementsByTagName('status')
	assert status[0].firstChild.nodeValue == 'success'

def test_most_popular_news_xml():
	espn_api = EspnNowAPI(API_KEY, format='xml')
	data = espn_api.most_popular_news()
	status = data.getElementsByTagName('status')
	assert status[0].firstChild.nodeValue == 'success'