from src.bot import *
from src.defs import *
from src.sqlite import *
from src.admin.keyboards import *
from src.admin.add_balance import *

#Добавление баланса тон
def add_balance_ton(val):
    id_balance = azaza()
    res = cursor.execute(f'SELECT ton FROM main WHERE id = {id_balance}').fetchone()[0]
    if val.startswith('+'):
        val = val.replace('+', '')
        val = res+int(val)
        cursor.execute(f'UPDATE main SET ton = {val} WHERE id = {id_balance}')
        sqlite.commit()
    elif val.startswith('-'):
        val = val.replace('-', '')
        val = res-int(val)
        cursor.execute(f'UPDATE main SET ton = {val} WHERE id = {id_balance}')
        sqlite.commit()
    elif val.replace("+", "").replace("-", "").isdigit():
        cursor.execute(f'UPDATE main SET ton = {val} WHERE id = {id_balance}')
        sqlite.commit()  
    return price_to_human(val)

#Добавление баланс(TON)
@dp.callback_query_handler(lambda call: call.data.startswith('ton_bal_change'), state='*')
async def pashalka(call: types.CallbackQuery):
    await call.answer()
    state = dp.current_state(user=call.from_user.id)
    await state.set_state(States.AMOUNT_TON)
    await bot.send_message(call.from_user.id, "<b>Введите сумму(прим. <code>+1488</code> - добавить, <code>-1488</code> - отнять, <code>1488</code> - переписать):</b>")

#Баланс(сумма TON)
@dp.message_handler(state=States.AMOUNT_TON)
async def sumka(message: types.Message):
    if message.text.replace("+", "").replace("-", "").isdigit():
        await message.answer(f"<b>Done\nНовый баланс: <code>{add_balance_ton(message.text)}</code> TON</b>", reply_markup=admin_markup)
    else:
        await message.answer("<b>Ошибка\nНажмите на кнопку ещё раз и введите число</b>")
    state = dp.current_state(user=message.from_user.id)
    await state.reset_state()