from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from util import log, money
from config import AMAZON_EMAIL, AMAZON_PASSWORD, PRICE_LIMIT

def amazon_purchase(ITEM_URL):
    try:
        options = Options()
        if len(config.CHROME_USER_DATA) > 0:
            options.add_argument('user-data-dir=' + config.CHROME_USER_DATA)
        browser = webdriver.Chrome(config.CHROME_DRIVER, chrome_options=options)
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
        try:
            browser.find_element_by_id('ap_password').send_keys(AMAZON_PASSWORD)
            log("Typed in password")
            sleep(0.1)
            browser.find_element_by_id('signInSubmit').click()
            log("Signing in")
            sleep(0.1)
        except:
            log('Already logged in')
            pass
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
