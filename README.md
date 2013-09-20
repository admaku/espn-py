# ESPN Python API Wrapper

Simple Python wrapper around the [ESPN API](http://developer.espn.com/)

This project is a work in progress.

### Installation

`pip install sandman`

## Headlines API
- list_headlines
- sports_headlines
- city_sites_headlines
- espnw_headlines
- fantasy_headlines
- espn_mag_headlines

## Athletes API
- list_athletes
- baseball_athletes
- mlb_athletes
- mens_colg_baseball_athletes (Requested data isn't supported at this time by ESPN)
- basketball_athletes
- nba_athletes
- wnba_athletes
- mens_colg_basketball_athletes
- womens_colg_basketball_athletes
- football_athletes
- nfl_athletes
- colg_football_athletes
- hockey_athletes
- nhl_athletes
- mens_colg_hockey_athletes
- womens_colg_hockey_athletes (Requested data isn't supported at this time by ESPN)
- golf_athletes
- euro_tour_golf_athletes
- lpga_golf_athletes (Requested data isn't supported at this time by ESPN)
- pga_golf_athletes
- sga_golf_athletes
- racing_athletes
- indycar_athletes
- sprint_cup_athletes
- nationwide_athletes
- camping_world_truck_athletes
- f1_athletes
- soccer_athletes
- mls_athletes
- la_liga_athletes
- premier_league_athletes
- tennis_athletes
- atp_athletes
- wta_athletes

## Teams API
- list_teams
- baseball_leagues
- mlb_teams
- mens_colg_baseball_teams (Requested data isn't supported at this time by ESPN)
- basketball_leagues
- nba_teams
- wnba_teams
- mens_colg_basketball_teams
- womens_colg_basketball_teams
- football_leagues
- nfl_teams
- colg_football_teams
- hockey_leagues
- nhl_teams
- mens_colg_hockey_teams
- womens_colg_hockey_teams (Requested data isn't supported at this time by ESPN)

## EspnNow API
- most_recent_news
- top_news
- most_popular_news

Sample:

    from espn_py import espn
    espn_api = espn.TeamsAPI('YOURAPIKEY', format='json')

    # see all MLB teams
	mlb_teams = espn_api.list_teams('baseball', 'mlb')