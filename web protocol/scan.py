import socket
from concurrent.futures import ThreadPoolExecutor

def scan_port(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(0.3)
            result = sock.connect_ex((ip, port))
            if result == 0:
                print(f"[+] Port {port} is OPEN")
    except Exception as e:
        pass  # Ignore errors silently or log if needed

def scan_ports(ip, start_port=1, end_port=65535, workers=8):
    print(f"Scanning {ip} from port {start_port} to {end_port} using {workers} workers...")
    with ThreadPoolExecutor(max_workers=workers) as executor:
        for port in range(start_port, end_port + 1):
            executor.submit(scan_port, ip, port)

# Example usage
target_ip = "help.twitter.com"
scan_ports(target_ip, 2097, 65535, workers=100)