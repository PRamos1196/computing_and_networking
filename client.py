import sys
import time
import struct
import socket

# Pedro Antonio Ramos
# par25
# 003

count = 0
newTime = []
host = sys.argv[1]
port = int(sys.argv[2])

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print(f"Pinging  {host}, {port}")
for i in range(11):
    # A bytes object containing the ping request and the increment 
    data = struct.pack(">ii", 1, i)
    # creates a new string object given the increment
    increm = str(i)
    # If no response is received within a certain amount of time (one second)
    clientsocket.settimeout(1) # time out
    try:
        sent_time = time.time()
        clientsocket.sendto(data,(host, port))
    except socket.timeout:
        print(f"Ping message number {increm} has timed out")
        continue
    try:
        dataEcho, address = clientsocket.recvfrom(8)
        recover_time = time.time()

        # Unpack from the buffer, the result is a tuple
        dataEcho = struct.unpack(">ii", dataEcho)

        # increments the count, for times a packet has returned
        count = count + 1

        # Measuring the time a packet replied to, and appending to that
        # list
        newTime.append(recover_time - sent_time)

        print(f"Ping message number {increm} RTT: {round(recover_time - sent_time,6)} secs")
    except socket.timeout:
        print(f"Ping message number {increm} timed out")
        continue
clientsocket.close()

# Function names implied...
def average(x):
    t = 0
    for i in range(len(x)):
        t += x[i]
    t = t/ len(x)
    return t

def minimum(x):
    l = 1
    for i in range(len(x)):
        if (x[i] < l):
            l = x[i]
        else:
            continue
    return l

def maximum(x):
    m = 0
    for i in range(len(x)):
        if (x[i] > m):
            m = x[i]
        else:
            continue
    return m

# Displays Number of Packets that were sent, recieved, and lost(%)
print(f"Number of packets sent: {i}, Number of packets recieved: {count}, Packet Loss: {(10 - count) / 10 * 100} %")

# Displayes Minimum, the Maximum, and the Average RTT (kind of beast)
print(f"Minimum RTT: {round(1000*(minimum(newTime)),2)} ms, Maximum RTT: {round(1000*(maximum(newTime)),2)} ms, Average RTT:  {round(1000*(average(newTime)),2)} ms.")
