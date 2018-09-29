from pymysql import *
from time import ctime,sleep
class SJK:
    def __init__(self,database,host="localhost",user="root",password="123456",charset="utf8"):
        self.database=database
        self.host=host
        self.user=user
        self.password=password
        self.charset=charset

    def open(self):
        self.open=connect(database=self.database,host=self.host,user=self.user,password=self.password,charset=self.charset)
        self.cur=self.open.cursor()

    def close(self):
        self.cur.close()
        self.open.close()

    def work(self,sql,L=[]):
        self.open()
        try:
            self.cur.execute(sql,L)
            self.open.commit()
            print('ok')
        except Exception as e:
            self.open.rollback()
            print('Failed',e)
        # self.close()






if __name__ == '__main__':
    # data = input('请输入')
    # mag=work(data)

    p = open('dict.txt')
    for i in p:
        mysql = SJK('dict')
        name=i.split(' ')[0]
        sql_insert="insert into dicts(name,definition,time) values('%s','%s','%s');"%(name,i,ctime())
        mysql.work(sql_insert)
    mysql.close()