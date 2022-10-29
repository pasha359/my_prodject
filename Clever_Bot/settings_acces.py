import os
from dotenv import load_dotenv
import telebot

load_dotenv()

bot = telebot.TeleBot(os.getenv('BOT_TOKEN'))
pixels_key = os.getenv('PEXELS_KEY')
weather_key = os.getenv('WETHER_KEY')

user_db = os.getenv('use_db')
password_db = os.getenv('password_db')
name_db = os.getenv('name_db')