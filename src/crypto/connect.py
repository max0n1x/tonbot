from web3 import Web3, HTTPProvider
from web3.middleware import geth_poa_middleware
from src.config import *

#Сеть
w3 = Web3(HTTPProvider(config.get('crypto', 'network_url')), middlewares=[geth_poa_middleware])


