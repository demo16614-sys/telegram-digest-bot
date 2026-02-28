import requests
import os
from datetime import datetime

TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

def send_digest():
    today = datetime.now().strftime("%Y-%m-%d")

    message = f"""
🟢 Weekly Digest - {today}

✅ Tasks Completed:
- Example task 1
- Example task 2

📊 Goals:
- Keep building
- Stay consistent

🔥 Keep going genius!
"""

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }

    requests.post(url, data=payload)

if __name__ == "__main__":

    send_digest()
