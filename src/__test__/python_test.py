import sys, json

def read_in():
    lines = sys.stdin.readlines()
    return json.loads(lines[0])

def main():
    data = read_in()
    brand, series, model, url = data['brand'], data['series'], data['model'], data['url']
    print('Notification: {} {} series {} at {}'.format(brand, model, series, url))

# Start process
if __name__ == '__main__':
    main()
