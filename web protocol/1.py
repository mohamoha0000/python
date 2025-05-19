import socket
import select
import threading
import random
client=[]
choice=[]
def handle_client(n,no):
    global client,choice
    try:
        request = client[n].recv(4096)
        if not request:
            return

        request_line = request.decode(errors="ignore").split('\n')[0]
        print(f"[Request] {request_line}")

        method, target, _ = request_line.split()
        if "googlevideo.com" in target:
            if no=="no":
                choice.append(target)
            else:
                target=random.choice(choice)
        # دعم HTTPS tunneling
        if method.upper() == "CONNECT":
            host, port = target.split(":")[0], int(target.split(":")[1])
            remote = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            remote.connect((host, port))

            # أخبر المتصفح أن النفق جاهز
            client[n].sendall(b"HTTP/1.1 200 Connection established\r\n\r\n")

            # تمرير البيانات بين العميل والخادم
            while True:
                ready, _, _ = select.select([client[n], remote], [], [])
                for sock in ready:
                    data = sock.recv(4096)
                    if not data:
                        return
                    (remote if sock is client[n] else client[n]).sendall(data)

        # دعم HTTP العادي
        elif "forever.com" in target :
            if target.startswith("http://"):
                target = target[len("http://"):]

            host = target.split('/')[0]

            html = "<h1 style='text-align:center;'>hi</h1>"
            response = (
                "HTTP/1.1 200 OK\r\n"
                "Content-Type: text/html\r\n"
                f"Content-Length: {len(html.encode())}\r\n"
                "Connection: close\r\n"
                "\r\n"
                f"{html}"
            )
            client[n].sendall(response.encode())
            client[n].close()
        else:
            # إذا طلب المتصفح رابط كامل مثل http://...
            if target.startswith("http://"):
                target = target[len("http://"):]

            host = target.split('/')[0]
            remote = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            remote.connect((host, 80))
            remote.sendall(request)

            # إعادة بيانات الخادم للعميل
            while True:
                data = remote.recv(4096)
                if not data:
                    break
                client[n].sendall(data)

            remote.close()


    except Exception as e:
        print(f"[Error] {e}")
    finally:
        client[n].close()


def start_proxy(host='0.0.0.0', port=8080):
    global client,choice
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((host, port))
    server.listen(100)
    print(f"Proxy listening on {host}:{port} ...")

    while True:
        no="ok"
        client_sock, addr = server.accept()
        client.append(client_sock)
        print(f"[Connected] {addr}")
        if "192.168.1.5" in addr:
            no="no"
        # لكل عميل نبدأ ثريد جديد لمعالجته
        t = threading.Thread(target=handle_client, args=(len(client)-1,no,))
        t.daemon = True
        t.start()


if __name__ == "__main__":
    start_proxy()
