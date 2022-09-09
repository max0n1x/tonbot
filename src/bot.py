from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton as kb
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from src.config import *
import sys

#Крутие импорты
sys.path.append('/Users/zxc/Desktop/projects/tonbot')

#Бот
bot = Bot(token=config.get('bot', 'token'), parse_mode='html')
dp = Dispatcher(bot, storage=MemoryStorage())

#Cостояния
class States(StatesGroup):
    AMOUNT = State()
    CURS = State()
    USER_ID = State()
    AMOUNT_USD = State()
    AMOUNT_TON = State()

