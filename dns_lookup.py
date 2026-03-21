import socket

domain = input("Enter a domain name: ")

try:
    ip = socket.gethostbyname(domain)
    print(f"The IP address of {domain} is {ip}")
except socket.gaierror as e:
    print(f"DNS lookup failed: {e}")
except OSError as e:
    print(f"OS error occurred: {e}")
