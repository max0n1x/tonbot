import requests as r
from src.bot import *
from src.defs import *
from src.sqlite import *

curs = 100
cursor.execute(f'INSERT INTO money (curs) VALUES ({curs})')
sqlite.commit()

#Изменение курса путём коэффициента
def price(kf):
    curs = 100
    curs = int(round(float(r.get("https://api.binance.com/api/v3/ticker/price?symbol=XRPUSDT").json()["price"])*float(kf), 2)*100)
    cursor.execute(f'UPDATE money SET curs = {curs}')
    sqlite.commit()
    return price_to_human(curs)

def get_curs():
    res=cursor.execute(f'SELECT curs FROM money').fetchone()[0]
    return res
