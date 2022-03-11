import requests
import os
from dotenv import load_dotenv

load_dotenv()
key = os.getenv('key')



def get_wather():

    url = 'http://api.openweathermap.org/data/2.5/weather?q=Minsk&APPID=' + key
    res = requests.get(url).json()
    sity = res['name']
    cor_temp = res['main']['temp'] - 273.15
    feel_like = res['main']['feels_like'] - 273.15
    condishn = res['weather'][0]['description']
    return f'сейчас в {sity}е {condishn}, температура {int(cor_temp)} градуса, ощущается как {int(feel_like)}'

