try:
    import simplejson as json
except ImportError:
    import json

import requests
from xml.dom.minidom import parseString

class EspnBase(object):
    """Base wrapper used for all ESPN API classes. For further information on
    the API itself see: http://developer.espn.com/
    """
    def __init__(self):
        """Basic initialization of EspnBase class"""
        self.api_url = 'http://api.espn.com/v1'

    def _get_response(self, r):
        if self._ok_status(r.status_code) and r.status_code is not 404:
            if r.headers['content-type'].split(";")[0] == 'application/json':
                return r.json()
            elif r.headers['content-type'].split(";")[0] == 'text/xml':
                #returns xml.dom.minidom.Document instance
                data = parseString(r.text)
                return data
            else:
                raise Exception("Did not receive json from the api: %s" % str(r))
        else:
            self.handle_exception(r, r.status_code)

    @classmethod
    def _ok_status(cls, status_code):
        """Check if status code is OK status i.e. 2xx or 404"""
        if status_code / 200 is 1:
            return True
        elif status_code / 400 is 1:
            if status_code is 404:
                return True
            else:
                return False
        elif status_code is 500:
            return False

    def handle_exception(self, r, status_code):
        if r.headers['content-type'].split(";")[0] == 'application/json':
            data = json.loads(r.text)
            raise Exception("Got an error: %s\nMessage: %s" %
                            (str(status_code), data['message']))
        elif r.headers['content-type'].split(";")[0] == 'text/xml':
            data = parseString(r.text)
            message = data.getElementsByTagName('message')
            msg = message[0].firstChild.nodeValue
            raise Exception("Got an error: %s\nMessage: %s" %
                           (str(status_code), msg))
        else:
            raise Exception('Got an unexpected error')

    def build_url_params(self, enable=None, groups=None, rostertype=None,
                         dates=None, teams=None, athletes=None, events=None,
                         disable=None, insider=None, lang=None, region=None,
                         leagues=None, limit=None, offset=None):
        params = ''
        if enable:
            params += "enable=%s&" % enable
        if groups:
            params += "groups=%s&" % groups
        if rostertype:
            params += "rostertype=%s&" % rostertype
        if dates:
            params += "dates=%s&" % dates
        if teams:
            params += "teams=%s&" % teams
        if athletes:
            params += "athletes=%s&" % athletes
        if events:
            params += "events=%s&" % events
        if disable:
            params += "disable=%s&" % disable
        if insider:
            params += "insider=%s&" % insider
        if lang:
            params += "lang=%s&" % lang
        if region:
            params += "region=%s&" % lang
        if leagues:
            params += "leagues=%s&" % leagues
        if limit:
            params += "limit=%d&" % limit
        if offset:
            params += "offset=%d&" % offset
        return params


class HeadlinesAPI(EspnBase):
    """Basic wrapper for the ESPN Headlines API. For further information on the 
    API itself see: http://developer.espn.com/docs/headlines
    """
    def __init__(self, api_key, format):       
        self.api_url = 'http://api.espn.com/v1'
        self.api_key = 'apikey=' + api_key
        if format is "json":
            self.headers = {'Accept': 'application/json'}
        if format is "xml":
            self.headers = {'Accept': 'text/xml'}

    def _headlines_get(self, api_target, **kwargs):
        params = self.build_url_params(**kwargs)
        r = requests.get(api_target + "?" + params + self.api_key, 
                         headers=self.headers)
        return self._get_response(r)

    def list_headlines(self, news_section, sport_name=None, league_name=None, 
                       method='default', headline_ID=None, **kwargs):
        """Latest sports news and analysis from ESPN. Generic method for 
        parsing data from ESPN Headlines API with optional keyword parameters. 

        :param news_section: News section
        :param sport_name: Sport name
        :param league_name: League / organizing body within the sport
        :param method: Type of stories to retrieve
        :param headline_id: ID of specific story to retrieve (Optional)
        :param **kwargs: Optional parameters specific to the Headlines API
        """
        if news_section == 'sports':
            api_target = self.api_url + '/sports'
        else:
            api_target = self.api_url + '/%s' % news_section
        if sport_name:
            api_target = api_target + '/' + sport_name
        if league_name:
            api_target = api_target + '/' + league_name

        if method is 'default':
            api_target = '/'.join([api_target, 'news/'])
        elif method is 'headlines':
            api_target = '/'.join([api_target, 'news/headlines/'])
        elif method is 'top':
            api_target = '/'.join([api_target, 'news/headlines/top/'])

        return self._headlines_get(api_target, **kwargs)

    def sports_headlines(self, **kwargs):
        """List Sports headlines for all sports and leagues"""
        return self.list_headlines('sports', **kwargs)

    def city_sites_headlines(self, **kwargs):
        """List ESPN City Sites headlines for all sports and leagues"""
        return self.list_headlines(news_section='cities', **kwargs)

    def espnw_headlines(self, **kwargs):
        """List ESPNW headlines for all sports and leagues"""
        return self.list_headlines(news_section='espnw', **kwargs)

    def fantasy_headlines(self, **kwargs):
        """List Fantasy headlines for all sports and leagues"""
        return self.list_headlines(news_section='fantasy', **kwargs)

    def espn_mag_headlines(self, **kwargs):
        """List ESPN Magazine headlines for all sports and leagues"""
        return self.list_headlines(news_section='magazine', **kwargs)


class AthletesAPI(EspnBase):
    """Basic wrapper for the ESPN Athletes API. For further information on the API 
    itself see: http://developer.espn.com/docs/athletes
    """
    def __init__(self, api_key, format):
        """Basic initialization of AthletesAPI class

        :param api_key: Api authorization key
        :param format: Format to return requested data in ('JSON' or 'XML')
        """        
        self.api_url = 'http://api.espn.com/v1/sports'
        self.api_key = 'apikey=' + api_key
        if format is "json":
            self.headers = {'Accept': 'application/json'}
        if format is "xml":
            self.headers = {'Accept': 'text/xml'}

    def _athletes_get(self, api_target, **kwargs):
        params = self.build_url_params(**kwargs)
        r = requests.get(api_target + "?" + params + self.api_key, 
                         headers=self.headers)
        return self._get_response(r)

    def list_athletes(self, sport_name, league_name, athlete_ID=None, **kwargs):
        """Athlete stats and information from ESPN. Generic method for 
        parsing data from ESPN Athletes API with optional keyword parameters.

        :param sport_name: Sport name
        :param league_name: League / organizing body within the sport
        :param athlete_id: Specific athlete ID
        :param **kwargs: Optional parameters specific to the Athletes API
        """
        if sport_name and league_name:
            api_target = '/'.join([self.api_url, sport_name, league_name, 'athletes/'])

        if athlete_ID:
            api_target += '%s/' % athlete_ID

        return self._athletes_get(api_target, **kwargs)
        
    def baseball_athletes(self):
        """List Baseball athletes"""
        api_target = '/'.join([self.api_url, 'baseball', 'athletes/'])
        return self._athletes_get(api_target)

    def mlb_athletes(self, **kwargs):
        """List all MLB athletes"""
        return self.list_athletes('baseball', 'mlb', **kwargs)

    def mens_colg_baseball_athletes(self, **kwargs):
        """List all College Baseball athletes."""
        return self.list_athletes('baseball', 'college-baseball', **kwargs)

    def basketball_athletes(self):
        """List all Basketball athletes"""
        api_target = '/'.join([self.api_url, 'basketball', 'athletes/'])
        return self._athletes_get(api_target)

    def nba_athletes(self, **kwargs):
        """List all NBA athletes"""
        return self.list_athletes('basketball', 'nba', **kwargs)

    def wnba_athletes(self, **kwargs):
        """List all WNBA athletes"""
        return self.list_athletes('basketball', 'wnba', **kwargs)

    def mens_colg_basketball_athletes(self, **kwargs):
        """List all Mens College Basketball athletes."""
        return self.list_athletes('basketball', 'mens-college-basketball',
                                  **kwargs)

    def womens_colg_basketball_athletes(self, **kwargs):
        """List all Womens College Basketball athletes."""
        return self.list_athletes('basketball', 'womens-college-basketball', 
                                  **kwargs)

    def football_athletes(self):
        """List all Football athletes"""
        api_target = '/'.join([self.api_url, 'football', 'athletes/'])
        return self._athletes_get(api_target)

    def nfl_athletes(self, **kwargs):
        """List all NFL teams"""
        return self.list_athletes('football', 'nfl')

    def colg_football_athletes(self, **kwargs):
        """List all College Football athletes."""
        return self.list_athletes('football', 'college-football', **kwargs)

    def hockey_athletes(self):
        """List all Hockey athletes"""
        api_target = '/'.join([self.api_url, 'hockey', 'athletes/'])
        return self._athletes_get(api_target)

    def nhl_athletes(self, **kwargs):
        """List all NHL athletes"""
        return self.list_athletes('hockey', 'nhl')

    def mens_colg_hockey_athletes(self, **kwargs):
        """List all Mens College Hockey athletes."""
        return self.list_athletes('hockey', 'mens-college-hockey', **kwargs)

    def womens_colg_hockey_athletes(self, **kwargs):
        """List all Womens College Hockey athletes."""
        return self.list_athletes('hockey', 'womens-college-hockey', **kwargs)

    def golf_athletes(self):
        """List all Golf athletes"""
        api_target = '/'.join([self.api_url, 'golf', 'athletes/'])
        return self._athletes_get(api_target)

    def euro_tour_golf_athletes(self, **kwargs):
        """List all European Tour athletes"""
        return self.list_athletes('golf', 'eur')

    def lpga_golf_athletes(self, **kwargs):
        """List all LPGA athletes"""
        return self.list_athletes('golf', 'lpga')

    def pga_golf_athletes(self, **kwargs):
        """List all PGA athletes"""
        return self.list_athletes('golf', 'pga')

    def sga_golf_athletes(self, **kwargs):
        """List all SGA athletes"""
        return self.list_athletes('golf', 'sga')

    def racing_athletes(self):
        """List all Racing athletes"""
        api_target = '/'.join([self.api_url, 'racing', 'athletes/'])
        return self._athletes_get(api_target)

    def indycar_athletes(self):
        """List all IndyCar Series athletes"""
        return self.list_athletes('racing', 'irl')

    def sprint_cup_athletes(self, **kwargs):
        """List all NASCAR Sprint Cup athletes"""
        return self.list_athletes('racing', 'sprint')

    def nationwide_athletes(self, **kwargs):
        """List all NASCAR Nationwide athletes"""
        return self.list_athletes('racing', 'nationwide')

    def camping_world_truck_athletes(self, **kwargs):
        """List all NASCAR Camping World Truck athletes"""
        return self.list_athletes('racing', 'truck')

    def f1_athletes(self):
        """List all Formula One athletes"""
        return self.list_athletes('racing', 'f1')

    def soccer_athletes(self):
        """List all Soccer athletes"""
        api_target = '/'.join([self.api_url, 'soccer', 'athletes/'])
        return self._athletes_get(api_target)

    def mls_athletes(self, **kwargs):
        """List all Major League Soccer athletes"""
        return self.list_athletes('soccer', 'usa.1')

    def la_liga_athletes(self, **kwargs):
        """List all Spanish Primera Division(La Liga) athletes"""
        return self.list_athletes('soccer', 'esp.1')

    def premier_league_athletes(self, **kwargs):
        """List all Barclays Premier League athletes"""
        return self.list_athletes('soccer', 'eng.1')

    def tennis_athletes(self):
        """List all Tennis athletes"""
        api_target = '/'.join([self.api_url, 'tennis', 'athletes/'])
        return self._athletes_get(api_target)

    def atp_athletes(self, **kwargs):
        """List all Association of Tennis Professionals(ATP) athletes"""
        return self.list_athletes('tennis', 'atp')

    def wta_athletes(self, **kwargs):
        """List all Womens Tennis Association(WTA) athletes"""
        return self.list_athletes('tennis', 'wta')


class TeamsAPI(EspnBase):
    """Basic wrapper for the ESPN Teams API. For further information on the API 
    itself see: http://developer.espn.com/docs/teams
    """
    def __init__(self, api_key, format):
        """Basic initialization of TeamsAPI class

        :param api_key: Api authorization key
        :param format: Format to return requested data in ('JSON' or 'XML')
        """
        self.api_url = 'http://api.espn.com/v1/sports'
        self.api_key = 'apikey=' + api_key
        if format is "json":
            self.headers = {'Accept': 'application/json'}
        if format is "xml":
            self.headers = {'Accept': 'text/xml'}

    def _teams_get(self, api_target, **kwargs):
        params = self.build_url_params(**kwargs)
        r = requests.get(api_target + "?" + params + self.api_key, 
                         headers=self.headers)
        return self._get_response(r)

    def list_teams(self, sport_name, league_name, team_id=None, **kwargs):
        """Sports team stats and information from ESPN. Generic method for 
        parsing data from ESPN Teams API with optional keyword parameters. 

        :param sport_name: Sport name
        :param league_name: League / organizing body within the sport
        :param team_id: Specific team ID (optional)
        :param **kwargs: Optional parameters specific to the Teams API
        """
        if sport_name and league_name:
            api_target = '/'.join([self.api_url, sport_name, league_name,
                                   'teams/'])
        return self._teams_get(api_target, **kwargs)

    def baseball_leagues(self):
        """List all Baseball leagues"""
        api_target = '/'.join([self.api_url, 'baseball', 'teams/'])
        return self._teams_get(api_target)

    def mlb_teams(self):
        """List all MLB teams"""
        return self.list_teams('baseball', 'mlb')

    def mens_colg_baseball_teams(self, **kwargs):
        """List all College Baseball teams."""
        return self.list_teams('baseball', 'college-baseball', **kwargs)

    def basketball_leagues(self):
        """List all Basketball leagues"""
        api_target = '/'.join([self.api_url, 'basketball', 'teams/'])
        return self._teams_get(api_target)

    def nba_teams(self):
        """List all NBA teams"""
        return self.list_teams('basketball', 'nba')

    def wnba_teams(self):
        """List all WNBA teams"""
        return self.list_teams('basketball', 'wnba')

    def mens_colg_basketball_teams(self, **kwargs):
        """List all Mens College Basketball teams."""
        return self.list_teams('basketball', 'mens-college-basketball',
                               **kwargs)

    def womens_colg_basketball_teams(self, **kwargs):
        """List all Womens College Basketball teams."""
        return self.list_teams('basketball', 'womens-college-basketball', 
                               **kwargs)

    def football_leagues(self):
        """List all Football leagues"""
        api_target = '/'.join([self.api_url, 'football', 'teams/'])
        return self._teams_get(api_target)

    def nfl_teams(self):
        """List all NFL teams"""
        return self.list_teams('football', 'nfl')

    def colg_football_teams(self, **kwargs):
        """List all College Football teams."""
        return self.list_teams('football', 'college-football', **kwargs)

    def hockey_leagues(self):
        """List all Hockey leagues"""
        api_target = '/'.join([self.api_url, 'hockey', 'teams/'])
        return self._teams_get(api_target)

    def nhl_teams(self):
        """List all NHL teams"""
        return self.list_teams('hockey', 'nhl')

    def mens_colg_hockey_teams(self, **kwargs):
        """List all Mens College Hockey teams."""
        return self.list_teams('hockey', 'mens-college-hockey', **kwargs)

    def womens_colg_hockey_teams(self, **kwargs):
        """List all Womens College Hockey teams."""
        return self.list_teams('hockey', 'womens-college-hockey', **kwargs)


class EspnNowAPI(EspnBase):
    """Basic wrapper for the ESPN Now API. For further information on the API 
    itself see: http://developer.espn.com/docs/now
    """
    def __init__(self, api_key, format):
        """Basic initialization of EspnNow class

        :param api_key: Api authorization key
        :param format: Format to return requested data in ('JSON' or 'XML')
        """
        self.api_url = 'http://api.espn.com/v1/now'
        self.api_key = 'apikey=' + api_key
        if format is "json":
            self.headers = {'Accept': 'application/json'}
        if format is "xml":
            self.headers = {'Accept': 'text/xml'}

    def _espn_now_get(self, api_target, **kwargs):
        params = self.build_url_params(**kwargs)
        r = requests.get(api_target + "?" + params + self.api_key, 
                         headers=self.headers)
        return self._get_response(r)

    def most_recent_news(self, **kwargs):
        """List most recent ESPN news content.
        
        :param **kwargs: Optional parameters specific to the EspnNow API
        """
        api_target = self.api_url + '/'
        return self._espn_now_get(api_target, **kwargs)

    def top_news(self, **kwargs):
        """List top ESPN news content.
        
        :param **kwargs: Optional parameters specific to the Teams API
        """
        api_target = '/'.join([self.api_url, 'top/'])
        return self._espn_now_get(api_target, **kwargs)

    def most_popular_news(self, **kwargs):
        """List most popular ESPN news content.
        
        :param **kwargs: Optional parameters specific to the Teams API
        """
        api_target = '/'.join([self.api_url, 'popular/'])
        return self._espn_now_get(api_target, **kwargs)