import requests as r

#Проверка курса
req = r.get('https://api.binance.com/api/v3/ticker/price?symbol=BNBUSDT')
bnb_price = int(req.json()['price'].replace('.', '')[:-6])