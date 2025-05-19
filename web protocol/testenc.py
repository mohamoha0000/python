from websocket import create_connection

proxy_host = "help.twitter.com"
proxy_port =443

# عنوان WebSocket مع wss://
ws_url = "wss://proxyhttp-mmgp.onrender.com:443"

# إعداد البروكسي
proxy = {
    "http_proxy_host": proxy_host,
    "http_proxy_port": proxy_port,
    "proxy_type": "http",
}

try:
    ws = create_connection(ws_url, http_proxy_host=proxy_host, http_proxy_port=proxy_port)
    print("✅ اتصال WSS ناجح")
    ws.send("Hello WebSocket")
    result = ws.recv()
    print("Received:", result)
    ws.close()
except Exception as e:
    print("❌ فشل اتصال WSS:", e)
