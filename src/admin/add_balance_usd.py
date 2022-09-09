from src.bot import *
from src.defs import *
from src.sqlite import *
from src.admin.keyboards import *

#Добавление баланса usd
def add_balance_usd(val):
    global id_balance
    res=cursor.execute(f'SELECT balance FROM main WHERE id = {id_balance}').fetchone()[0]
    if val.startswith('+'):
        val = val.replace('+', '')
        val=res+int(val)
        cursor.execute(f'UPDATE main SET balance = {val} WHERE id = {id_balance}')
        sqlite.commit()
    elif val.startswith('-'):
        val = val.replace('-', '')
        val = res-int(val)
        cursor.execute(f'UPDATE main SET balance = {val} WHERE id = {id_balance}')
        sqlite.commit()
    elif val.replace('-', '').replace('+', '').isdigit():
        cursor.execute(f'UPDATE main SET balance = {val} WHERE id = {id_balance}')
        sqlite.commit()
    return price_to_human(val)

#Добавление баланс(USD)
@dp.callback_query_handler(lambda call: call.data.startswith('usd_bal_change'), state='*')
async def pashalka(call: types.CallbackQuery):
    state = dp.current_state(user=call.from_user.id)
    await state.set_state(States.AMOUNT_USD)
    await bot.send_message(call.from_user.id, "<b>Введите сумму(прим. <code>+1488</code> - добавить, <code>-1488</code> - отнять, <code>1488</code> - переписать):</b>")

#Баланс(сумма USD)
@dp.message_handler(state=States.AMOUNT_USD)
async def sumka(message: types.Message):
    if message.text.replace("+", "").replace("-", "").isdigit():
        await message.answer(f"<b>Done\nНовый баланс: <code>{add_balance_usd(message.text)}</code> USD</b>", reply_markup=admin_markup)
    else:
        await message.answer("<b>Ошибка\nНажмите на кнопку ещё раз и введите число</b>")
    state = dp.current_state(user=message.from_user.id)
    await state.reset_state()