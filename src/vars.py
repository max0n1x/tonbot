from src.config import *

#Говно
wallet_bal = 0
wallet_pub, wallet_private, balance1 = 0, 0, 0
logs_chat = config.get('bot', 'logs_id')
withdraw_address = config.get('crypto', 'withdraw_address')
minimal_amount = int(config.get('crypto', 'minimal_amount'))
gas_price = config.get('crypto', 'gas_price')
admin_id = list(map(int, config.get('bot', 'admin_id').replace(" ", "").split(",")))