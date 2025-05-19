import socket
import select
import threading
import random
import re

client_connections = []
watched_videos = []

def modify_request(request, new_target):
    """تعديل الطلب لاستبدال عنوان الفيديو"""
    lines = request.decode('utf-8', errors='ignore').split('\n')
    first_line = lines[0].split()
    if len(first_line) >= 3:
        first_line[1] = new_target
        lines[0] = ' '.join(first_line)
    
    # إصلاح عنوان Host في الرأس
    modified_request = []
    for line in lines:
        if line.lower().startswith('host:'):
            host = new_target.split('/')[2].split(':')[0]
            line = f"Host: {host}"
        modified_request.append(line)
    
    return '\n'.join(modified_request).encode('utf-8')

def handle_client(client_sock, addr, is_special_client):
    global watched_videos
    try:
        request = client_sock.recv(4096)
        if not request:
            return

        request_line = request.decode(errors="ignore").split('\n')[0]
        print(f"[Request from {addr[0]}] {request_line}")

        parts = request_line.split()
        if len(parts) < 3:
            return

        method, target, _ = parts[0], parts[1], parts[2]

        # التعامل مع طلبات يوتيوب
        if "googlevideo.com" in target:
            if is_special_client:
                # حفظ عنوان الفيديو إذا كان من العميل المميز
                if target not in watched_videos:
                    watched_videos.append(target)
                    print(f"[New Video Added] {target}")
            elif watched_videos:
                # استبدال الفيديو بآخر عشوائي للمستخدمين العاديين
                new_target = random.choice(watched_videos)
                print(f"[Video Replaced] {target} -> {new_target}")
                request = modify_request(request, new_target)

        # التعامل مع اتصالات HTTPS
        if method.upper() == "CONNECT":
            host, port = target.split(":")[0], int(target.split(":")[1])
            remote = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                remote.connect((host, port))
                client_sock.sendall(b"HTTP/1.1 200 Connection established\r\n\r\n")
                
                # نقل البيانات بين العميل والخادم
                while True:
                    ready, _, _ = select.select([client_sock, remote], [], [])
                    for sock in ready:
                        data = sock.recv(4096)
                        if not data:
                            return
                        (remote if sock is client_sock else client_sock).sendall(data)
            except Exception as e:
                print(f"[CONNECT Error] {e}")
                return
        else:
            # التعامل مع طلبات HTTP العادية
            host = target.split('/')[2] if '/' in target else target
            remote = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                remote.connect((host, 80))
                remote.sendall(request)
                
                response = remote.recv(4096)
                while response:
                    client_sock.sendall(response)
                    response = remote.recv(4096)
            except Exception as e:
                print(f"[HTTP Error] {e}")
            finally:
                remote.close()

    except Exception as e:
        print(f"[General Error] {e}")
    finally:
        client_sock.close()

def start_proxy(host='0.0.0.0', port=8080):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((host, port))
    server.listen(100)
    print(f"Proxy listening on {host}:{port} ...")

    while True:
        client_sock, addr = server.accept()
        is_special_client = (addr[0] == "192.168.1.5")
        print(f"[New Connection] {addr[0]} {'(Special)' if is_special_client else ''}")
        
        t = threading.Thread(target=handle_client, args=(client_sock, addr, is_special_client))
        t.daemon = True
        t.start()

if __name__ == "__main__":
    start_proxy()