from socket import *

def determine_mime_type(file):
    if file.endswith(".html"):
        return "text/html; charset=utf-8"
    elif file.endswith(".png"):
        return "image/png"
    elif file.endswith(".ico"):
        return "image/x-icon"
    return "application/octet-stream"

server_socket = socket()
server_socket.bind(('', 80))
server_socket.listen(10)

while True:
    client_socket, client_address = server_socket.accept()
    
    request_data = client_socket.recv(1024)
    request_message = request_data.decode()
    
    lines = request_message.split('\r\n')
    
    if lines:
        request_line = lines[0]
        method, path, _ = request_line.split()
        file_name = path.lstrip('/')
        
        if file_name == "":
            file_name = "index.html"

        try:
            mime_type = determine_mime_type(file_name)
            if file_name.endswith(".html"):
                with open(file_name, 'r', encoding='utf-8') as file:
                    content = file.read()
                response_body = content.encode('utf-8')
            else:
                with open(file_name, 'rb') as file:
                    response_body = file.read()

            response_line = "HTTP/1.1 200 OK\r\n"
            response_headers = f"Content-Type: {mime_type}\r\n\r\n"
            response = response_line + response_headers
            client_socket.send(response.encode() + response_body)

        except Exception as e:
            print(f"파일을 찾을 수 없음: {file_name}, {e}")
            response_line = "HTTP/1.1 404 Not Found\r\n"
            response_headers = "\r\n"
            response_body = "<html><head><title>Not Found</title></head><body>Not Found</body></html>"
            response = response_line + response_headers + response_body
            client_socket.send(response.encode())

    client_socket.close()
