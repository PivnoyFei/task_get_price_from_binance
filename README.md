<h1 align="center"><a target="_blank" href="">task_get_price_from_binance</a></h1>

### Стек
![Python](https://img.shields.io/badge/Python-171515?style=flat-square&logo=Python)![3.11](https://img.shields.io/badge/3.11-blue?style=flat-square&logo=3.11)

## Заданиe: 

> Напишите код программы на Python, которая будет в реальном времени (с максимально возможной скоростью) считывать текущую цену фьючерса XRP/USDT на бирже Binance. 
В случае, если цена упала на 1% от максимальной цены за последний час, программа должна вывести сообщение в консоль. 
При этом программа должна продолжать работать дальше, постоянно считывая актуальную цену.


### Запуск проекта
Клонируем репозиторий и переходим в него:
```bash
gh clone https://github.com/PivnoyFei/task_get_price_from_binance
cd task_get_price_from_binance
```

#### Создаем и активируем виртуальное окружение:
```bash
python -m venv venv
source venv/Scripts/activate
```
#### Обновиляем pip и ставим зависимости из requirements.txt:
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### Запуск проекта main.py - реализован через api запросы, websocket.py - через websocket
```bash
python main.py
python websocket.py
```
