import pymysql
#1创建数据库连接对象　
db=pymysql.connect(host="localhost",\
                    user="root",password="123456",\
                    database="db4",charset="utf8")

#2利用db创建游标对象
cursor=db.cursor()

#3利用cursor的execute()方法执行SQL命令　
sql_insert='insert into sheng values(30,400000,"吉林省");'
cursor.execute(sql_insert)

#4提交到数据库执行　
db.commit()
#关闭
cursor.close()
db.close()


# import pymysql
# db=pymysql.connect(host="localhost",
#                      user="root",password="123456",
#                     database="db4",charset="utf8")

# cursor=db.cursor()
# #1,在sheng表中插入一条记录　
# #2, 删除id为８的记录
# #3,id 为１的省的名称改为浙江省　
# try:
#     cursor.execute('insert into sheng values(11,230000,"安徽省");')
#     cursor.execute('delete from sheng where id=8')
#     cursor.execute('update sheng set s_name="浙江省" where id=1')
#     db.commit()
#     print('ok')
# except Exception as e:
#     db.rollback()
#     print('Failed',e)
# cursor.close()
# db.close()



# from pymysql import connect

# db=connect(host='localhost',user='root',
#             password='123456',database='db4',
#             charset='utf8',port=3306)
# cursor=db.cursor()
# sql_select="select * from sheng;"
# cursor.execute(sql_select)
# #所有的查询结果结果放到了游标对象　cursor 中　
# #fetchone() 
# data=cursor.fetchmany(1)
# data1=cursor.fetchall()
# print(data)
# print(data1)

# cursor.close()
# db.close()






