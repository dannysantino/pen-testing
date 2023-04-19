#!/user/bin/python3

import socket

def banner(ip, port):
    s = socket.socket()
    s.connect((ip, int(port)))
    print(s.recv(1024))
    
def main():
    ip = input("Enter IP address: ")
    port = input("Enter port number: ")
    banner(ip, port)

main()