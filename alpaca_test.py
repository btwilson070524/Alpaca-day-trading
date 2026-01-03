import os
import requests

API_KEY = os.getenv("ALPACA_API_KEY", "")
SECRET_KEY = os.getenv("ALPACA_SECRET_KEY", "")
BASE_URL = os.getenv("ALPACA_BASE_URL", "")

print("BASE_URL =", BASE_URL)
print("API_KEY prefix =", API_KEY[:2], " len =", len(API_KEY))
print("SECRET_KEY len =", len(SECRET_KEY))

if not API_KEY or not SECRET_KEY or not BASE_URL:
    raise RuntimeError("Missing Alpaca environment variables")

headers = {
    "APCA-API-KEY-ID": API_KEY.strip(),
    "APCA-API-SECRET-KEY": SECRET_KEY.strip(),
}

url = f"{BASE_URL.rstrip('/')}/v2/account"
print("Requesting:", url)

response = requests.get(url, headers=headers)
print("Status:", response.status_code)
print("Body:", response.text)

response.raise_for_status()

account = response.json()
print("✅ Alpaca connection successful")
print("Account status:", account.get("status"))
print("Cash available:", account.get("cash"))
