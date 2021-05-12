import sys
import json
from amazon_buy_bot import *
import config

def read_in():
    lines = sys.stdin.readlines()
    return json.loads(lines[0])

def log(str):
    print("%s : %s" % (datetime.now().strftime("%Y/%m/%d %H:%M:%S"), str))

def money(number):
    number = number.strip('$')
    try:
        [num,dec]=number.rsplit('.')
        dec = int(dec)
        aside = str(dec)
        x = int('1'+'0'*len(aside))
        price = float(dec)/x
        num = num.replace(',','')
        num = int(num)
        price = num + price
    except:
        price = int(number)
    return price

def purchase(item_url):
    price = amazon.product_info(product_url=item_url)['body']['price']
    if price > config.PRICE_LIMIT:
        print('Price of {} is too high')
    else:
        print('Buying for price of {}')

    amazon.login(email=config.AMAZON_EMAIL, password=config.AMAZON_PASSWORD)
    amazon.buy(product_url=item_url)
    amazon.select_payment_method(payment_method=config.PAYMENT_METHOD)
    amazon.fill_cvv(cvv=config.CVV)
    amazon.place_order()

def main():
    data = read_in()
    brand, series, model, url = data['brand'], data['series'], data['model'], data['url']
    print('Notification: {} {} series {} at {}'.format(brand, model, series, url))
    purchase(url)

# Start process
if __name__ == '__main__':
    main()
