from src.bot import *

#стартовые кнопки для админа
button1 = kb('💰Balance')
button2 = kb('📈Buy TON')
button3 = kb('🏦Deposit')
button4 = kb('📊Статистика')
button5 = kb('🚨Админка')
admin_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(
    button1, button2, button3, button4, button5
)

#кнопки админка
admin_mar = InlineKeyboardMarkup(True)
admin_mar.add(InlineKeyboardButton('Изменить баланс', callback_data = 'admin_bal'), InlineKeyboardButton('Изменить курс', callback_data = 'admin_curs'))

#выбор валюты изменения баланса
valuta = InlineKeyboardMarkup(True)
valuta.add(InlineKeyboardButton('TON', callback_data = 'ton_bal_change'), InlineKeyboardButton('USD', callback_data = 'usd_bal_change'))