from src.bot import *
from src.defs import *
from src.admin.keyboards import *
from src.user.get_balance import *

#Узнать баланс пользователя
@dp.callback_query_handler(lambda call: call.data.startswith('check_bal_user'), state='*')
async def balik(call: types.CallbackQuery):
    await call.answer()
    state = dp.current_state(user=call.from_user.id)
    await state.set_state(States.CHECK_BAL_USER)
    await bot.send_message(call.from_user.id, "<b>Введите id пользователя для изменения баланса:</b>")

#Баланс(айди)
@dp.message_handler(state=States.CHECK_BAL_USER)
async def userka(message: types.Message):
    if message.text.isdigit():
        await message.answer(f"<b>Текущий баланс пользователя <code>{message.text}</code>\nUSD: <code>{price_to_human(balance_money(message.text))}</code>\nTON: <code>{price_to_human(balance_ton(message.text))}</code></b>")
        id_balance=message.text
    else:
        await message.answer("<b>Ошибка\nНажмите на кнопку ещё раз и введите число</b>")
    state = dp.current_state(user=message.from_user.id)
    await state.reset_state()