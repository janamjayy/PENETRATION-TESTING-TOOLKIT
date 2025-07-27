import argparse
from modules import port_scanner, brute_forcer

def main():
    parser = argparse.ArgumentParser(description="🛠️ Penetration Testing Toolkit")
    parser.add_argument("--scan", help="Run Port Scanner on target IP", metavar="IP")
    parser.add_argument("--brute", help="Run Brute Force on login URL", metavar="URL")
    parser.add_argument("--userlist", help="Path to usernames list")
    parser.add_argument("--passlist", help="Path to passwords list")
    args = parser.parse_args()

    if args.scan:
        print(f"[+] Starting Port Scan on {args.scan}")
        open_ports = port_scanner.run(args.scan)
        print(f"[+] Open ports: {open_ports}")

    if args.brute and args.userlist and args.passlist:
        print(f"[+] Starting Brute Force Attack on {args.brute}")
        brute_forcer.brute_force(args.brute, args.userlist, args.passlist)
    elif args.brute:
        print("[-] Brute Force requires both --userlist and --passlist")

if __name__ == "__main__":
    main()
