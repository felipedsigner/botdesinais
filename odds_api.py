import requests
from settings import ODDS_API_KEY

def get_odds(match_id):
    url = f"https://api.the-odds-api.com/v4/sports/soccer/odds"
    params = {
        'apiKey': ODDS_API_KEY,
        'regions': 'us',  # Região que você deseja, se necessário
        'markets': 'h2h',  # Head-to-head
    }

    response = requests.get(url, params=params)
    odds_data = response.json()
    
    return odds_data
