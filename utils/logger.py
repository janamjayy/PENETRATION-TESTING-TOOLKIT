import datetime

def log_info(message: str):
    print(f"[INFO] {datetime.datetime.now().strftime('%H:%M:%S')} - {message}")

def log_warning(message: str):
    print(f"[WARN] {datetime.datetime.now().strftime('%H:%M:%S')} - {message}")

def log_error(message: str):
    print(f"[ERROR] {datetime.datetime.now().strftime('%H:%M:%S')} - {message}")
