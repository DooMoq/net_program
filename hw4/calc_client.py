from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 3333))

while True:
    msg = input('연산 식 입력 ex) 20+17, 또는 q 로 종료 : ')
    if msg.lower() == 'q':
        break
    s.send(msg.encode())
    result = s.recv(1024).decode()
    print('결과 :', result)

s.close()
