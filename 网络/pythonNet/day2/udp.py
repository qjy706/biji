from socket import *

sockfd=socket(AF_INET,SOCK_DGRAM)
server_addr=('0.0.0.0',10000)

sockfd.bind(server_addr)


while True:
    data,addr=sockfd.recvfrom(4096)
#有链接是一对一关系　客户端退出　服务端有一个专属套接字　也要做出相应处理
#ＵＤＰ没有联系　
    print('from %s:%s' % (addr,data.decode()))

    sockfd.sendto('已收到消息'.encode(),addr)


sockfd.close()


