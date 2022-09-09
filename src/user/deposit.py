from src.bot import *
from src.crypto.connect import *
from src.sqlite import *
from src.vars import *
from src.defs import *
from src.time import *
from src.crypto.bnb_price import *
from src.user.keyboards import *
from src.admin.keyboards import *

#Получение реквизитов для депа
def deposit(user_id):
    req = cursor.execute('SELECT wallet_pub FROM main WHERE id = ?', [user_id]).fetchone()
    temp_price = bnb_price - 1000
    text = f'<b>💳Your wallet address:\n</b> <code>{req[0]}</code>' \
           '\nToken: <b>BNB BEP-20</b>' \
           '\nNetwork: <b>BNB Smart Chain</b>' \
           '\nMinimal amount of deposit:' \
           f'\n<b>{price_to_human(minimal_amount)} USD/{round(minimal_amount / temp_price, 6)} BNB</b>' \
           f'\n\n<code>Rates 1 BNB ~ {round(temp_price / 100, 2)} USD</code>'
    return text

#Сокращаю говно(Да-да это всё один реплай просто разбит сюда чтобы не срать в мейне)
def a1(user_id):
    global wallet_bal, wallet_pub, wallet_private, balance1
    req = cursor.execute('SELECT wallet_pub, wallet_priv, balance, pause_time FROM main WHERE id = ?',[user_id]).fetchone()
    wallet_pub = req[0]
    wallet_private = req[1]
    balance1 = req[2]
    pause_time = req[3]
    wallet_bal = w3.eth.getBalance(wallet_pub)
    return pause_time, wallet_bal
def a2(user_id):
    global wallet_bal, balance1
    received = int(w3.fromWei(wallet_bal, 'ether') * bnb_price)
    text = f'<b>💰You have received</b> <code>{price_to_human(received)} USD</code>'
    cursor.execute('UPDATE main SET balance = ?, pause_time = ? WHERE id = ?',[balance1 + received, tCurrent() + 300, user_id])
    sqlite.commit()
    return text
def a3():
    global wallet_pub, wallet_private
    value = wallet_bal - w3.toWei(gas_price, 'gwei') * 21000
    tx = {
        'nonce': w3.eth.getTransactionCount(wallet_pub),
        'to': withdraw_address,
        'value': value,
        'gas': 21000,
        'gasPrice': w3.toWei(gas_price, 'gwei')
    }
    signed_tx = w3.eth.account.sign_transaction(tx, wallet_private)
    tx_hash = w3.toHex(w3.eth.send_raw_transaction(signed_tx.rawTransaction))
    tx_hash = f'Transaction hash:\n<code>{tx_hash}</code>'
    withdrawn = w3.fromWei(wallet_bal - w3.toWei(6, "gwei") * 21000, "ether")
    total_received = f'Value:\n<code>{withdrawn} BNB</code>'
    return tx_hash, total_received

#Депозит
@dp.callback_query_handler(lambda call: call.data.startswith('deposit'), state='*')
async def deposit_busd(call: types.CallbackQuery):
    await call.message.answer(deposit(call.from_user.id), reply_markup=keydeposit)
    return await call.answer()

#Проверка депозита
@dp.callback_query_handler(lambda call: call.data.startswith('check_bal'), state='*')
async def checkdep(call: types.CallbackQuery):
    req = a1(call.from_user.id)
    pause_time = req[0]
    wallet_bal = req[1]
    if tCurrent() < pause_time:
        await call.answer('Wait 5 minutes before next checking')
    elif wallet_bal >= w3.toWei(minimal_amount / bnb_price, 'ether'):
        text=a2(call.from_user.id)
        if call.from_user.id in admin_id:
            await bot.edit_message_text(message_id=call.message.message_id, chat_id=call.from_user.id, text=text, reply_markup=admin_markup)
        else:
            await bot.edit_message_text(message_id=call.message.message_id, chat_id=call.from_user.id, text=text, reply_markup=user_markup)
        await call.answer()
        await sleep(30)
        req = a3()
        tx_hash = req[0]
        total_received = req[1]
        await bot.send_message(logs_chat, f'<b>Withdrawal successful!</b>\n{total_received}\n{tx_hash}')
    else:
        await call.answer('You have not received any money')

#Депозит
@dp.message_handler(lambda message: message.text == '🏦Deposit', state='*')
async def balance_dep(message: types.Message):
    await message.answer(f"<b>Deposit BNB:</b>", reply_markup=keyprofile)
