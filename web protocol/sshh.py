import socket
import threading
import paramiko
import sys

# مفتاح الخادم (يُنشأ مرة واحدة عند بدء الخادم)
host_key = paramiko.RSAKey.generate(2048)

# تعريف خادم SSH البسيط
class SimpleSSHServer(paramiko.ServerInterface):
    def __init__(self):
        self.event = threading.Event()

    def check_auth_password(self, username, password):
        if username == 'test' and password == 'test':
            return paramiko.AUTH_SUCCESSFUL
        return paramiko.AUTH_FAILED

    def get_allowed_auths(self, username):
        return 'password'

    def check_channel_request(self, kind, chanid):
        if kind == 'session':
            return paramiko.OPEN_SUCCEEDED
        return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED

def handle_connection(client_socket, client_addr):
    print(f"[+] اتصال جديد من {client_addr[0]}:{client_addr[1]}")
    try:
        transport = paramiko.Transport(client_socket)
        transport.add_server_key(host_key)
        server = SimpleSSHServer()
        try:
            transport.start_server(server=server)
        except paramiko.SSHException as e:
            print("[-] فشل في بدء جلسة SSH:", str(e))
            return

        chan = transport.accept(10)
        if chan is None:
            print("[-] لم يتم قبول القناة")
            return

        chan.send("✅ تم الاتصال بخادم SSH البسيط.\r\n")
        while True:
            chan.send("$ ")
            command = chan.recv(1024).decode('utf-8').strip()
            if command.lower() == 'exit':
                chan.send("👋 مع السلامة!\r\n")
                break
            else:
                response = f"👉 تم استلام الأمر: {command}\r\n"
                chan.send(response)

        chan.close()
    except Exception as e:
        print("[-] خطأ:", str(e))
    finally:
        client_socket.close()

def start_ssh_server(host='0.0.0.0', port=2222):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    server_socket.listen(100)
    print(f"[√] خادم SSH يعمل على {host}:{port} - تسجيل الدخول بـ test:test")

    try:
        while True:
            client, addr = server_socket.accept()
            threading.Thread(target=handle_connection, args=(client, addr)).start()
    except KeyboardInterrupt:
        print("\n[*] إيقاف الخادم...")
    finally:
        server_socket.close()

if __name__ == '__main__':
    start_ssh_server()
