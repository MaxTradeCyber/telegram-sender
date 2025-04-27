import requests
import time

BOT_TOKEN = '8121218195:AAHOJHGEbGIQXvvxtHk7KmyGHQW0UqEvEVs'
CHAT_ID = '@MaxTradingAssistant'
MESSAGE = 'Тестовое сообщение от сервера!'

def send_message():
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": MESSAGE
    }
    requests.post(url, json=payload)

while True:
    send_message()
    time.sleep(1800)  # 1800 секунд = 30 минут
