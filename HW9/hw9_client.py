import socket
import threading

def recv_handler(sock):
    while True:
        try:
            msg = sock.recv(1024)
            if not msg:
                break
            print("\n" + msg.decode())
        except:
            break

server_addr = ('localhost', 2500)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(server_addr)

my_id = input("ID를 입력하세요: ")
sock.sendall(f"[{my_id}]".encode())


thread = threading.Thread(target=recv_handler, args=(sock,))
thread.daemon = True
thread.start()


while True:
    msg = input()
    if msg.lower() == 'quit':
        sock.sendall('quit'.encode())
        break
    full_msg = f"[{my_id}] {msg}"
    sock.sendall(full_msg.encode())

sock.close()