
                c.send('用户不存在,正为您# from socket import *
# from select import *
# import os 

# class Send:
#     def __init__(self,AF=AF_INET,SOCK=SOCK_STREAM):
#         self.AF=AF
#         self.SOCK=SOCK
#         self.s=socket(self.AF,self.SOCK)

#     def connect(self,addr=('127.0.0.1',5000)):
#         self.s.connect(addr)

#     def close(self):
#         self.s.close()

#     def os(self):
#         self.connect()
#         pid=os.fork()
#         if pid < 0:
#             print('创建多路复用失败')

#         elif pid == 0:
#             while True:
#                 data=input('请输入>>')
#                 if not data:
#                     break
#                 self.s.send(data.encode())
#         else:
#             data=self.s.recv(4096)
#             print('{}'.format(data.decode())

#         self.close()



# p=Send()
# p.os()
                
from socket import *
from select import *
import os 

s=socket()

s.connect(('127.0.0.1',5000))

# pid=os.fork()
# if pid < 0:
#     print('创建多路复用失败')

# elif pid == 0:
#     while True:
#         data=input('请输入>>')
#         if not data:
#             break
#             s.send(data.encode())
#         else:
#             data=s.recv(4096)
#             print('{}'.format(data.decode())

# pid=os.fork()
# if pid < 0:
#     print('结束')

# elif pid == 0:
    # data=input('请输入>>')
    # if not data:
    #     break
    #     s.send(data.encode())
# else:
    # data=s.recv(4096)
    # print('{}'.format(data.decode())


for i in range(1,10):
    pid = os.fork()
    if pid <0:
        print('fork error')
        sys.exit(-1)
    elif pid > 0:
        data=input('请输入>>')
        if not data:
            break
        s.send(data.encode())

    else:
        data=s.recv(4096)
        print('{}'.format(data.decode())