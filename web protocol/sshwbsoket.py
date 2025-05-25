import socket
import threading

# إعدادات الخادم
LISTEN_HOST = '0.0.0.0'
LISTEN_PORT = 8880  # المنفذ الذي يستقبل بايلود WebSocket
SSH_HOST = '127.0.0.1'
SSH_PORT = 22       # منفذ SSH في جهازك

# الرد الخاص بالـ Handshake WebSocket
WS_HANDSHAKE_RESPONSE = (
    "HTTP/1.1 101 Switching Protocols\r\n"
    "Upgrade: websocket\r\n"
    "Connection: Upgrade\r\n"
    "\r\n"
)

def handle_client(client_socket):
    try:
        http_response = (
        "HTTP/1.1 200 OK\r\n"
        "Content-Type: text/plain\r\n"
        "Content-Length: 13\r\n"
        "\r\n"
        "Hello, world!")
        # استقبال البيانات الأولى (handshake)
        request = client_socket.recv(1024).decode(errors='ignore')
        print(request.lower())
        if "ebsocket" not in request.lower():
            client_socket.send(http_response.encode())
            client_socket.close()
            return
        # إرسال رد WebSocket Handshake
        client_socket.send(WS_HANDSHAKE_RESPONSE.encode())

        # الاتصال بخادم SSH
        ssh_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ssh_socket.connect((SSH_HOST, SSH_PORT))

        # دالة لتحويل البيانات بين الطرفين
        def forward(src, dst):
            try:
                while True:
                    data = src.recv(4096)
                    if not data:
                        break
                    dst.sendall(data)
            except:
                pass
            finally:
                src.close()
                dst.close()

        # إطلاق ثريدات لنقل البيانات في كلا الاتجاهين
        threading.Thread(target=forward, args=(client_socket, ssh_socket)).start()
        threading.Thread(target=forward, args=(ssh_socket, client_socket)).start()

    except Exception as e:
        print("خطأ:", e)
        client_socket.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((LISTEN_HOST, LISTEN_PORT))
    server.listen(100)
    print(f"🚀 الخادم يعمل على {LISTEN_HOST}:{LISTEN_PORT} وينقل لـ SSH في {SSH_HOST}:{SSH_PORT}")

    while True:
        client_socket, addr = server.accept()
        print("con")
        threading.Thread(target=handle_client, args=(client_socket,)).start()

if __name__ == '__main__':
    start_server()



"ssh -R 80:127.0.0.1:8880 serveo.net"

#https://chatgpt.com/share/682c7013-46fc-8004-b3b1-56a6a7b04f22
#cloudflared tunnel --url http://localhost:8880
#.\cloudflared tunnel --url http://localhost:8880