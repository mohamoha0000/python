
import requests
from websocket import create_connection

import socket

from concurrent.futures import ThreadPoolExecutor




# 1. اختبار البروكسي باستخدام requests (تطبيق أزرق)
def test_http_proxy(proxy_host,proxy_port):
    proxies = {
        "http": f"http://{proxy_host}:{proxy_port}",
        "https": f"http://{proxy_host}:{proxy_port}",
    }
    try:
        response = requests.get("https://google.com", proxies=proxies, timeout=5)
        print("proxy normale",proxy_host,":",proxy_port)
    except Exception as e:
        pass
        #print(f"HTTP Proxy: فشل ({e})")

# تنفيذ الفحص




host_header = "ssh-fr-1.vpnv.cc:80"
#host_header="meayouf.M.crabdance.com:80"
payload = (
    "GET / HTTP/1.1\r\n"
    f"Host: {host_header}\r\n"
    "Connection: Upgrade\r\n"
    "User-Agent: redmi a3\r\n"
    "Upgrade: websocket\r\n"
    "\r\n"
)

def test_raw_websocket_like_http_custom(proxy_host,proxy_port):
    global payload
    try:
        s = socket.create_connection((proxy_host, proxy_port), timeout=5)
        s.sendall(payload.encode())

        response = s.recv(4096).decode()
        #print("الرد من البروكسي:\n", response)

        if "101 Switching Protocols" in response:
            #print("✅ WebSocket Proxy يشتغل مثل تطبيق HTTP Custom")
            print("websoket",proxy_host,":",proxy_port)
        else:
            pass
            #print("❌ WebSocket Proxy لا يتصرف مثل تطبيق HTTP Custom")
        
        s.close()
    except Exception as e:
        pass
        #print(f"فشل الاتصال الخام (raw socket): {e}")



def test(proxy_host):
    ports=[80,8080,8880,2052,3128,8888,8000]
    for proxy_port in ports:
        test_http_proxy(proxy_host,proxy_port)
        test_raw_websocket_like_http_custom(proxy_host,proxy_port)
name=["whatsapp.com","facebook.com","instagram.com","x.com","snapchat.com","twitter.com"]        
lis=[]
common_subdomains = [
        'www', 'mail', 'ftp', 'help', 'blog', 'api', 'dev', 'test', 'secure', 'shop',
        'forum', 'news', 'docs', 'support', 'app', 'login', 'staging', 'beta'
    ]
for x in name:
    for i in common_subdomains:
        lis.append(i+"."+x)
with ThreadPoolExecutor(max_workers=50) as executor:
    for host in lis:
        executor.submit(test,host)