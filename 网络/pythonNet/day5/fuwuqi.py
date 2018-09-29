from socket import *
import sys 
import os


def do_child(ADDR,s):
    pass

def do_parent(s):
    use={}
    data,addr=s.recvfrom(1024)
    msg=data.decode().split(' ')
    if msg[0] == 'L':
        newclient(addr,use,s,msg[1])
    elif msg[0] == 'C':
        sendclient(msg[1],' '.join(msg[2:]),s,use)
    elif msg[0] == 'Q':
         do_quit(s,use,msg[1])


def do_quit(s,use,name):
    msg= '\n' + name + '推出聊天室'
    for i in use:
        if i == name:
            s.sendto('EXIT'.encode(),use[i])
        else:
            s.sendto(msg.encode(),use[i])
    del use[name]#删除这个键值对


def sendclient(name,data,s,use):
    msg = '\n{}　说:{}'.format(name,data)
    for i in use:
        if i != name:
            s.sendto(msg.encode(),use[i])

def newclient(addr,use,s,name):
    if (name in use) and name == '管理员':
        data = '用户已存在'
        s.send(data.encode(),addr)
        return#跳出该函数
    for i in use:
        msg='欢迎 {} 进入聊天室'.format(name)
        s.send(msg.encode(),use[i])
    use[name]=addr










def main():
    s = socket(AF_INET,SOCK_DGRAM)
    ADDR=('0.0.0.0',8888)
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(ADDR)

    pid = os.fork()
    if pid < 0:
        sys.exit('创建进程失败')
    elif pid == 0:
        do_child(ADDR,s)
    else:
        do_parent(s)

if __name__ == '__main__':
    main()


