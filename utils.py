from collections import deque
from datetime import datetime, timedelta


class Queue:
    def __init__(self, target: datetime) -> None:
        self.target = target
        self.prices_list: deque[float] = deque([])
        self.data_list: deque[datetime] = deque([])

    @property
    async def last_price(self) -> float:
        return self.prices_list[0]

    @property
    async def last_data(self) -> datetime:
        return self.data_list[0]

    @property
    async def max_price(self) -> float:
        return max(self.prices_list)

    async def add(self, now: float) -> None:
        self.prices_list.append(now)
        self.data_list.append(datetime.now())

    @property
    async def pop(self) -> None:
        self.prices_list.popleft()
        self.data_list.popleft()


async def check_price(queue: Queue, now_price: float, currency: str) -> None:
    await queue.add(now_price)
    max_price = await queue.max_price
    changes = (max_price - now_price) / max_price * 100

    if changes > 1 and queue.target < datetime.now():
        print(
            f"Цена {currency} снизилась на {round(changes, 3)}% "
            f"от максимальной цены {max_price} до {now_price}."
        )
        queue.target = datetime.now() + timedelta(hours=1)

    if await queue.last_data + timedelta(hours=1) < datetime.now():
        await queue.pop
