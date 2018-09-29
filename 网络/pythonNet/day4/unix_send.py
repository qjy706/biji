# from socket import *

# #确保通信两端用的同一个套接字文件　

# sock_file='./sock_file'

# #创建本地套接字　
# sockfd=socket(AF_UNIX,SOCK_STREAM)

# #连接另一端　
# sockfd.connect(sock_file)

# #收发消息　
# while True:
#     msg=input('>>')
#     if msg:
#         sockfd.send(msg.encode())
#         print(sockfd.recv(1024).decode())

# spckfd.close()


from socket import *

kobe='./kobe'

s=socket(AF_UNIX,SOCK_STREAM)

s.connect(kobe)

while True:
    msg=input('>>')
    if msg:
        s.send(msg.encode())
        print(s.recv(1024).decode())

s.close()