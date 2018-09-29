from mysqlpython import MysqlHelp


mysql = MysqlHelp('db4')
    # sql_insert="insert into sheng(s_name) values('河北省');"
    # mysql.work(sql_insert)
sql_insert="select * from sheng;"
result=mysql.getAll(sql_insert)
print(result)



