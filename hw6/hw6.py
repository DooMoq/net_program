import socket
import time

def request_device(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('localhost', port))
    s.send("Request".encode())
    data = s.recv(1024).decode()
    s.close()
    return data

def send_quit(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('localhost', port))
    s.send("quit".encode())
    data = s.recv(1024).decode()
    s.close()

def main():
    device_a_port = 1001
    device_b_port = 1002
    data_file = "data.txt"
    
    device_a_count = 0
    device_b_count = 0
    
    # 데이터 수집 횟수를 5번 이상으로 설정
    while device_a_count < 5 or device_b_count < 5:
        cmd = input("Enter 1 (Device A), 2 (Device B), or quit: ").strip()
        
        if cmd == "1" and device_a_count < 5:
            result = request_device(device_a_port)
            timestamp = time.ctime()
            log_line = f"{timestamp}: Device A: {result}\n"
            with open(data_file, "a", encoding="utf-8") as f:
                f.write(log_line)
            device_a_count += 1
            print(f"Device A 데이터 수집 완료 ({device_a_count}/5)")
        
        elif cmd == "2" and device_b_count < 5:
            result = request_device(device_b_port)
            timestamp = time.ctime()
            log_line = f"{timestamp}: Device B: {result}\n"
            with open(data_file, "a", encoding="utf-8") as f:
                f.write(log_line)
            device_b_count += 1
            print(f"Device B 데이터 수집 완료 ({device_b_count}/5)")

        elif cmd.lower() == "quit":
            send_quit(device_a_port)
            send_quit(device_b_port)
            break

        else:
            print("Invalid input.")
        
        # 10개 데이터가 채워지면 종료 조건
        if device_a_count >= 5 and device_b_count >= 5:
            print("모든 데이터를 수집했습니다.")
            break

if __name__ == '__main__':
    main()
