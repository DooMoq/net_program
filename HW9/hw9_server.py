import socket
import select
import time

HOST = ''
PORT = 2500
server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_sock.bind((HOST, PORT))
server_sock.listen(5)
print("Server Started")


socket_list = [server_sock]

while True:
    read_sockets, _, _ = select.select(socket_list, [], [])

    for sock in read_sockets:
       
        if sock == server_sock:
            client_sock, addr = server_sock.accept()
            socket_list.append(client_sock)
            print(f"New client {addr}")
        else:
            try:
                data = sock.recv(1024)
                if not data:
                    raise ConnectionResetError  

                msg = data.decode().strip()
                if 'quit' in msg.lower():
                    print(f"{time.asctime()}{sock.getpeername()} exited")
                    socket_list.remove(sock)
                    sock.close()
                    continue

                print(f"{time.asctime()}{sock.getpeername()}:{msg}")
                
                for client in socket_list:
                    if client != server_sock and client != sock:
                        client.sendall(data)
            except:
                print(f"{time.asctime()}{sock.getpeername()} disconnected unexpectedly")
                socket_list.remove(sock)
                sock.close()