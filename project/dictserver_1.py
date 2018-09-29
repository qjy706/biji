from pymysql import connect
from threading import Thread
from time import ctime,sleep
import sys 
import traceback
from socket import *
import re
import signal



class SJK:
    def __init__(self,database,host="localhost",user="root",password="123456",charset="utf8"):
        self.database=database
        self.host=host
        self.user=user
        self.password=password
        self.charset=charset

    def __open(self):
        #创建数据库连接对象　
        self.open=connect(database=self.database,host=self.host,user=self.user,password=self.password,charset=self.charset)
        self.cur=self.open.cursor()
        #创建游标对象

    def __close(self):
        self.cur.close()
        self.open.close()

    def work(self,sql,L=[]):
        self.__open()
        try:
            self.cur.execute(sql,L)
            self.open.commit()
            print('ok')
        except Exception as e:
            self.open.rollback()
            print('Failed',e)
        # self.__close()

    def getall(self,sql,L=[]):
        self.__open()
        self.cur.execute(sql,L)
        r=self.cur.fetchall()
        self.__close()
        return r

    def getone(self,sql,L=[]):
        self.__open()
        self.cur.execute(sql,L)
        r=self.cur.fetchone()
        self.__close()
        return r

    def getmany(self,sql,n,L=[]):
        self.__open()
        self.cur.execute(sql,L)
        r=self.cur.fetchmany(n)
        self.__close()
        return r

# mysql = SJK('DICT')
# # chaxun = SJK('DICT')
# # lishi = SJK('DICT')

# p=open('dict.txt')
# for i in p:
#     name=re.split(r'\s+','i')
#     word = name[0]
#     inrerpret = ' '.join(name[1:])
#     sql_insert="insert into dict(name,definition) values('%s','%s');"%(word,inrerpret)
#     mysql.work(sql_insert)
# p.close()



class Server(object):

    def __init__(self,ADDR,HOST,PORT):
        self.ADDR = ADDR 
        self.HOST = HOST
        self.PORT = PORT
        self.create()


    def find(self,data):
        p = open('dict.txt')
        for i in p:
            name=i.split(' ')
            if data == name[0]:
                return i

    def create(self):
        self.s = socket()
        self.s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
        self.s.bind(self.ADDR)

    def start(self):
        self.s.listen(10)
        print('listen')
        while True:
            c,addr = self.s.accept()
            print('from {} '.format(addr))
            t = Thread(target = self.handler,args=(c,))
            t.setDaemon(True)
            t.start()

    def handler(self,c):
        while True:
            try:
                b = c.recv(1024).decode()
                print(b)
                name = b.split(' ')
            except:
                traceback.print_exc()
                continue
            if name[0] == 'L':#L name password
                self.load(c,name[1],name[2])
            elif name[0] == 'R':
                self.register(c,name=name[1],password=name[2])
            elif name[0] == 'C':
                self.check(c,name[1],name[2])
            elif name[0] == 'H':
                self.history(c,name[1])
            elif name[0] == 'Q':
                self.quit(c)

    def load(self,c,name1,name2):
        print('正在处理')
        sql = 'select * from user'
        result=mysql.getall(sql)
        if not result:
            c.send('EXISTS'.encode())
        try:
            for i in result:
                if name1 == i[1]:
                    c.send('OK'.encode())
        except:
            c.send('False'.encode())


    def register(self,c,name,password):
        print('注册')
        sql = "select * from user where name='%s'"%name
        r=mysql.getone(sql)
        if r == None:
            c.send('已存在该用户'.encode())
        else:
            sql = "insert into user(name,password) values('%s','%s')"%(name1,name2)
            mysql.work(sql)
            c.send('创建成功'.encode())


    def check(self,c,name,word):
        print('正在查询')
        b=ctime()
        sql="insert into history(name,time) values('%s','%s')"%(name,b)
        mysql.work(sql)
        sql = "select * from dict where name='%s"%word
        r=mysql.getone(sql)
        if r == None:
            c.send('False'.encode())
        else:
            data = r[2]
            c.send(data.encode())






    def quit(self,c,user):
        pass
        sys.exit(0)

    def history(self):
        pass




if __name__ == '__main__':
    HOST='0.0.0.0'
    PORT=8000
    ADDR=(HOST,PORT)
    mysql = SJK('DICT')
    s=Server(ADDR,HOST,PORT)
    s.start()












# mysql> show tables;
# +----------------+
# | Tables_in_DICT |
# +----------------+
# | dict           |
# | history        |
# | user           |
# +----------------+
# 3 rows in set (0.00 sec)
