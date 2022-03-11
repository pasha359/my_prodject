import requests
import telebot
import random
from telebot import types
from exchrate import course
from get_pexels import download
from get_ip import get_ip
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('token')
key = os.getenv('key')

bot = telebot.TeleBot(token)

count = 0
number = random.randint(1, 10)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    sticker_id = 'CAACAgUAAxkBAAICsGFz0yJVoEPwuhWsM0LNPaU0-TlFAAJvAwAC6QrIA6_OvtkCul10IQQ'
    bot.send_sticker(message.chat.id, sticker_id)
    name = message.from_user.first_name
    tekst = f'привет {name}, я новый бот! Смотри что могу ;)'

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    itembtn1 = types.KeyboardButton('посмотреть погоду')
    itembtn2 = types.KeyboardButton('сыграть в игру')
    itembtn3 = types.KeyboardButton('текущие курсы')
    itembtn4 = types.KeyboardButton('получить открытку')
    itembtn5 = types.KeyboardButton('Чекнуть IP')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5)
    bot.send_message(message.chat.id, tekst, reply_markup=markup)


@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == 'посмотреть погоду':
            msg = bot.send_message(message.chat.id, 'Введите город')
            bot.register_next_step_handler(msg, user_sity)
        elif message.text == 'текущие курсы':
            bot.send_message(message.chat.id, course())
        elif message.text == 'сыграть в игру':
            bot.send_message(message.chat.id, f'сыграем в угадай число, которое от 1 до 10, у тебя 3 попытки')
            msg = bot.send_message(message.chat.id, 'Введите число')
            bot.register_next_step_handler(msg, digit_user)
        elif message.text == 'получить открытку':
            msg = bot.send_message(message.chat.id, 'укажи тему')
            bot.register_next_step_handler(msg, download)
        elif message.text == 'Чекнуть IP':
            msg = bot.send_message(message.chat.id, 'введите IP')
            bot.register_next_step_handler(msg, get_ip)

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

def digit_user(message):
    global count, number
    num = int(message.text)
    if count < 2:
        if num < number:
            msg = bot.send_message(message.chat.id, f'загаданное число больше {num}')
            bot.register_next_step_handler(msg, digit_user)
            count += 1
        elif num > number:
            msg = bot.send_message(message.chat.id, f'загаданное число меньше {num}')
            bot.register_next_step_handler(msg, digit_user)
            count += 1
        elif num == number:
            bot.send_message(message.chat.id, f'Победа! Угадал с {count} раз')
            sticker_id = 'CAACAgUAAxkBAAIJoGF7Gp70UZSoNsSLByQItDb7GpzmAAJuAwAC6QrIA3w0Dz_a7ARtIQQ'
            bot.send_sticker(message.chat.id, sticker_id)
            count = 0
    else:
        msg = bot.send_message(message.chat.id, 'попытки исчерпаны, вы проиграл')
        sticker_id = 'CAACAgIAAxkBAAIJnmF7GjI31S5qzDJnfyVL3Y6pH6qQAAIjAQACCaYCB1TWVSh5UUs7IQQ'
        bot.send_sticker(message.chat.id, sticker_id)
        count = 0



bot.polling(none_stop=True)
