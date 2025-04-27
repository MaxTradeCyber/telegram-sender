import requests
import time

# Твой токен бота
TOKEN = '8121218195:AAHOJHGEbGIQXvvxtHk7KmyGHQW0UqEvEVs'

# ID чата или канала, куда отправлять сообщение
CHAT_ID = '@MaxTradingAssistant'

# Сообщение, которое будет отправляться
MESSAGE = 'Привет! Это автоматическое сообщение каждые 30 минут.'

def send_message():
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        'chat_id': CHAT_ID,
        'text': MESSAGE
    }
    requests.post(url, json=payload)

if __name__ == "__main__":
    while True:
        send_message()
        time.sleep(1800)  # Пауза 30 минут
