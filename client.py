#! /usr/bin/env python3
# Echo Client
# Pedro A. Ramos
# UCID: par25
# Section: 003

import sys, time
import socket

# Get the server hostname, port and data length as command line arguments
host = sys.argv[1]
port = int(sys.argv[2])
count = int(sys.argv[3])
data = 'X' * count # Initialize data to be sent

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientsocket.settimeout(1)

# Create UDP client socket. Note the use of SOCK_DGRAM
for i in range(3):
    try: 
        # Send data to server
        print("Sending data to   " + host + ", " + str(port) + ": " + data)
        clientsocket.sendto(data.encode(),(host, port))
        dataEcho, address = clientsocket.recvfrom(count)
        print("Receive data from " + address[0] + ", " + str(address[1]) + ": " + dataEcho.decode())
        break
    except socket.timeout:
        print("Message timed out")      
clientsocket.close()
