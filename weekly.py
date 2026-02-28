import requests
import os
from datetime import datetime

TOKEN = os.environ.get(8667343851:AAHtjsQR-BT57jXBDYFr4NdWvC6R-qcRzUA)
CHAT_ID = os.environ.get(1686479134)

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