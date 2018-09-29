# 功能　：类似qq群聊　
# １．进入聊天室需要输入姓名，姓名不能重复　

# ２．有人进入聊天室，会向其他人发送通知　新的连接套接字　

# ３．一个人发消息，其他人会受到消息， (addr)
# 　　　　xxx 说：　xxxxxxx 
# print (f,'say',c.send(data.encode()))
# 4.某人退出聊天室，其他人也会收到通知　

# ５　管理员发消息　

from socket import *
import os 
import sys

# １．进入聊天室需要输入姓名，姓名不能重复　
def main():
    s = socket(AF_INET,SOCK_DGRAM)
    ADDR=('0.0.0.0',8888)

    while True:
        name = input('请输入姓名')
        msg='L '+name
        s.sendto(msg.encode(),ADDR)
        data,addr = s.recvfrom(1024)
        if data.decode() == 'ok':
            print('您已进入聊天室')
        　　　　break
        else:
            print(data.decode())
    pid = os.fork()
    if pid < 0:
        print('创建子进程失败')
    elif pid == 0:
        do_send(s,name,ADDR)
    else:
        do_recv(s,ADDR)

def do_send(s,name,ADDR):
    while True:
        data = input('请输入')
        if data.strip() == 'quit':
            msg = 'Q '+name
            s.sendto(msg.encode(),ADDR)
            sys.exit('推出聊天室')
        msg = 'C {} {}'.format(name.data)
        s.sendto(msg.encode(),ADDR)

def do_recv(s,ADDR):
    while True:
        data,addr = s.recvfrom(2048)
        if data.decode() == 'EXIT':
            sys.exit(0)
        print(data.decode()+'\n发言:',end='')






if __name__ == '__main__':
    main()
