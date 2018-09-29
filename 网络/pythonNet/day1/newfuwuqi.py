from socket import *
def fuwuqi():
    sockfd=socket(AF_INET,SOCK_STREAM)
    sockfd.bind(('0.0.0.0',10000))
    sockfd.listen(5)
#等待接受连接　
    print('wait')
    connfd,addr = sockfd.accept() 
    #链接套接字
#阻塞
    print('connect from',addr)


#收发消息　
    while True:
        data=connfd.recv(2048).decode()
        if data == '##':
            print(data)
            n=connfd.send(b'bye')
            connfd,addr = sockfd.accept()
        print('接收到:',data)
        n=connfd.send(b'666')
        print('发送了%d字节' % n)

    connfd.close()
    sockfd.close()

fuwuqi()