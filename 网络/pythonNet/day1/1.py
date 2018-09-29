from socket import *

sockfd=socket(AF_INET,SOCK_STREAM)
sockfd.bind(('0.0.0.0',5555))
sockfd.listen(5)
#等待接受连接　
print('wait')
connfd,addr = sockfd.accept() 
#阻塞
print('connect from',addr)


#收发消息　
while True:
    data=connfd.recv(2048).decode()
    if data == '##':
        break
    print(data)
    a=input('请输入')
    n=connfd.send(b'a')
    print('发送了%d字节' % n)

connfd.close()
sockfd.close()

#tarena@tedu:~/桌面/pythonNet$ telnet 127.0.0.1 6666
# Trying 127.0.0.1...
# Connected to 127.0.0.1.
# Escape character is '^]'.

