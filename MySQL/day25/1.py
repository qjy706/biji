from pymysql import connect

db=connect(host='loaclhost',user='root',password='123456',database='db4',charset='utf8')
cursor=db.cursor

sql_insert='insert into sheng values(30,400000,'贵州省');'
cursor.execute(sql_insert)

db.commit()
cursor.close()
db.close()
