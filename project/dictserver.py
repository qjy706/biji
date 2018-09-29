import os 
import sys
import signal
import pymysql
import time 
from socket import *
import traceback

#定义需要的全局变量　
DICT_TEXT = './dict.txt'
HOST = '0.0.0.0'
PORT = 8000
ADDR = (HOST,PORT)

def main():
    #创建数据库连接
    db = pymysql.connect('localhost','root','123456','dict')

    #创建套接字　
    s = socket()
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(ADDR)
    s.listen(5)
    #忽略子进程信号　 避免僵尸进程
    signal.signal(signal.SIGCHLD,signal.SIG_IGN)
    #等待客户端连接　
    while True:
        try:
            c,addr = s.accept()
            print('connect from ',addr)
        except KeyboardInterrupt:
            s.close()
            sys.exit('服务器退出')
        except Exception as e:
            traceback.print_exc()
        #创建子进程　
        pid = os.fork()
        if pid == 0:
            s.close()
            print('子进程准备处理请求')
            do_child(c,db)
            sys.exit(0)
        else:
            c.close()
            continue

def do_child(c,db):
    while True:
        data = c.recv(1024).decode()
        print(c.getpeername(),':',data)
        if (not data) or data[0] == 'E':
            c.close()
            sys.exit(0)
        elif data[0] == 'R':
            do_register(c,data,db)
        elif data[0] == 'L':
            do_login(c,data,db)
        elif data[0] == 'Q':
            do_query(c,data,db)
        elif data[0] == 'H':
            do_history(c,data,db)


def do_login(c,db,data):
    print('登录操作')
    l = data.split(' ')
    name = l[1]
    passwd = l[2]
    cursor = db.cursor()#创建游标对象

    sql = "select * from user where name='%s' and password='%s'"%(name,passwd)
    cursor.execute(sql)
    r=cursor.fetchone()

    if r == None:
        c.send(b'FALL')
    else:
        c.send(b'ok')


def do_register():
    print('注册操作')
    l = data.split(' ')
    name = l[1]
    passwd = l[2]
    cursor = db.cursor()

    sql = "select * from user where name='%s'"%name
    cursor.execute(sql)
    r = cursor.fetchone()
    if r != None:
        c.send(b'EXISTS')
        return
    sql = "insert into user(name,password) values('%s','%s') "%(name,passwd)
    try:
        cursor.execute(sql)
        db.commit()
        c.send(b'OK')
    except:
        db.rollback()
        c.send(b'FALL')
    else:
        print('%s注册成功'%name)


def do_query(c,data,db):
    print('查询操作')
    l = data.split(' ')
    name = l[1]
    passwd = l[2]
    cursor = db.cursor()
    def insert_history():
        tm = tmme.ctime()
        sql = "insert into history (name,word,time) values('%s','%s','%s')"%(name,word,tm)
        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback
    try:
        f = open(DICT_TEXT)
    except:
        c.send(b'FALL')
        return

    for line in f:
        tmp=line.split(' ')[0]
        if tmp > word:
            c.send(b'FALL')
            return
        elif tmp == word:
            c.send(b'OK')
            time.sleep(0.1)
            c.send(line.encode())
            f.close()
            insert_history()
            return
    c.send(b'FALL')
    f.close()



xzazx
def history(c,data,db):
    print('历史记录')
    l = data.split(' ')
    name = l[1]
    cursor = db.cursor()

    sql = "select * from history where name='%s'"%name

    cursor.execute(sql)
    r = cursor.fetchall()
    if not r:
        c.send(b'FALL')
        return
    else:
        c.send(b'OK')
    for i in r:
        time.sleep(0.1)
        msg = "%s   %s    %s"%(i[1],i[2],i[3])
        c.send(msg.encode())
    time.sleep(0.1)
    c.send(b'##')

if __name__ == '__main__':
    main()



