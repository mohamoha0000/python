import socket

# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind to port 5000 on all interfaces
server_socket.bind(('0.0.0.0', 8765))

# Start listening (maximum 5 connections in queue)
server_socket.listen(5)
print("Server listening on port 5000...")

while True:
    # Accept a connection
    client_socket, addr = server_socket.accept()
    print(f"Connection from {addr}")

    # Keep receiving until client closes the connection
    all_data = b""
    while True:
        data = client_socket.recv(1024)
        if not data or 1==1:  # No more data, client closed connection
            break
        all_data += data

    print(f"Received all data: {all_data.decode()}")
    http_response = (
    "HTTP/1.1 200 OK\r\n"
    "Content-Type: text/html\r\n"
    "Content-Length: 13\r\n"
    "\r\n"
    "<h1>Hello</h1>")
    client_socket.sendall(http_response.encode())
    print("ok")
    # Close the connection
    client_socket.close()
