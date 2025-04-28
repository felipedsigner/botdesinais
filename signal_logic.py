from sofascore_api import get_game_data
from odds_api import get_odds
from settings import ALLOWED_TOURNAMENTS, MIN_ODDS
from telegram_bot import send_signal

def analyze_and_send_signals():
    game_data = get_game_data()

    for game in game_data:
        home_team, away_team, time, tournament = game

        if tournament not in ALLOWED_TOURNAMENTS:
            continue

        odds = get_odds(f"{home_team} vs {away_team}")  # Aqui você pode definir como pegar a odds do jogo

        if odds and odds[0]['h2h'][0]['price'] >= MIN_ODDS:
            signal = f"🟢 **Sinal de Aposta** 🟢\nJogo: {home_team} vs {away_team}\nOdds: {odds[0]['h2h'][0]['price']}\nHorário: {time}\nTorneio: {tournament}\n\n*Boa sorte!*"
            send_signal(signal)
