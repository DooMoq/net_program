from socket import *
import random

BUFF_SIZE = 1024
port = 5555
sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', port))
print('Listening...')

mailboxes = {}  

while True:
    data, addr = sock.recvfrom(BUFF_SIZE)
    data = (data.decode()).split(' ')
    
    if data[0] == 'send':
        mbox_id = data[1]
        msg = ' '.join(data[2:])  
        if mbox_id not in mailboxes:
            mailboxes[mbox_id] = []
        mailboxes[mbox_id].append(msg)
        sock.sendto('OK'.encode(), addr)

    elif data[0] == 'receive':
        mbox_id = data[1]
        if mbox_id in mailboxes and mailboxes[mbox_id]:
            msg = mailboxes[mbox_id].pop(0)
            sock.sendto(msg.encode(), addr)
        else:
            sock.sendto('No messages'.encode(), addr)
            
    elif data[0] == 'quit':
        break
