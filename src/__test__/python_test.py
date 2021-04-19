import sys, json

def read_in():
    lines = sys.stdin.readlines()
    return json.loads(lines[0])

def main():
    data = read_in()
    print('Python script received data!')
    print(data['url'])

# Start process
if __name__ == '__main__':
    main()
