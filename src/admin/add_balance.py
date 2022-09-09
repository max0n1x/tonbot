from src.bot import *
from src.defs import *
from src.admin.keyboards import *
from src.user.get_balance import *

id_balance = 0

def azaza():
    return id_balance

#Работа с балансом
@dp.callback_query_handler(lambda call: call.data.startswith('admin_bal'), state='*')
async def balik(call: types.CallbackQuery):
    await call.answer()
    state = dp.current_state(user=call.from_user.id)
    await state.set_state(States.USER_ID)
    await bot.send_message(call.from_user.id, "<b>Введите id пользователя для изменения баланса:</b>")

#Баланс(айди)
@dp.message_handler(state=States.USER_ID)
async def userka(message: types.Message):
    global id_balance
    if message.text.isdigit():
        await message.answer(f"<b>Текущий баланс пользователя <code>{message.text}</code>\nUSD: <code>{price_to_human(balance_money(message.text))}</code>\nTON: <code>{price_to_human(balance_ton(message.text))}</code>\nВыберите валюту:</b>", reply_markup=valuta)
        id_balance=message.text
    else:
        await message.answer("<b>Ошибка\nНажмите на кнопку ещё раз и введите число</b>")
    state = dp.current_state(user=message.from_user.id)
    await state.reset_state()