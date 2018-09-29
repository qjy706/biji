from socket import *

sockfd=socket(AF_INET,SOCK_STREAM)

sockfd.connect(('127.0.0.1',8888))
# f=open('send.jpg','rb')

while True:
    a=input('请输入')
    if not a:
        break
    date=a.encode()
    sockfd.send(date)
    # data=f.read(1024)
    # if not data:
    #     break
    # sockfd.send(data)

    data=sockfd.recv(4096).decode()
    print(data)
# f.close()
sockfd.close()