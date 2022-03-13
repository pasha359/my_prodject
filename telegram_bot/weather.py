import requests
import telebot
import settings

bot = telebot.TeleBot(settings.bot_token)
key = settings.weayher_key

def user_sity (message):
    sity = message.text
    try:
        url = f'http://api.openweathermap.org/data/2.5/weather?q={sity}&APPID=' + key
        res = requests.get(url).json()
        sity = res['name']
        cor_temp = res['main']['temp'] - 273.15
        feel_like = res['main']['feels_like'] - 273.15
        condishn = res['weather'][0]['description']
        result = f'сейчас в {sity}е {condishn}, температура {int(cor_temp)} градуса, ощущается как {int(feel_like)}'
        bot.send_message(message.from_user.id, result)
    except:
        bot.send_message(message.from_user.id, "Город " + sity + " не найден")
        sticker_id = 'CAACAgUAAxkBAAIJoWF7GwMikpwmjRZq_-Aij7nQyMnAAAJ5AwAC6QrIA5Hag_iV9NWgIQQ'
        bot.send_sticker(message.chat.id, sticker_id)