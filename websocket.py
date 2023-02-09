import asyncio
import json
from datetime import datetime

from websockets import client

from utils import Queue, check_price

CURRENCIES = ["btcusdt", "ethusdt", "xrpusdt"]
URL = "wss://stream.binance.com:9443/stream?streams={0}@miniTicker"


async def websocket_activity(queue: Queue, currency: str) -> None:
    async with client.connect(URL.format(currency)) as websocket:
        while True:
            data = json.loads(await websocket.recv())["data"]
            now_price = float(data["c"])
            await check_price(queue, now_price, currency)

            import time
            event_time = time.localtime(data["E"] // 1000)
            print(
                {
                    "currency": data["s"],
                    "time": f"{event_time.tm_hour}:{event_time.tm_min}:{event_time.tm_sec}",
                    "price": float(data["c"]),
                }
            )


if __name__ == '__main__':
    tasks = [
        websocket_activity(Queue(datetime.now()), currency) for currency in CURRENCIES
    ]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(*tasks))
