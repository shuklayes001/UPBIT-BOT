import requests
import time
import os

# ===== CONFIG =====
TELEGRAM_TOKEN = os.environ["8008238927:AAGJsPjX-PyAdqZiHg2QcaYrk_A5w4qwidE"]
CHAT_ID = os.environ["1680874718"]
UPBIT_API_URL = "https://api.upbit.com/v1/market/all"

# ===== FUNCTIONS =====
def send_message(text):
    """Send a Telegram message to your personal chat"""
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text, "parse_mode": "HTML"}
    requests.post(url, data=payload)

def get_upbit_markets():
    """Fetch all Upbit markets"""
    res = requests.get(UPBIT_API_URL)
    if res.status_code == 200:
        return [coin["market"] for coin in res.json()]
    else:
        print("❌ Error fetching Upbit data:", res.status_code)
        return []

# ===== MAIN LOOP =====
print("✅ Personal Upbit Listing Bot started...")
send_message("🤖 Bot Started: Tracking new Upbit listings for you!")

known_markets = set(get_upbit_markets())

while True:
    time.sleep(60)  # check every 60 seconds
    current_markets = set(get_upbit_markets())
    new_listings = current_markets - known_markets

    if new_listings:
        for listing in new_listings:
            send_message(f"🚀 New coin listed on Upbit!\nMarket: <b>{listing}</b>")
        known_markets = current_markets