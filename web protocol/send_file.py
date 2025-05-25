# server.py
import socket

import os

from tqdm import tqdm


def recive(HOST,PORT,path):
    bin=b''
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)

    print(f"[+] Server listening on {HOST}:{PORT}")
    conn, addr = server_socket.accept()
    print(f"[+] Connected by {addr}")

    filesize = int(conn.recv(1024).decode())
    conn.send(b"OK")  # acknowledge

    received = 0
    with open(path, "wb") as f, tqdm(total=filesize, unit="B", unit_scale=True, desc="Downloading") as bar:
        while received < filesize:
            data = conn.recv(65536)
            if not data:
                break
            f.write(data)
            received += len(data)
            bar.update(len(data))
    conn.sendall("good".encode())
    conn.close()


def send(HOST,PORT,path):
    filesize = os.path.getsize(path)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    print(f"[+] Connected to server at {HOST}:{PORT}")
    client_socket.sendall(str(filesize).encode())
    ack = client_socket.recv(2)
    with open(path, "rb") as f, tqdm(total=filesize, unit="B", unit_scale=True, desc="Uploading") as bar:
        while True:
            chunk = f.read(65536)
            if not chunk:
                break
            client_socket.sendall(chunk)
            bar.update(len(chunk))
    data = client_socket.recv(1024).decode()
    print(f"Server replied: {data}")

    client_socket.close()


HOST="192.168.1.2"
PORT=3456
path=r"C:\Users\HP\Downloads\m\AIDE CMODs_3.2.200108.apk"
send(HOST,PORT,path)