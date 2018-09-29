from socket import *

sockfd=socket(AF_INET,SOCK_STREAM)


sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

sockfd.bind(('0.0.0.0',9999))

sockfd.listen(5)

# while True:
c,addr=sockfd.accept()
print('Connect from',addr)
    # while True:
#发送图片
f=open('recv.jpg','wb')

while True:
    data=c.recv(4096)
    if not data:
        break
    f.write(data)

f.close()
c.close()
sockfd.close()
#         if not data:
#             break
#         print('接收到{}:'.format(data))

        
#         c.send(b'666')

# c.close()
# sockfd.close()
