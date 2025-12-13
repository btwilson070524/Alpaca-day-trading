import alpaca_trade_api as tradeapi
import pandas as pd
import time
import os

API_KEY = os.getenv("APCA_API_KEY_ID")
SECRET_KEY = os.getenv("APCA_API_SECRET_KEY")
BASE_URL = "https://paper-api.alpaca.markets"

api = tradeapi.REST(API_KEY, SECRET_KEY, BASE_URL)

SYMBOL = "AAPL"
QTY = 1
MAX_TRADES_PER_DAY = 3
trades_today = 0

def get_bars():
    return api.get_bars(SYMBOL, tradeapi.TimeFrame.Minute, limit=20).df

while True:
    try:
        if trades_today >= MAX_TRADES_PER_DAY:
            time.sleep(300)
            continue

        bars = get_bars()
        last_close = bars.close.iloc[-1]
        high_5 = bars.high.tail(5).max()
        volume_spike = bars.volume.iloc[-1] > bars.volume.tail(10).mean() * 2

        positions = [p.symbol for p in api.list_positions()]
        in_position = SYMBOL in positions

        if not in_position and last_close > high_5 and volume_spike:
            api.submit_order(
                symbol=SYMBOL,
                qty=QTY,
                side="buy",
                type="market",
                time_in_force="day"
            )
            trades_today += 1

        time.sleep(60)

    except Exception as e:
        print(e)
        time.sleep(60)
