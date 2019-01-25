__author__ = 'silverback'

import socket

addr = "8.8.8.8"
hostname = "www.google.com"

print(socket.gethostbyaddr(addr))
print(socket.gethostbyname(hostname))

