import sys
import json
from time import sleep
from datetime import datetime
from selenium import webdriver

from config import AMAZON_EMAIL, AMAZON_PASSWORD, PRICE_LIMIT

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

def purchase(ITEM_URL):
    try:
        browser = webdriver.Chrome('.\chromedriver.exe')
        browser.get(ITEM_URL)
        log('Visiting {}'.format(ITEM_URL))
        sleep(0.1)
    except:
        log('Failed to open browser.')
        exit()

    # Add to cart
    browser.find_element_by_id('add-to-cart-button').click()
    log('Adding to cart')
    sleep(0.1)

    # Proceed to checkout
    browser.get('https://www.amazon.com/gp/cart/view.html?ref_=nav_cart')
    browser.find_element_by_name('proceedToRetailCheckout').click()
    log('Proceeding to checkout')
    sleep(0.1)

    # Log in
    try:
        browser.find_element_by_id('ap_email').send_keys(AMAZON_EMAIL)
        log("Typed in email address")
        sleep(0.1)
        browser.find_element_by_id('continue').click()
        log("Continuing")
        sleep(0.1)
        browser.find_element_by_id('ap_password').send_keys(AMAZON_PASSWORD)
        log("Typed in password")
        sleep(0.1)
        browser.find_element_by_id('signInSubmit').click()
        log("Signing in")
        sleep(0.1)
    except:
        log('Already logged in')
        pass

    # Say no to Amazon Prime free trial
    # try:
    #     browser.find_element_by_css_selector('a.prime-nothanks-button').click()
    #     log('No thanks to Amazon Prime free trial')
    # except:
    #     pass

    # Validate price
    price_txt = browser.find_element_by_css_selector('td.grand-total-price').text
    log('Price is {}'.format(price_txt))
    if money(price_txt) > PRICE_LIMIT:
        log('Price is too high, clearing cart')
        browser.get('https://www.amazon.com/gp/cart/view.html?ref_=nav_cart')
        sleep(0.1)
        browser.find_element_by_css_selector('.sc-action-delete input[value*=Delete]').click()
        return

    # Place order
    browser.find_element_by_name('placeYourOrder1').click()
    log('Placed order')
    sleep(5)

def main():
    data = read_in()
    brand, series, model, url = data['brand'], data['series'], data['model'], data['url']
    print('Notification: {} {} series {} at {}'.format(brand, model, series, url))
    purchase(url)

# Start process
if __name__ == '__main__':
    main()
