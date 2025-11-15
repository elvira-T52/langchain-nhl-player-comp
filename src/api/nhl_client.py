import requests
from typing import Optional, Dict, List
from nhlpy import NHLClient 

"""
NHL API Client

This module handles all interactions with the NHL API.
You'll implement functions here to:
- Search for players by name
- Fetch player career statistics
- Retrieve advanced analytics (Corsi, Fenwick, xG, etc.)

Resources:
- NHL Stats API: https://gitlab.com/dword4/nhlapi
- Example endpoint: https://api-web.nhle.com/v1/player/{playerId}/landing
"""

class NHLDataClient:

    def __init__ (self):
        "Constructor for NHLClient Def"
        self.client = NHLClient()
        

    def search_player (self, playerFirstName: str, playerLastName: str, teamAbbv: str, givenYear:int = None) -> dict:
        """
        So I can't directly search a player, so here, in this function search_player, I simply just search through the default rosters to try and find a player, unless the
        user tries to add a year where a player exists. Ill add in some graceful handling whenever this function is called to ensure that it doesn't continue if there is no player found.
        

        
        """
        if givenYear is None:
            roster = self.client.teams.team_roster(team_abbr = teamAbbv, season = "20242025")
            fullRoster = roster['forwards'] + roster['defensemen'] + roster['goalies']
        else:
            roster = self.client.teams.team_roster(team_abbr = teamAbbv, season = givenYear)
            fullRoster = roster['forwards'] + roster['defensemen'] + roster['goalies']
        
        for player in roster:
            rosterFirstName = player.get('firstName', {}.get('default', '')).lower()
            rosterLastName = player.get('lastName', {}.get('default', '')).lower()

            #Check if names match
            if rosterFirstName == playerFirstName.strip().lower() and rosterLastName.strip().lower() == playerLastName:
                return player.get('id')
        ##Return if not found
        return None

    def get_player_stats(self, player_id: int) -> dict:
        pass

    def get_advanced_stats(self, player_id: int, season: str= None) -> dict:
        pass
