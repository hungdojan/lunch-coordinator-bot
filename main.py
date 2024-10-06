# A telegram bot that sends a poll to a chat with the options for lunch times tomorrow

import os
import requests
from datetime import datetime, timedelta

token = os.getenv("TELEGRAM_BOT_TOKEN")
chat_id = os.getenv("TELEGRAM_CHAT_ID")

base_url = f"https://api.telegram.org/bot{token}/"

# print(requests.get(base_url + "getUpdates").json())

today = datetime.now()
tomorrow = today + timedelta(days=1)

question = f"Lunch {tomorrow.strftime('%A (%d.%m.%Y)')}"
options = ["11-12h", "12-13h", "13-14h", "14-15h"]

send_poll_result = requests.post(base_url + "sendPoll", json = {
	"chat_id": chat_id,
	"question": question,
	"options": options,
	"allows_multiple_answers": True,
	"is_anonymous": False,
})
if send_poll_result.status_code != 200:
	print("Error sending poll")
	print(send_poll_result.json())
	exit(1)