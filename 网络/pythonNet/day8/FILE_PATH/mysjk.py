from pymysql import connect

class SJK:
    def __init__(self,database,host="localhost",user="root",password="123456",charset="utf8"):
        self.database=database
        self.host=host
        self.user=user
        self.password=password
        self.charset=charset

    def __open(self):
        self.open=connect(database=self.database,host=self.host,user=self.user,password=self.password,charset=self.charset)
        self.cur=self.open.cursor()

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
        self.__close()

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
