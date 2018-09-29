


# from socket import *



# sockfd=socket(AF_INET,SOCK_DGRAM)
# addr=('127.0.0.1',9999)


# while True:
#     a=input('请输入')
#     if not a:
#         break
#     sockfd.sendto(a.encode(),addr)

#     data,addrs=sockfd.recvfrom(4096)
#     print('接收到',data.decode())


# sockfd.close()



# from socket import *
# import sys
# if len(sys.argv) < 3:
#     print('''argv is error run as python3 udpkehuduan.py 127.0.0.1 8888''')
# #从命令行输入IP 端口
# HOST=sys.argv[1]
# PORT=int(sys.argv[2])#命令行是字符串组成的列表
# ADDR=(HOST,PORT)
# #创建套接字
# sockfd=socket(AF_INET,SOCK_DGRAM)


# #消息发送接收
# while True:
#     data=input('发送>>')
#     if not data:
#         break
#     sockfd.sendto(data.encode(),ADDR)
#     data,addr=sockfd.recvfrom(1024)
#     print('接收到:',data.decode())



# sockfd.close()


# from socket import *

# sockfd=socket(AF_INET,SOCK_DGRAM)

# addr=(('192.168.1.166',10000))

# while True:
#     data=input('请输入')
#     if not data:
#         break
#     sockfd.sendto(data.encode(),addr)
#     data,addrs=sockfd.recvfrom(1024)
#     print('接收到:',data.decode())

# sockfd.close()


from socket import *


#创建套接字
sockfd=socket(AF_INET,SOCK_STREAM)
#链接服务器
sockfd.connect(('127.0.0.1',9999))

while True:
    data=input('发送:')
    if not data:
        break
    sockfd.send(data.encode())
#发送和接受　必须发送的是字节串
    data=sockfd.recv(4096)
    print('接收到:',data.decode())

sockfd.close()
