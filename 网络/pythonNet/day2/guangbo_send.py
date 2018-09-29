# from socket import *
# from time import sleep

# dest = ('176.8.18.255',9999)

# s=socket(AF_INET,SOCK_DGRAM)

# s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)

# while True:
#     sleep(2)
#     s.sendto('双击666'.encode(),dest)

# s.close()

from socket import *
from time import sleep 

dest = ('192.168.1.255',9999)

s=socket(AF_INET,SOCK_DGRAM)

s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)

while True:
    sleep(2)
    s.sendto('双击666'.encode(),dest)

s.close()