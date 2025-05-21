import socket
from concurrent.futures import ThreadPoolExecutor

def scan_port(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(0.1)
            result = sock.connect_ex((ip, port))
            if result == 0:
                if (port ==80 or port==443) and not "302" in send_payload(ip,port,"GET / HTTP/1.1\r\nHost: [host]\r\nConnection: close\r\n\r\n"):
                    print(f"http://{ip}:80")
                    return True
                #print(f"{ip}:[+] Port {port} is OPEN")
    except Exception as e:
        pass  # Ignore errors silently or log if needed



def send_payload(host,port,pyload):
    pyload = pyload.replace("[host]", host)
    # Create a socket object
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(0.5)  # S
    # Connect to the server
    client.connect((host, port))

    # Send HTTP GET request
    client.send(pyload.encode())

    # Receive and print response
    response = b""
    while True:
        chunk = client.recv(4096)
        if not chunk:
            break
        response += chunk
    client.close()
    return(response.decode())



def scan_ports(ip, start_port=1, end_port=65535, workers=8):
    #print(f"Scanning {ip} from port {start_port} to {end_port} using {workers} workers...")
    with ThreadPoolExecutor(max_workers=workers) as executor:
        for port in range(start_port, end_port + 1):
            executor.submit(scan_port, ip, port)

# Example usage
#target_ip = "help.twitter.com"



lis="192.168.1."
for x in range(1,300):
    scan_ports(lis+str(x), 1, 100, 100)
"""
pyload="GET / HTTP/1.1\r\nHost: [host]\r\nConnection: close\r\n\r\n"
print(send_payload("192.168.1.75",80,pyload))
"""
#scan_ports("192.168.137.52",1,1000,200)