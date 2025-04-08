
import socket
import random

def run_device_b():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 1002))
    s.listen(5)

    while True:
        c, addr = s.accept()
        data = c.recv(1024).decode().strip()
        if not data:
            c.close()
            continue
        
        if data == "Request":
            heartbeat = random.randint(40, 140)
            steps = random.randint(2000, 6000)
            cal = random.randint(1000, 4000)
            response = f"Heartbeat={heartbeat}, Steps={steps}, Cal={cal}"
            c.send(response.encode())
        elif data == "quit":
            c.send("Device B 종료".encode())
            c.close()
            break
        c.close()
    s.close()

if __name__ == '__main__':
    run_device_b()
