# tcp客户端
from socket import *

sockfd=socket(AF_INET,SOCK_STREAM)
#发起连接
server_addr = ('127.0.0.1',9999)
sockfd.connect(server_addr)

#消息发送接收
while True:
    data=input('发送>>')
    if data == '##':
        break
    sockfd.send(data.encode())
    data=sockfd.recv(1024)
    print('接收到:',data.decode())



sockfd.close()


