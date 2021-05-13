from datetime import datetime

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
