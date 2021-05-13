import sys
import json

from amazon import amazon_purchase

def read_in():
    lines = sys.stdin.readlines()
    return json.loads(lines[0])

def main():
    data = read_in()
    brand, series, model, url = data['brand'], data['series'], data['model'], data['url']
    print('Notification: {} {} series {} at {}'.format(brand, model, series, url))
    if 'amazon.com' in url:
        amazon_purchase(url)

# Start process
if __name__ == '__main__':
    main()
