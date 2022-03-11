import requests
url = 'https://belarusbank.by/api/kursExchange/minsk'
res = requests.get(url).json()
def course ():
    buy_usd = res[0] ['USD_in']
    sell_usd = res[0]['USD_out']
    buy_eur = res[0] ['EUR_in']
    sell_eur = res[0] ['USD_out']
    buy_rus = res[0] ['RUB_in']
    sell_russ =res[0]  ['RUB_out']
    usd_eur_buy = res[0]['USD_EUR_in']
    usd_eur_sell = res[0]['USD_EUR_out']
    resul = f'Сегодня БеларусБанк установил следующие курсы\nUSD: {buy_usd}/ {sell_usd}\nEUR: {buy_eur}/ {sell_eur}\n' \
        f'RUB: {buy_rus}/ {sell_russ}\n_____________________\n'\
        f'конверсии покупка (USD/EUR) {usd_eur_buy}\n'\
        f'конверсии продажа (USD/EUR) {usd_eur_sell}'
    return resul



