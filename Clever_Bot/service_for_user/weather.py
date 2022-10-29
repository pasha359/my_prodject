import requests
from settings_acces import bot, weather_key


def user_city(message):
    city = message.text
    try:
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&APPID=' + weather_key
        res = requests.get(url).json()
        city = res['name']
        cor_temp = res['main']['temp'] - 273.15
        feel_like = res['main']['feels_like'] - 273.15
        condition = res['weather'][0]['description']
        result = f'сейчас в {city}е {condition}, температура {int(cor_temp)} градуса, ощущается как {int(feel_like)}'
        bot.send_message(message.from_user.id, result)
    except:
        bot.send_message(message.from_user.id, "Город " + city + " не найден")
        sticker_id = 'CAACAgUAAxkBAAIJoWF7GwMikpwmjRZq_-Aij7nQyMnAAAJ5AwAC6QrIA5Hag_iV9NWgIQQ'
        bot.send_sticker(message.chat.id, sticker_id)