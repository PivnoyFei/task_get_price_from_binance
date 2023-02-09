import asyncio
from datetime import datetime

import aiohttp

from utils import Queue, check_price

URL = "https://api.binance.com/api/v3/ticker/price?symbol="


async def price(queue: Queue, currency: str) -> bool:
    """
    Тесты проходили в синхронном и асинхронном вариантах.
    Сравнивалась скорость четырех вариантов и все они показали
    примерно одинаковые результаты с погрешностью в 0.01с.
    Наилучший и более стабильный результат в 0.33 у aiohttp.
    """
    # response = requests.get(f"{URL}{currency}")  #  0.34c - 0.35c

    # http = Http()
    # response, content = http.request(f"{URL}{currency}") # 0.33c - 0.35c

    # manager = PoolManager(10)
    # response = manager.request("GET", f"{URL}{currency}") # 0.33c - 0.35c

    async with aiohttp.ClientSession() as session:
        async with session.get(f"{URL}{currency}") as response:
            if response.status == 200:
                r = await response.json()
                now_price = float(r["price"])
            else:
                print("== status_code ==", response.status)
                return False

    await check_price(queue, now_price, currency)
    return True


async def main(currencies: list[str]) -> None:
    prices = {i: Queue(datetime.now()) for i in currencies}

    while True:
        for currency in currencies:
            if not await price(prices[currency], currency):
                break


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(["XRPUSDT"]))
