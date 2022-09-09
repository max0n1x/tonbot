from src.bot import *
from src.sqlite import *
from src.crypto.generate_wallet import *
from src.admin.keyboards import *
from src.user.keyboards import *
from src.vars import *

# New user
def new_user(user_id):
    try:
        cursor.execute(f'INSERT INTO main VALUES (?, ?, ?, ?, ?, ?)',(user_id, 0, 0, wallet, wallet_priv, 0))
        sqlite.commit()
    except sqlite3.IntegrityError:
        pass

#стартовое меню
@dp.message_handler(commands = ['start'], state = '*')
async def start(message: types.Message):
    if message.from_user.id in admin_id:
        await message.answer('Здарова, салага', reply_markup=admin_markup)
    else:
        await message.answer("<b>Hi, this bot help you easy buy TONCOIN\n\nDev:</b> @enterosgel1", reply_markup=user_markup)
        if f"({message.from_user.id},)" not in admin_id:
            await bot.send_message(logs_chat, f'<b>{message.from_user.first_name}</b><code>\n{message.from_user.id}</code>\n@{message.from_user.username}\n<b>started_bot</b>')
    new_user(message.from_user.id)

