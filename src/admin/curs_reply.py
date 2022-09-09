from src.bot import *
from src.admin.curs import *
#Курс
@dp.callback_query_handler(lambda call: call.data.startswith('admin_curs'), state='*')
async def kkurs(call: types.CallbackQuery):
    state = dp.current_state(user=call.from_user.id)
    await state.set_state(States.CURS)
    await bot.send_message(call.from_user.id, "<b>Сумма на которую умножается реальный курс XRP(прим. 0.1):</b>")

#Курс(кеф)
@dp.message_handler(state=States.CURS)
async def kef_ch(message: types.Message):
    if message.text.replace(".", "").isdigit():
        await message.answer("<b>Done\nНовый курс: <code>"+str(price(message.text))+"</code> USD/TON</b>")
    else:
        await message.answer("<b>Ошибка\nНажмите на кнопку ещё раз и введите число</b>")
    state = dp.current_state(user=message.from_user.id)
    await state.reset_state()