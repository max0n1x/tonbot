from src.bot import *

#стартовые кнопки для пользователя
button1 = kb('💰Balance')
button2 = kb('📈Buy TON')
button3 = kb('🏦Deposit')
user_markup = ReplyKeyboardMarkup(resize_keyboard=True).add(
    button1, button2, button3
)

#депозит кнопки
keyprofile = InlineKeyboardMarkup(True)
keyprofile.add(InlineKeyboardButton('💳Deposit', callback_data='deposit'))

#проверка транзакции кнопки
keydeposit = InlineKeyboardMarkup(True)
keydeposit.add(InlineKeyboardButton('🔄Check', callback_data='check_bal'))

#покупка тон
buy = InlineKeyboardMarkup(True)
buy.add(InlineKeyboardButton('💵Buy', callback_data = 'buy_ton'))

#подтверждение покупки
auth = InlineKeyboardMarkup(True)
auth.add(InlineKeyboardButton('Yes', callback_data = 'yes_buy_ton'), InlineKeyboardButton('No', callback_data = 'no_buy_ton'))