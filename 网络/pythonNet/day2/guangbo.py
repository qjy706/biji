from socket import *

s = socket(AF_INET,SOCK_DGRAM)

# 设置套接字可以发送接受广播　
s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)

#绑定一个固定端口　
s.bind(('0.0.0.0',9999))

while True:
    try:
        msg,addr = s.recvfrom(1024)
        print('从{}获取信息:{}'.format(addr,msg.decode()))


    except (KeyboardInterrupt,SyntaxError):
        raise

    except Exception as e:
        print(e)

s.close()


# >>> s='{1} is a {0}'.format('Bob','boy')
# >>> s
# 'boy is a Bob'
        