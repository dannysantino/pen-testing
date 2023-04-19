#!/usr/bin/python3

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = input("Enter IP address: ")
port = int(input("Enter port number: "))

def PortScanner(port):
    if s.connect_ex((host, port)):
        print("The port is closed")
    else:
        print("The port is open")

PortScanner(port)