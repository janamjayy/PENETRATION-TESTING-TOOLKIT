# PENETRATION-TESTING-TOOLKIT

A simple penetration testing toolkit written in Python. This toolkit provides modules for brute force attacks, port scanning, and other security testing tasks, with easy-to-read logs and colored terminal output.

## Features

- **Brute Force Module:** Automate login brute force attacks using custom user and password lists.
- **Port Scanner Module:** Scan target hosts for open TCP ports.
- **Logging Utility:** Consistent, timestamped logs for info, warnings, and errors.
- **Report Generation:** Saves brute force and port scan results to a report file.
- **Colored Output:** Uses `termcolor` for clear, color-coded terminal messages.

## Requirements

- Python 3.7+
- [requests](https://pypi.org/project/requests/)
- [termcolor](https://pypi.org/project/termcolor/)

Install dependencies:
```sh
pip install -r requirements.txt
```

## Usage

### Brute Force Attack

```sh
python main.py --brute <target_url> --userlist <userlist.txt> --passlist <passlist.txt>
```

**Example:**
```sh
python main.py --brute http://127.0.0.1:5000 --userlist userlist.txt --passlist passlist.txt
```

### Port Scanning

```sh
python main.py --scan <target_host> --ports <port_range>
```

**Example:**
```sh
python main.py --scan 127.0.0.1 --ports 20-1024
```

### Output

- Results and logs are saved to `reports/report.txt`.
- Colored output in the terminal for easy reading.

## Project Structure

```
pen_test_toolkit/
├── main.py
├── modules/
│   ├── brute_forcer.py
│   └── port_scanner.py
├── utils/
│   └── logger.py
├── reports/
│   └── report.txt
├── userlist.txt
├── passlist.txt
└── requirements.txt
```

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## Disclaimer

This toolkit is for educational and authorized penetration testing only. Do **not** use it on systems you do not own or have explicit permission to test.
