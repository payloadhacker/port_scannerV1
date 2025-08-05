#SOCKETS-used to connect to ports & ips
#!/bin/python3

import socket
import sys
from datetime import datetime

#define target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) #Translate hostname to ipv4

else:
    print("Invalid amount of arguments")
    print('Syntax: python3 scanner.py <ip>')


#adding a banner
print('_' * 50)
print(f"Scanning Target:{target}")
print(f"Time started {datetime.now()}")
print('_' * 50)
print("Scanning for port....")
try:
    for port in range(50,85):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #af_inet is ipv4,
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f'Port {port} is open')
        s.close()
except KeyboardInterrupt:
    print('Exiting program')
    sys.exit()
except socket.gaierror:
    print('Hostname could not be resolved')
    sys.exit()
except socket.error:
    print('Could not connect to server')