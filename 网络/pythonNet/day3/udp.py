# from socket import *
# s=socket(AF_INET,SOCK_DGRAM)
# s.bind(('0.0.0.0',9999))

# while True:
#     c,addr=s.recvfrom(4096)
#     print('from {}:{}'.format(addr,c.decode()')
#     data=(c,addr)
#     s.sendto('666'.encode(),data)
# s.close()


from socket import *

s=socket(AF_INET,SOCK_DGRAM)
c=('127.0.0.1',9999)

while True:
    a=input('请输入')
    if not a:
        break
    s.sendto(a.encode(),c)
    b,addr=s.recvfrom(4096)
    print('from {}:{}'.format(addr,b.decode()))
s.close()