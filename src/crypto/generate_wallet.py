from src.crypto.connect import *

#Генерация кошелька
acc_gen = w3.eth.account.create()
wallet = acc_gen._address
wallet_priv = acc_gen._private_key