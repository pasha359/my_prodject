import requests

key = '563492ad6f9170000100000144badf34ab6e488798ce993ff6145bb0'



def get_wather():

    url = 'http://api.openweathermap.org/data/2.5/weather?q=Minsk&APPID=' + key
    res = requests.get(url)
    print(res.status_code)

get_wather()