# from socket import *
# import sys
# import os 


# def main():
#     if len(sys.argv) < 3:
#         print('argv is error')
#         return
#     HOST = sys.argv[1]
#     PORT = int(sys.argv[2])
#     ADDR=(HOST,PORT)    

#     s=socket(AF_INET,SOCK_DGRAM)

#     while True:
#         name = input('请输入姓名')
#         msg = 'L '+name
#         s.sendto(msg.encode(),ADDR)
#         data,addr= s.recvfrom(1024)
#         datalist = data.decode()
#         if datalist == 'ok':
#             print('您已进入聊天室')
#             break
#         else:
#             print(datalist)
#             continue
#     pid = os.fork()
#     if pid < 0:
#         sys.exit('创建子进程失败')

#     elif pid == 0:
#         send_msg(s,ADDR,name)
#     else:
#         recv_msg(s)


# def send_msg(s,addr,name):
#     while True:
#         text = input('发言: ')
#         #如果输入quit表示退出
#         if text.strip() == 'quit':
#             msg='Q '+name
#             s.sendto(msg.encode(),addr)
#             #这是子进程的函数　
#             sys.exit('退出聊天室')
#         msg = 'C {} {}'.format(name,text)
#         s.sendto(msg.encode(),addr)

# #接收消息
# def recv_msg(s):
#     while True:
#         data,addr = s.recvfrom(2048)
#         if data.decode() == 'EXIT':
#             sys.exit(0)
#         print(data.decode()+'\n发言:',end='')