from src.bot import *
from src.sqlite import *
from src.defs import *
from src.user.keyboards import *
from src.admin.curs import *
from src.admin.keyboards import *

# Balance check
def balance_money(user_id):
    balance = cursor.execute(f'SELECT balance FROM main WHERE id = {user_id}').fetchone()[0]
    return balance

# Balance ton check
def balance_ton(user_id):
    balance_ton = cursor.execute(f'SELECT ton FROM main WHERE id = {user_id}').fetchone()[0]
    return balance_ton

#Запрос баланса
def balance(user_id):
    bal = balance_money(user_id)
    bal_ton = balance_ton(user_id)
    res = (f"<b>Your balance: <code>{price_to_human(bal)}</code> USD\nYour TON balance: <code>{price_to_human(bal_ton)}</code> TON\n\n<code>1</code> TON ≈ <code>{price_to_human(get_curs())}</code> USD\nApproximate cost: <code>{price_to_human(int(bal_ton*get_curs()/100))}</code> USD</b>")
    return res

#Запрос баланса
@dp.message_handler(lambda message: message.text == '💰Balance', state='*')
async def balance_check(message: types.Message):
    await message.answer(balance(message.from_user.id))