from src.bot import *
from src.crypto.connect import *
from src.sqlite import *
from src.vars import *
from src.defs import *
from src.time import *
from src.crypto.bnb_price import *
from src.user.keyboards import *
from src.user.get_balance import *
from src.admin.curs import *
from src.admin.keyboards import *

#покупка тон(финал)
def buy_ton2(user_id, amount):
    req = cursor.execute('SELECT balance, ton FROM main WHERE id = ?',[user_id]).fetchone()
    balance1 = req[0]
    ton = req[1]
    if balance1 >= amount * get_curs() / 100:
        balance1 -= amount * get_curs() / 100
        ton += amount
        cursor.execute('UPDATE main SET balance = ?, ton = ? WHERE id = ?', [balance1, ton, user_id])
        sqlite.commit()
        text = f'<b>You bought {price_to_human(amount)} TON for {price_to_human(int(amount * get_curs() / 100))} USD</b>'
        return text
    else:
        text = False
        return text

#покупка тон(подтверждение)
def buy_ton1(user_id, amount):
    req = cursor.execute('SELECT balance, ton FROM main WHERE id = ?',[user_id]).fetchone()
    balance1 = req[0]
    ton = req[1]
    if balance1 >= amount * get_curs() / 100:
        text = f'<b>Are you sure you want to buy {amount} TON for {price_to_human(int(amount * get_curs()))} USD?</b>'
        return text
    else:
        text = False
        return text

#Покупка монет
@dp.message_handler(lambda message: message.text == '📈Buy TON', state='*')
async def buy_ton(message: types.Message):
    await message.answer(f"<b>Buy TON</b>\n\n<b>Balance:</b> <code>{price_to_human(balance_money(message.from_user.id))}</code> USD\n<b>Balance TON:</b> <code>{price_to_human(balance_ton(message.from_user.id))}</code> TON\n\n<code>1</code> <b>TON</b> ≈ <code>{price_to_human(get_curs())}</code> USD", reply_markup=buy)

#Покупка монет(кнопка)
@dp.callback_query_handler(lambda call: call.data.startswith('buy_ton'), state='*')
async def keyton(call: types.CallbackQuery):
    state = dp.current_state(user=call.from_user.id)
    await state.set_state(States.AMOUNT)
    await bot.send_message(call.from_user.id, "<b>Enter the amount of TON you want to buy:</b>")

#Покупка монет(количество)
@dp.message_handler(state=States.AMOUNT)
async def amount_state(message: types.Message):
    if message.text.isdigit():
        if int(message.text) > 0:
            if buy_ton1(message.from_user.id, int(message.text)) != False:
                await message.reply(buy_ton1(message.from_user.id, int(message.text)), reply_markup=auth)
            else:
                await message.answer("<b>You do not have enough money</b>")
        else:
            await message.answer("<b>Enter correct amount</b>")
    state = dp.current_state(user=message.from_user.id)
    await state.reset_state()
    
#Покупка монет(да)
@dp.callback_query_handler(lambda call: call.data.startswith('yes_buy_ton'), state='*')
async def buy_ton_yes(call: types.CallbackQuery):
    await bot.send_message(call.from_user.id, buy_ton2(call.from_user.id, int(call.message.text.split(' ')[-2].replace('.', ''))), reply_markup=auth)

#Покупка монет(нет)
@dp.callback_query_handler(lambda call: call.data.startswith('no_buy_ton'), state='*')
async def buy_ton_no(call: types.CallbackQuery):
    if call.from_user.id in admin_id:
        await bot.send_message(call.from_user.id, "No", reply_markup=admin_markup)
    else:
        await bot.send_message(call.from_user.id, "Purchase canceled", reply_markup=user_markup)