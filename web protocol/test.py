import requests
from websocket import create_connection

import socket
# إعداد البروكسي
proxy_host = "help.twitter.com"
#proxy_host ="web.whatsapp.com"
proxy_port = 80



host_header = "ssh-fr-1.vpnv.cc"
#host_header="meayouf.M.crabdance.com:80"
"""host_header="meayouf2.global.ssl.fastly.net:80"
host_header="proxyhttp-mmgp.onrender.com:80"
host_header ="meayouf.zapto.org:80"""
payload = (
    "GET / HTTP/1.1\r\n"
    f"Host: {host_header}\r\n"
    "Connection: Upgrade\r\n"
    "User-Agent: redmi a3\r\n"
    "Upgrade: websocket\r\n"
    "\r\n"
)



def test_raw_websocket_like_http_custom():
    try:
        s = socket.create_connection((proxy_host, proxy_port), timeout=5)
        s.sendall(payload.encode())

        response = s.recv(4096).decode()
        print("الرد من البروكسي:\n", response)

        if "101 Switching Protocols" in response:
            print("✅ WebSocket Proxy يشتغل مثل تطبيق HTTP Custom")
        else:
            print("❌ WebSocket Proxy لا يتصرف مثل تطبيق HTTP Custom")
        
        s.close()
    except Exception as e:
        print(f"فشل الاتصال الخام (raw socket): {e}")

test_raw_websocket_like_http_custom()
