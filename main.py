from src.bot import *
from src.admin.add_balance import *
from src.admin.curs_reply import *
from src.admin.add_balance_ton import *
from src.admin.add_balance_usd import *
from src.admin.admin_button import *
from src.admin.stats import *
from src.user.help import *
from src.user.new_user import *
from src.user.deposit import *
from src.user.buy_ton import *
from src.user.get_balance import *

#Цикл обработки всех сообщений
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)


