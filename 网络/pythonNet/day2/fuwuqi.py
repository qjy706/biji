# from socket import *
# #创建一个创建一个套接字

# sockfd=socket(AF_INET,SOCK_DGRAM)
# # 绑定一个服务器地址
# sockfd.bind(('0.0.0.0',10000))

# print('wite')
# while True:
#     data,addr=sockfd.recvfrom(4096)
# # 返回一个数据　和　ip地址

#     # print('从{}获取信息:{}'.format(yao,kobe.decode()))
#     print('from %s:%s' % (addr,data.decode()))
# # 二进制
#     sockfd.sendto('已收到消息'.encode(),addr)

# # 　关闭
# sockfd.close()


# from socket import *
# #创建套接字
# sockfd=socket(AF_INET,SOCK_STREAM)
# # 可以自动释放端口
# sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
# #绑定地址
# sockfd.bind(('0.0.0.0',9999))
# #监听队列
# sockfd.listen(5)

# while True:
#     c,add=sockfd.accept()
# #阻塞函数　等待接入　返回一个连接套接字　和地址
#     while True:
#         data=c.recv(4096).decode()
#         if not data:
#             break
#         print('接收到:',data)
# #收信息　发信息
#         c.send(b'666')

# c.close()
# sockfd.close()
