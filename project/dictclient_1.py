from socket import *
import sys
from time import ctime,sleep


s = socket()
HOST = '127.0.0.1'
PORT = 8000
ADDR = (HOST,PORT)
s.connect(ADDR)

def frist():
    print('''---------1登录------------''')
    print('''---------2注册------------''')
    print('''---------3退出------------''')

def two(s,name):
    while True:
        print('''---------1查询------------''')
        print('''---------2历史记录---------''')
        print('''---------3退出------------''')
        cmd = input('请输入')
        if cmd == '1':
            r=do_check(s,name)
            if r == 1:
                print('数据不存在')
            else:
                print(r)

        elif cmd == '2':
            r=do_history(s,name)

        elif cmd == '3':
            break


def do_check(name):
    data = input('查询的单词')
    msg = 'C {} {}'.format(name,data)
    s.send(msg.encode())

    a = s.recv(1024).decode()
    if a == 'False':
        return 1
    else:
        return a

def do_check(s,name):
    











def login():
    cmd = input('请输入姓名和密码')
    data = cmd.split(' ')
    try:
        msg = 'L {} {}'.format(data[0],data[1])  
        s.send(msg.encode())
        msg1 = s.recv(1024).decode()
        if msg1 == 'ok':
            print('登陆成功,进入下一界面')
            while True:
                two(s,data[0])

        else:
            print(msg1)
            return
    except:
        return


def rigister():
    print('正在注册')
    while True:
        name = input('User:')
        passwd = getpass.getpass()
        passwd1 = getpass.getpass()
        if (' 'in name) or (' ' in passwd):
            print('用户名和密码不许有空格')
            continue
        if passwd != passwd1:
            print('两次密码不一致')
            continue
        mag = 'R {} {}'.format(name,passwd)
        s.send(mag.encode())

        data = s.recv(1024).decode()
        if data == 'OK':
            return 0
        elif data == 'EXISTS':
            return 1 
        else:
            return 2

while True:
    frist()
    a = input('请输入选项')
    if a == '1':
        login()
    elif a == '2':
        r=rigister()
        if r == 0:
            print('注册成功')
        elif r == 1:
            print('文件已存在')
        elif r == 2:
            print('失败')
    elif a == '3':
        sys.exit('服务器退出')







#坦克项目　
#发送服务端不知道的东西　分组　属性　
#套接字　跳转界面信息　
#界面跳转　
#聊天室简单写一下



