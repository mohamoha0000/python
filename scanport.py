import socket

def scan_ports(ip, start_port=1, end_port=1024):
    print(f"Scanning {ip} from port {start_port} to {end_port} (Timeout: 3s)")
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)  # Set timeout to 3 seconds
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"[+] Port {port} is OPEN")
        else:
            print("no",port)
        sock.close()

# Example usage:
target_ip = "154.144.225.88"  # Replace with your target IP
scan_ports(target_ip, 1, 65535)  # Scan ports 1 to 100
