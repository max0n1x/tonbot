from configparser import ConfigParser

#Конфиг
config = ConfigParser()
config.read('config.ini')
admin_id = list(map(int, config.get('bot', 'admin_id').replace(" ", "").split(",")))