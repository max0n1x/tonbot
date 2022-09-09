from src.bot import *
from src.admin.keyboards import *

#Админка
@dp.message_handler(lambda message: message.text == '🚨Админка', state='*')
async def adminka(message: types.Message):
    if message.from_user.id in admin_id:
        await message.answer(f"<b>Функции администратора:</b>", reply_markup=admin_mar)
