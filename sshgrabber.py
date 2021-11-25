#!/usr/bin/env python

# banner grab timeee
import socket

#abc-123 vm 
IPADDRESS = '192.168.84.137'

# initalize from socket
s = socket.socket()

# connect to given ip address and port 22 ssh
s.connect((IPADDRESS, 22))


# recvieve in 1024 bytes
response = s.recv(1024)

print(response)


s.close

