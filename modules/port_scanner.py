import socket
from termcolor import colored

def run(host, start_port=1, end_port=1024):
    print(colored(f"[*] Scanning {host} from port {start_port} to {end_port}", "cyan"))
    open_ports = []

    for port in range(start_port, end_port + 1):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((host, port))
            if result == 0:
                open_ports.append(port)
                print(colored(f"[+] Open port: {port}", "green"))
            sock.close()
        except socket.error:
            pass

    if not open_ports:
        print(colored("[-] No open ports found.", "red"))

    return open_ports
