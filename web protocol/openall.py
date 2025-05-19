import socket
import threading

PORT_RANGE = range(1, 1023)  # ⚠️ Use a small range for testing first
HOST = "0.0.0.0"  # Listen on all interfaces

def handle_port(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((HOST, port))
        s.listen(1)
        print(f"[+] Listening on port {port}")
        while True:
            conn, addr = s.accept()
            print(f"[!] Connection attempt on port {port} from {addr[0]}:{addr[1]}")
            conn.close()
    except Exception as e:
        print(f"[-] Could not open port {port}: {e}")

def main():
    for port in PORT_RANGE:
        threading.Thread(target=handle_port, args=(port,), daemon=True).start()

    print("[*] Monitoring started. Press Ctrl+C to stop.")
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("\n[!] Stopping monitor.")

if __name__ == "__main__":
    main()
