import socket
import ssl
from urllib.parse import urlparse

def get_redirect_location(url):
    parsed = urlparse(url)
    host = parsed.hostname
    path = parsed.path or "/"
    if parsed.query:
        path += "?" + parsed.query
    use_https = parsed.scheme == "https"
    port = parsed.port or (443 if use_https else 80)

    # فتح الاتصال
    sock = socket.create_connection((host, port), timeout=10)
    if use_https:
        context = ssl.create_default_context()
        sock = context.wrap_socket(sock, server_hostname=host)

    # إرسال الطلب
    request = f"GET {path} HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n"
    sock.sendall(request.encode())

    # قراءة الاستجابة
    response = b""
    while True:
        data = sock.recv(4096)
        if not data:
            break
        response += data
    sock.close()

    # تحليل الرؤوس
    headers = response.split(b"\r\n\r\n")[0].decode(errors="ignore")
    print("Response headers:\n", headers)

    if " 302 " in headers or " 301 " in headers or "HTTP/1.1 3" in headers:
        for line in headers.split("\r\n"):
            if line.lower().startswith("location:"):
                print("\nRedirect Location:", line.split(":", 1)[1].strip())
                return
    else:
        print("\nNo redirect found.")


# مثال:
url="""https://redirector.googlevideo.com/videoplayback?expire=1751603084&ei=LANnaPDUKPa46dsP1PXgqQI&ip=176.1.135.140&id=o-AMg1ip-OY3oPH8altwSCxi6t8Jmcex_oR2LaTlnGdYPl&itag=18&source=youtube&requiressl=yes&xpc=EgVo2aDSNQ%3D%3D&met=1751581484%2C&mh=H3&mm=31%2C29&mn=sn-uxax4vopj5qx-q0n6%2Csn-4g5e6nzl&ms=au%2Crdu&mv=m&mvi=2&pl=20&rms=au%2Cau&pcm2=no&initcwndbps=2056250&bui=AY1jyLM5T7NcQTcsA_pdLAm_m7_Ew-y9RF9XeVlS8Ut1PXmpiE1kRJDa67vN6goChWxb8hK4aovfx4QN&spc=l3OVKVDpOyuG7b_x2gUQUTkS2sowZPgScWZsmWO5Bk5k_VD2SU9FJnU&vprv=1&svpuc=1&mime=video%2Fmp4&ns=hABbCK7pZroLsIlS1H-HqqAQ&rqh=1&gir=yes&clen=14420610&ratebypass=yes&dur=242.207&lmt=1749477086338223&mt=1751581013&fvip=2&fexp=51331020&c=MWEB&sefc=1&txp=4538534&n=ZJl9g9qxK0ZQiA&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cxpc%2Cpcm2%2Cbui%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cns%2Crqh%2Cgir%2Cclen%2Cratebypass%2Cdur%2Clmt&sig=AJfQdSswRgIhAJFn-Db1SKQE-5ZPd3V6GWHzOdzTQoxl8dbC_5scMjBrAiEAlMwjB5Gy9st709XjdQdQmzv1dyes3V7riSJGjuUXYHs%3D&lsparams=met%2Cmh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Crms%2Cinitcwndbps&lsig=APaTxxMwRAIgEC2VL6ZIfFUtJ02sYc1ZmQldziBzDJ1K70g7b7AkA20CIFRy6wyCoYNtwrF08WkLH4o_RKpYlTjpyRY4PbtOB38f&pot=MnQgtJG7dcsL6SCIw3zUtGJlWrDP926ZQFA0MniRjuD-8VY6yt8ZBG9YOstXnAnJ4tpr8uyimuRtooS0qZDTRDIs8gTF6lJl_HwZoMI4f6KPTXf9MGSberuXxXnGgzxP1-HdX-HrKDXADQxrdefdH-6JN86QMg=="""
get_redirect_location(url)