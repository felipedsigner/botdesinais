import requests
from bs4 import BeautifulSoup

def get_game_data():
    url = "https://www.sofascore.com/pt/futebol"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    games = soup.find_all('div', class_='event-class')  # Ajuste conforme a estrutura da página
    game_info = []

    for game in games:
        home_team = game.find('span', class_='home-team').text.strip()
        away_team = game.find('span', class_='away-team').text.strip()
        time = game.find('span', class_='event-time').text.strip()
        tournament = game.find('span', class_='event-tournament').text.strip()

        game_info.append((home_team, away_team, time, tournament))
    
    return game_info
