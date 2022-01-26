import requests
from bs4 import BeautifulSoup
import csv
import os

url = 'https://auto.ria.com/newauto/marka-hyundai/'
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/94.0.4606.71 Safari/537.36',
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,'
           'application/signed-exchange;v=b3;q=0.9'}
FILE = 'cars.csv'

def get_html(url, params=None): # params нужен для доп параметров, например для доп страни браузера
    r = requests.get(url,headers=headers,params=params)
    return r

def get_pages (html):
    soup = BeautifulSoup(html, 'html.parser')
    pages = soup.find_all(class_='page-item mhide')
    if pages:
        return int(pages[-1].get_text())
    else:
        return 1


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser') #конструктор супа для работы с
    #создаются объекты python
    items = soup.find_all('div',class_ ='proposition_area')

    cars = []
    for item in items:
        prices = item.find(class_='proposition_price')
        if prices:
            prices= prices.get_text(strip=True).replace('•',' ')
        cars.append({
            'title':item.find(class_='proposition_title').get_text(strip=True),
            # 'link': item.find('a',class_='proposition_link').get('href'),
            'price_usd': prices,
            'city': item.find(class_='item region').get_text(strip=True)
        })
    return cars

def save (items, path):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['марка', 'цена', 'город'])#колонки ексель
        for item in items:
            writer.writerow([item['title'],item['price_usd'],item['city']])

def pars():
    url = input('ввеите адрес')

    html = get_html(url) #парсим 1ю страницу
    if html.status_code == 200:
        pages_count = get_pages(html.text)
        cars = []
        for page in range(1, pages_count + 1):
            print(f'парсинг страницы {page} из {pages_count}')
            html = get_html(url,params={'page':page}) #'page' с сайта
            cars.extend(get_content(html.text))
        save(cars,FILE)
        print(cars)
        print(f'получено {len(cars)} автомобилей')
        os.startfile(FILE)

        # cars = get_content(html.text)
    else:
        print('что-то не так')

pars()
