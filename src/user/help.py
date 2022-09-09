from src.bot import *

#Комманда help
@dp.message_handler(commands = ['help'], state='*')
async def help(message: types.Message):
    if message.from_user.id in admin_id:
        await message.answer("<b>Доступные команды:\n<code>/kf</code> - изменить курс(сумма на которую умножается реальный курс XRP)\nИспользование: <code>/kf</code> кэф(больше нуля)\n<code>/bal</code> - изменить баланс\nИспользование: <code>/bal</code> user id валюта(t- ton, u- usd) новое значение баланса\n<code>/help</code> - помощь</b>")
    else:
        await message.answer("Доступные команды:\n/help - помощь")