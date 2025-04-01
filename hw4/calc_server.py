from socket import *

def calculate(expr):
    try:
        expr = expr.replace(' ', '')
        if '+' in expr:
            a, b = expr.split('+')
            return str(int(a) + int(b))
        elif '-' in expr:
            a, b = expr.split('-')
            return str(int(a) - int(b))
        elif '*' in expr:
            a, b = expr.split('*')
            return str(int(a) * int(b))
        elif '/' in expr:
            a, b = expr.split('/')
            return format(int(a) / int(b), '.1f')
        else:
            return '미지원 연산'
    except:
        return '잘못된 수식'

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 3333))
s.listen(5)
print('waiting...')

while True:
    client, addr = s.accept()
    print('connection from', addr)
    while True:
        data = client.recv(1024)
        if not data:
            break
        expr = data.decode()
        result = calculate(expr)
        client.send(result.encode())
    client.close()
