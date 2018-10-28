Day 05


１，数据备份（mysqldump.在linux 终端操作）　
　　１，命令格式
　　　mysqldump -u用户名　-p   源库名 > ****.sql
mysqldump -uroot -p db4 > /home/tarena/mydata/db4.sql
　　２，源库名的表示方式　
　　　--all-databases      备份所有的库
　　　库名　　　　　备份一个库
　　　-B 库１　库２．．．　　备份多个库　
　　　库名　表１　表２　　　备份多张表　
　　３，练习　
　　　　１，先把所有库备份　
　　　　２，备份db4库中的sheng city xian 三张表　db4scx.sql 
　　　　３，备份MOSHOU 和　db4 两个库　，md.sql 
２，数据恢复　（提前创建好库）
　　１，命令格式（linux终端）
　　　mysql -u用户名　-p 目标库名　< ***.sql
　　２，从所有库备份ALL.sql中恢复某一个库　
　　　mysql -u用户名　-p –one-database 恢复的库名 < ALL.sql
恢复之前要创建这个库

　　３，示例
　　　１，在db4.sheng 新增一条记录　
　　　２，在db4库，新建一张表t888
　　　３，从db4．sql 恢复db4库　
注意　　
　　　１，恢复库时，如果恢复到原库会将表中数据覆盖，新增表不会删除　
　　　２，恢复库时，如果库不存在，则必须先创建空库　
　　


　　MySQL 调优
　　１，创建索引　 create index(unique index) name on table(name);
　　　在select,where,order by 常涉及到的字段建立索引(index unique index ,primary key )　
　　２，选择合适的存储引擎
　　　１，读操作多：MyISAM 写的时候这个引擎　的读写操作都不能用了
　　　２，写操作多：InnoDB 　　
　　３，SQL语句优化（避免全表扫描）　
　　　１，where 字句尽量不使用　!= , 否则放弃索引全表扫描
　　　２，尽量避免Null 判断，否则全表扫描（指定数据类型的时候　not null就可以避免）　
　　　　　优化前　
　　　　　select number from t1 where number is null 
　　　　　优化前
　　　　　在number字段设置默认值０　确保number 字段无null 
default’0’   
　　　　　select number from t1 where number=0 ;
　　　３，尽量避免用or 连接条件，否则全表扫描
　　　　　优化前；　
　　　　　　select id from t1 where id=10 or id=20;
　　　　　优化后 
　　　　　　select id from t1 where id=10 union all select id from t1 where id=20;
　　　４，模糊查询尽量避免使用前置　% 　否则全表扫描　
　　　优化前
　　　　select variable from t1 where name=＂%secure%＂; 
　　　
　　　优化后
　　　　select variable from t1 where name=＂secure%＂; 


　　　５，尽量避免使用in 和 not in ，否则全表扫描　
　　　　优化前；　
　　　　　select id from t1 where id in(1,2,3,4); 
　　　　优化后：
　　　　　select id from t1 where id between 1 and 4;(值必须连续）　

　　　　６，不能使用select * from ……
　　　　　　用具体的字段来代替星号　

４，事务和事务回滚
　１，定义：　一件事从开始发生到结束的整个过程　
　２，作用：　确保数据一致性　
　３，事务和事务回滚　
　　　１,SQL命令会autocommit 到数据库执行　
　　　２，事务操作　
　　　　　１，开启事务　
　　　　　　　msql>   begin; |  start transactions; 
此时　autocommit 自动禁用　　
　　　　　　　mysql> SQL命令...
                                            ##     此时autocommit 被禁用　## 
中间所有字符命令都不会被提交　

　　　　　２，终止事务
　　　　　　　mysql > commit ;| rollback; 
字符命令会被提交
　　　　　

　　　３，案例　

５，与python 交互　
　　１，交互类型　
　　　　１，python3 
　　　　　模块名：　pymysql 
 　　　　　安装：　　1,在线：sudo pip3 install pymysql == 指定版本
　　　　　　　　　　 2,离线：pymysql.tar.gz 
　　　　　　　　　解压：setup.py 
　　　　　　　　　python3 setup.py install 

　　　　２，python2
　　　　　模块名：MySQLdb 
　　　　　安装：　sudo pip install 
　　２，pymysql 使用流程　
　　　　１，建立数据库连接对象（db=pymysql.connect(＂root＂．
　　　　   ２，创建游标对象（操作数据库对象）(cur=db.cursor())
　　　　３，游标对象：cur.execute(＂insert into sheng…..;＂)
　　　　４，提交到数据库执行：db.commit() 
　　　　５,　关闭游标对象cur.close()
　　　　６，关闭数据库　db.close() 


　　３，connect 连接对象　
　　　　１，db=pymysql.connect (参数列表)
　　　　２，host:主机地址
　　　　３．password:密码　
　　　　４，database: 库
　　　　５，charset=编码方式　推荐utf8
　　　　６，port:端口（３３０６）　

　　４，db(数据库连接对象）的方法
　　　　１，db.close() 断开连接　
　　　　２，db.commit() 提交到数据库执行
　　　　３，db.cursor() 游标对象，用来执行sql命令
　　　　４，db.rollback(): 回滚　

db = pymysql.connect()
cur = db.cursor()
cur.execute()
db.commit()

r = cur.fetchone()


　　５，cursor 游标对象的方法　
　　　　１，execute（ＳＱＬ命令）：执行SQL命令　
　　　　２，close()：关闭游标对象　
　　　　３，fetchone :获取查询结果的第一条数据　 没有值返回None 
查询结果是放在cursor里面，用cursor.fetchone() 拿出１条　
　　　　４，fetchmany(n);获取n条数据　 没有数值返回空元组 
　　　　５，fetchall(): 获取所有数据　
fetchmany(n)　fetchall():得到的结果一定是一个大元组套着一个小元组  没有值返回空元组
行为　关闭　打开　查询　执行语句　
属性　用户名　密码　．．．　对象库名

　　SQL语句参数化
id=input(‘’)
s_name=input(‘’)
sql_insert='insert into sheng(id,s_name) values(%s,%s );'
cursor.execute(sql_insert,[id,s_name])
db.commit()
print(‘ok’) 


6　　　workBench  图形化界面管理工具　
　　　Nacicat  window中图形化界面管理工具


7　　　orm(object Relation Mapping) 对象关系映射
　python 是面向对象编程　
１　示例　
          import sqlalchemy 
　　class User:
　　　　__tablename__=’t1’     
　　　　　　　　　id=Column(Integer,primary_key=True)
　　　　　　　　　name=Colum(String(20)) 
解释　
　一个类　User  →   数据库一张表　
　表中２个字段，　id 和name 

ＯＲＭ框架


MySQL数据库　

１　pymysql 操作原声SQL命令
２．ORM框架对象关系映射　
３　



完整备份


增量备份（只备份今天新增加的数据）
　　

