from src.bot import *
from src.sqlite import *
from src.defs import *
from src.vars import *
from src.admin.curs import *

#Статистика
def stats():
    balance_all, ton_all = 0, 0
    res = cursor.execute(f'SELECT id FROM main').fetchall()
    users_all = len(res)
    res = cursor.execute(f'SELECT balance FROM main').fetchall()
    for i in res:
        balance_all += i[0]
    res = cursor.execute(f'SELECT ton FROM main').fetchall()
    for i in res:
        ton_all +=i [0]
    tt = f"<b>Всего пользователей: <code>{users_all}</code>\nВсего баланса: <code>{price_to_human(balance_all)}</code> руб\nВсего TON: <code>{price_to_human(ton_all)}</code> TON\nКурс: <code>{price_to_human(get_curs())}</code> руб/монета </b>"
    return tt

#Стата
@dp.message_handler(lambda message: message.text == '📊Статистика', state = '*')
async def stata(message: types.Message):
    await message.answer(stats())
