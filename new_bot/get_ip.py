import requests
import telebot
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('token')

bot = telebot.TeleBot(token)

def get_ip(message):
    ip = message.text
    try:
        url = f'http://ip-api.com/json/{ip}'
        r = requests.get(url).json()
        info = {
            'country': r['country'],
            'city':r['city'],
            'zip':r['zip'],
            'organization':r['org'],
            'query':r['query']
        }
        for key, value in info.items():
            result = f'{key} - {value}'
            bot.send_message(message.from_user.id, result)
    except KeyError:
        bot.send_message(message.from_user.id, 'Что-то пошло не так')




