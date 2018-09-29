from socket import *
import os,sys


#发送消息
def send_msg(s,name,addr):
    while True:
        text = input('发言: ')
        #如果输入quit表示退出
        if text.strip() == 'quit':
            msg='Q '+name
            s.sendto(msg.encode(),addr)
            #这是子进程的函数　
            sys.exit('退出聊天室')
        msg = 'C {} {}'.format(name,text)
        s.sendto(msg.encode(),addr)

#接收消息
def recv_msg(s):
    while True:
        data,addr = s.recvfrom(2048)
        if data.decode() == 'EXIT':
            sys.exit(0)
        print(data.decode()+'\n发言:',end='')

#主要控制流程封装函数
#创建套接字　登录如果登陆成功　创建子进程，因为收消息　发消息都是随机行为，
def main():
    if len(sys.argv) < 3:
        print('argv is error')
        return
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    ADDR=(HOST,PORT)

#创建套接字　
    s=socket(AF_INET,SOCK_DGRAM)
#循环输入名字　，如果输入失败重新输入
    while True:
        name = input('请输入姓名')
#把请求类型和姓名发送过去
        msg = 'L '+name
#发送登录请求
        s.sendto(msg.encode(),ADDR)
#等待服务器回复　
        data,addr = s.recvfrom(4096)
#如果服务器返回一个ok　那就是成功进入聊天室了
        if data.decode() == 'ok':
            print('您已经入聊天室')
#这时候应该跳出循环　进行下一步　
            break
        else:
#如果服务器没有返回ok 服务器会回复不允许登录原因
            print(data.decode())
#创建父子进程
    pid = os.fork()

    if pid < 0:
        sys.exit('创建子进程失败')

    elif pid == 0: 
        send_msg(s,name,ADDR)

    else:
        recv_msg(s)

if __name__ == '__main__':
    main()



