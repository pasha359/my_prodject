from telebot import types


markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton('посмотреть погоду')
btn2 = types.KeyboardButton('сыграть в игру')
btn3 = types.KeyboardButton('текущие курсы')
btn4 = types.KeyboardButton('получить открытку')
btn5 = types.KeyboardButton('поговорить c ботом')
markup.add(btn1, btn2, btn3, btn4, btn5)
