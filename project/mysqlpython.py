# from pymysql import connect


# class MysqlHelp:
#     def __init__(self,database,host='localhost',password='123456',user='root',charset='utf8',port=3306):
#         self.database=database
#         self.host=host
#         self.user=user
#         self.password=password
#         self.charset=charset
#         self.port=port

#     #连接数据库
#     def open(self):
#         self.conn=connect(database=self.database,host=self.host,user=self.user,password=self.password,charset=self.charset,port=self.port)
#         #实例的数据库连接对象
#         self.cur=self.conn.cursor()#实例的游标

#     #关闭
#     def close(self):
#         self.cur.close()
#         self.conn.close()



#     #执行SQL语句
#     def work(self,sql,L=[]):
#         self.open()
#         try:
#             self.cur.execute(sql,L)
#             self.conn.commit()
#             print('ok')
#         except Exception as e:
#             self.conn.rollback()
#             print('Failed',e)
#         self.close()

# #查询结果
#     def getAll(self,sql,L=[]):
#          self.open()
#          self.cur.execute(sql,L)#存储到游标中
#          result=self.cur.fetchall()
#          print('ok')
#          self.close()
#          return result




# if __name__ == '__main__':
#     #测试
#     mysql = MysqlHelp('MOSHOU')
#     # sql_insert="insert into sheng(s_name) values('河北省');"
#     # mysql.work(sql_insert)
#     sql_insert="select * from sanguo;"
#     result=mysql.getAll(sql_insert)
#     print(result)



from pymysql import connect

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
        self.close()

    def getall(self,sql,L=[]):
        self.open()
        self.cur.execute(sql,L)
        r=self.cur.fetchall()
        self.close()
        return r

    def getone(self,sql,L=[]):
        self.open()
        self.cur.execute(sql,L)
        r=self.cur.fetchone()
        self.close()
        return r

    def getmany(self,sql,n,L=[]):
        self.open()
        self.cur.execute(sql,L)
        r=self.cur.fetchmany(n)
        self.close()
        return r


mysql = SJK('MOSHOU')
    # sql_insert="insert into sheng(s_name) values('河北省');"
    # mysql.work(sql_insert)
sql_insert="select * from sanguo;"
result=mysql.getmany(sql_insert,2)
print(result)