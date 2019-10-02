import sys
import socket
import struct
import random
import time

# Pedro Antonio Ramos
# par25
# 003

# Read server IP address and port from command-line arguments
serverIP = sys.argv[1]
serverPort = int(sys.argv[2])

# Create a UDP socket. Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Assign server IP address and port number to socket
serverSocket.bind((serverIP, serverPort))

print("The server is ready to receive on port:  " + str(serverPort) + "\n")

# loop forever listening for incoming UDP messages
while True:
    # Receive and print the client data from "data" socket
    data, address = serverSocket.recvfrom(1000)
    data2 = struct.unpack(">ii", data)
    time.sleep(0.0500)
    buff = random.randint(1, 10)
    
    data = struct.pack(">ii", 2, data2[1])

    if buff >= 4:
        serverSocket.sendto(data,address)
        print(f"Responding to ping request with sequence number {(data2[1])}")
        
    else:
        print(f"Message with the sequence number {(data2[1])} was dropped")
        pass

