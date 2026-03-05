import requests
import os
from datetime import datetime
from openai import OpenAI

# Load secrets
TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")
OPENAI_KEY = os.environ.get("OPENAI_API_KEY")

# Create OpenAI client
client = OpenAI(api_key=OPENAI_KEY)

def generate_ai_digest():
    today = datetime.now().strftime("%Y-%m-%d")

    prompt = f"""
    Today is {today}.

    Give me a weekly update for Myanmar region and global trends.

Structure it clearly with:

1️ Top 5 viral social media trends in Myanmar (Facebook, TikTok, YouTube)
– Short explanation (2–3 lines each)
– Why it went viral
– Category (entertainment, politics, meme, social issue, tech, etc.)

2️ Top 5 important news in Myanmar this week
– Very concise summary
– Why it matters

3️ Top 5 global viral trends
– Platform mentioned
– Why trending

4️ Top 5 important global news
– Economy / tech / politics / major events
– 2–3 lines each

Format everything so I can read it within 30 minutes.
No unnecessary long explanation.
Focus on high-impact information only.
Avoid gossip unless extremely viral.

End with a “What Actually Matters This Week” summary 
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ],
    )

    return response.choices[0].message.content

def send_to_telegram(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }

    requests.post(url, data=payload)

if __name__ == "__main__":
    ai_message = generate_ai_digest()
    send_to_telegram(ai_message)
