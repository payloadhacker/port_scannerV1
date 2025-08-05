# 🔌 Simple Python Port Scanner

This is a basic Python script that uses sockets to scan a target IP address for open TCP ports in the range of 50 to 84. It is useful for basic network reconnaissance and learning how socket programming works in Python.

## 📄 Description

The script:
- Accepts a single IP address or hostname as a command-line argument.
- Translates the hostname to its corresponding IPv4 address.
- Scans ports 50 to 84 using TCP connect requests.
- Prints out which ports are open.
- Includes basic exception handling for errors like invalid hostnames or user interruption.

---

## 🛠 Requirements

- Python 3.x

No external libraries are required — only built-in modules are used:
- `socket`
- `sys`
- `datetime`

---

## 🚀 Usage

```bash
python3 scanner.py <ip-address or hostname>

EXAMPLE
python3 scanner.py 192.168.1.1

⚠️ Disclaimer
This tool is intended for educational and authorized testing purposes only. Unauthorized port scanning may be considered illegal in many jurisdictions. Always get permission before scanning a system that you do not own.

OUTPUT EXAMPLE


__________________________________________________
Scanning Target: 192.168.1.1
Time started 2025-08-05 12:34:56.789123
__________________________________________________
Scanning for port....
Port 53 is open
Port 80 is open



