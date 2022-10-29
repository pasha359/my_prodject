import random

from keyboard import markup
from mashing_learning.mashing_learning import get_intent, get_response
from service_for_user.weather import user_city
from service_for_user.exchrate import course
from service_for_user.get_pexels import download
from db import save_user
from settings_acces import bot


@bot.message_handler(commands=['start'])
def send_welcome(message):
    name = message.from_user.first_name
    sticker_id = 'CAACAgUAAxkBAAICsGFz0yJVoEPwuhWsM0LNPaU0-TlFAAJvAwAC6QrIA6_OvtkCul10IQQ'
    bot.send_sticker(message.chat.id, sticker_id)
    text = f'привет {name}, я новый бот! Смотри что могу ;)'
    bot.send_message(message.chat.id, text, reply_markup=markup)
    save_user(name)#сохраняет пользователя


@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.text == 'посмотреть погоду':
        msg = bot.send_message(message.chat.id, 'Введите город')
        bot.register_next_step_handler(msg, user_city)

    elif message.text == 'текущие курсы':
        bot.send_message(message.chat.id, course())

    elif message.text == 'сыграть в игру':
        bot.send_message(message.chat.id, f'сыграем в угадай число, которое от 1 до 10, у тебя 3 попытки')
        msg = bot.send_message(message.chat.id, 'Введите число')
        bot.register_next_step_handler(msg, digit_user)

    elif message.text == 'получить открытку':
        msg = bot.send_message(message.chat.id, 'укажи тему')
        bot.register_next_step_handler(msg, download)

    elif message.text == 'поговорить c ботом':
        msg = bot.send_message(message.chat.id, f'Привет {message.from_user.first_name}, как ты?')
        bot.register_next_step_handler(msg, main_learning)


count = 1 # игра работает только при обявлении глобальной переменной
number = random.randint(1, 10)


def digit_user(message):
    global number, count
    try:
        num = int(message.text)
        if count < 3:
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
                count += 1
        else:
            msg = bot.send_message(message.chat.id, 'попытки исчерпаны, вы проиграли')
            sticker_id = 'CAACAgIAAxkBAAIJnmF7GjI31S5qzDJnfyVL3Y6pH6qQAAIjAQACCaYCB1TWVSh5UUs7IQQ'
            bot.send_sticker(message.chat.id, sticker_id)
            count = 0
    except ValueError:
        msg = bot.send_message(message.chat.id, 'вводите целое число')
        bot.register_next_step_handler(msg, digit_user)


def main_learning(message):
    text = message.text
    json_name = 'mashing_learning/intents_dataset.json'
    pkl_name = 'mashing_learning/model.pkl'
    intent = get_intent(text, json_name, pkl_name)
    answer = get_response(intent)
    msg = bot.send_message(message.chat.id, answer)
    bot.register_next_step_handler(msg, main_learning)


print('Bot online')
bot.polling(none_stop=True)
print('Bot offline')
