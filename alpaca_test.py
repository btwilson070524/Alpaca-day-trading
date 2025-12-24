import os
import requests

API_KEY = os.getenv("ALPACA_API_KEY")
SECRET_KEY = os.getenv("ALPACA_SECRET_KEY")
BASE_URL = os.getenv("ALPACA_BASE_URL")

if not API_KEY or not SECRET_KEY or not BASE_URL:
    raise RuntimeError("Missing Alpaca environment variables")

headers = {
    "APCA-API-KEY-ID": API_KEY,
    "APCA-API-SECRET-KEY": SECRET_KEY
}

# Test account endpoint
response = requests.get(f"{BASE_URL}/v2/account", headers=headers)

if response.status_code != 200:
    raise RuntimeError(f"Alpaca connection failed: {response.text}")

account = response.json()

print("✅ Alpaca connection successful")
print("Account status:", account["status"])
print("Cash available:", account["cash"])
