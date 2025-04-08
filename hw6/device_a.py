
import socket
import random

def run_device_a():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 1001))
    s.listen(5)

    while True:
        c, addr = s.accept()
        data = c.recv(1024).decode().strip()
        if not data:
            c.close()
            continue
        
        if data == "Request":
            temp = random.randint(0, 40)
            humid = random.randint(0, 100)
            illum = random.randint(70, 150)
            response = f"Temp={temp}, Humid={humid}, Illum={illum}"
            c.send(response.encode())
        elif data == "quit":
            c.send("Device A 종료".encode())
            c.close()
            break
        c.close()
    s.close()

if __name__ == '__main__':
    run_device_a()
