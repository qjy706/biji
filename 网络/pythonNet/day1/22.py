# from socket import *
# #创建套接字
# q=socket(AF_INET,SOCK_STREAM)

# #绑定服务端地址
# q.bind(('176.8.18.212',9999))

# #设置监听套接字 
# q.listen(10)
# #消息收发
# print('wait')
# fd,addr = q.accept()
# print('连接来自于',addr)

# a=fd.recv(2048).decode()
# print(a)

# fd.send(b'666')

# fd.close()
# q.close()

from socket import *

q=socket(AF_INET,SOCK_STREAM)
#创建套接字
q.bind(('0.0.0.0',10000))
#绑定服务器地址
q.listen(10)
#设置监听器套接字
fd,addr=q.accept()
#等待客户端连接请求
print('地址来自',addr)
while True:
    a=fd.recv(2048).decode()
    #fd是连接套接字，跟客户端通信用的
    print(a)
    if a == '##':
        print(fd.send(b'bye'))
        print('新的客户')
        fd,addr=q.accept()
    b=input('请输入')
    c=b.encode()
    fd.send(c)

fd.close()
q.close()
