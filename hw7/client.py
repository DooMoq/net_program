from socket import *
import random
BUFF_SIZE = 1024
port = 5555
sock = socket(AF_INET, SOCK_DGRAM)
sock.connect(('localhost',port))

while True:
    data = input('Enter the message("send [mboxID] message") or ("receive [mboxID]") : ')
    if data == 'quit':
        sock.send(data.encode())
        break
    
    elif data.split(' ')[0] == 'send':
        sock.send(data.encode())
        msg = sock.recv(BUFF_SIZE).decode() 
        print(msg)
        
    elif data.split(' ')[0] == 'receive':
        sock.send(data.encode())
        msg = (sock.recv(BUFF_SIZE)).decode()
        print(msg)