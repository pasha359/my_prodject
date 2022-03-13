import requests
import telebot
import settings

bot = telebot.TeleBot(settings.bot_token)
key = settings.pexel_key


def download(message):
    quary = message.text

    header = {'Authorization':key}
    url = f"https://api.pexels.com/v1/search?query={quary}&per_page=1"
    r = requests.get(url, headers=header)
    new_r = r.json()
    if len(new_r.get('photos')) == 0:
        bot.send_message(message.from_user.id, 'не удалось найти по вашей категории')
    else:
        for i in new_r.get('photos'):
            res = i['src']['large2x']
            bot.send_message(message.from_user.id, res)




