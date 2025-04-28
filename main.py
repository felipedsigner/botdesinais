import time
import schedule
from signal_logic import analyze_and_send_signals

def job():
    analyze_and_send_signals()

# Agendar o bot para rodar a cada 2 horas
schedule.every(2).hours.do(job)

# Rodar o agendamento
while True:
    schedule.run_pending()
    time.sleep(1)
