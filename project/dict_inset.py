import pymysql 
import re

f = open('dict.txt')

db = pymysql.connect('localhost','root','123456','DICT')
cursor = db.cursor()
for line in f:
    l = re.split(r'\s+',line)
    word = l[0]
    inrerpret = ' '.join(l[1:])
    sql="insert into dict(name,definition) values('%s','%s')"%(word,inrerpret)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()

f.close()