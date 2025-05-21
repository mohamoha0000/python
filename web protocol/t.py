import socket

proxy_host = "api.facebook.com"
proxy_port = 443  # HTTPS

# يجب استخدام SSL في هذا النوع (TLS handshake)
import ssl

def test_api_gateway_proxy():
    context = ssl.create_default_context()
    try:
        raw_socket = socket.create_connection((proxy_host, proxy_port), timeout=5)
        s = context.wrap_socket(raw_socket, server_hostname=proxy_host)

        payload = (
            "GET /v20.0/me HTTP/1.1\r\n"
            f"Host: {proxy_host}\r\n"
            "User-Agent: redmi a3\r\n"
            "Connection: close\r\n"
            "\r\n"
        )

        s.sendall(payload.encode())
        response = s.recv(4096).decode()
        print("🧠 رد API:\n", response)

        if "application/json" in response:
            print("✅ API Proxy يشتغل مثل Facebook Graph")
        else:
            print("❌ ليس API حقيقي أو رد مختلف")

        s.close()
    except Exception as e:
        print(f"❌ فشل الاتصال: {e}")

test_api_gateway_proxy()
