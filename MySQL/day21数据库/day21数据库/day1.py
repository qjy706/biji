Day21 

开源　可以传播　但不一定免费

特点　
５．７版本　最新８．０　

MySQL
    关系型数据库
           １，数据以行和列形式去存储　
            ２，表中行：一条记录　列：一个字段
           ３，表和表之间逻辑关联叫关系　
          4  mysql 基于硬盘读写　

     非关系型(效率高　但功能少）
     键值对方式存储　mongodb
              ｛  ＇姓名＇：ｑｑｑ，＇班级＇：三班，＇年龄＇：２５…}


      跨平台　
　             windows Linux Unix 运行

面试题目：
　　　数据库　数据库软件　数据仓库

１，数据库软件（就是一个软件，可操作，实现数据库逻辑功能）
２，数据库是一种逻辑概念（ 通过数据库软件来存储数据）
３，数据仓库　用于数据做分析　数据挖掘　


mysql 安装
１，　Ubuntu 安装MySQL服务　
　　１，安装服务器端
　　　　sudo apt-get install mysql-server   
         ２，安装客户端　
　　　　sudo apt-get install mysql-client

          ３　Ubuntu 安装软件　
　　　　1  sudo apt-get install update
                  2  sudo apt-get -f install 
           作用 修复依赖关系


２，　window安装MySQL服务　
　１，　下载安装包（windows)
            mysql-installer***5.7***.msi
    ２，双击


３　启动和链接服务　
　　１，　服务端启动
　1,查看服务状态　
sudo /etc/init.d/mysql status 

sudo /etc/init.d/mysql start

sudo /etc/init.d/mysql stop

sudo /etc/init.d/mysql restart

sudo /etc/init.d/mysql reload


客户端链接　
命令格式　
mysql -h主机地址 -u用户名　-p密码　

mysql -hlocalhost -uroot -p123456

 mysql -uroot -p (回车之后输入密码）



基本命令　
１．sql命令的规则
　　１，每条命令必须以 ；结尾
　　２，ＳＱＬ命令不区分字母大小写　
　　３，使用\c终止当前命令的执行　


２　库的管理　
mysql里面有很多库　库１　库２　库３　库４　
一个库里面有很多表　


１，库的基本操作
１，查看所有库　
　show databases;

 2,创建库
　　create database 库名; 

3,查看创建库的语句(查看字符集)
　show create database 库名;
show create database db1;

+----------+----------------------------------------------------------------+
| Database | Create Database                                                |
+----------+----------------------------------------------------------------+
| db1      | CREATE DATABASE `db1` /*!40100 DEFAULT CHARACTER SET latin1 */ 
+----------+----------------------------------------------------------------+
1 row in set (0.00 sec)



指定字符集
create database db2 character set utf8;


４　查看当前所在库　
select database();

5，切换到指定库
use 库名;


mysql> use db1;
Database changed


6　查看库中的表　
show tables ;

7　删除库
 drop database 库名;


2,　库的命名规则
１，数字，字母，＿　但是不能是纯数字　
２，库名区分字母大小写　
３，不能使用特殊字符，和　MySQL关键字　.like


练习
１，
　


３　表的基本操作　
　１，创建表（别忘了选择库）　在库里面创建表
create table 表名(name char(10),age int,score int );
create table 表名(字段名　数据类型,
                                字段名　数据类型, 
………………);
　２，行　记录　　列　字段　

3,　　表的默认字符集
create table 表名(字段名　数据类型 )character set utf8;

4 查看创建表的语句（字符集，存储引擎
　　show create table 表名;

5 查看表结构：

　desc 表名; 

6 删除表　
drop table 表名;

7 表里面的内容
　select * from 表名;




tarena@tedu:~$ sudo -i
[sudo] tarena 的密码： 
root@tedu:~# ~# cd /var/lib/mysql
~#：未找到命令
root@tedu:~# cd /var/lib/mysql
root@tedu:/var/lib/mysql# ls
auto.cnf         ib_buffer_pool  ib_logfile1  mysql_upgrade_info  sys
db1              ibdata1         ibtmp1       performance_schema
debian-5.7.flag  ib_logfile0     mysql        python1



４　注意　
　　１，　所有数据都是以文件形式存储在数据库目录下/var/lib/mysql
　　２，　




5，　表的记录管理　
１，插入（insert)  
       1,  insert into 表名 values（值１），（值２），｛根据你列的属性｝
　　２．insert into 表名（字段１，字段２）
　　　　values(值１），（值２）;
　　　
2, 查询(select) 
1. select * from 表名　where 条件;
2,  select 字段１,字段 2  from 表名　where 条件;




6, 如何更改库的默认字符集
　１，方法　：　更改配置文件
　２，步骤　：　

　　　１，获取root 权限　
　　　　　sudo -i
              2       cd  /etc/mysql/mysql.conf.d　　　(只适用于乌班图）
   　　  3        cp mysqld.cnf  mysqld.cnf.bak
              4        subl mysqld.cnf
              5         在[mysqld]下：
　　　　　　　character_set_server = utf8
　　　6           /etc/init.d/mysql restart 
         之前的库并不会改变字符集　之后的会改变






7 ，　客户端把数据存储到数据库服务器上的过程　
　　１，　链接到数据服务器　mysql -u用户名　-p 
          2  ,      选择库：　use 库名
　　3   ,       创建/修改表记录　　update 表名　
　　4 ,         断开与数据库的链接: exit; | quit; | \q; 
  
8,           数据类型　
　１，数值类型　
          1, 整型
              1, int 大整型（４个字节）
                        取值范围：　0～（2**32-1）　
　　　2 tinyint 微小整型（１个字节）
　　　　　１，有负号（signed默认）：　-128～127　
　　　　　２，无负号（unsigned): 0~255  tinyint unsigned
    3 smallint 小整型
    4  bigint 极大整型
                        
　　 2, 浮点型　
　　　　　　总位数不要超过七　float(7,2)
                 2, double 
                       字段名　double(m,n) ..
                 3, decimal(m,n)
                        1,存储空间（整数部分，小数部分分开存储）
　　　　　　　规则：　将　9的倍数包装成四个字节
　　　　　　　　　　余数　　　　　　　字节　
　　　　　　　　　　　　0　　　　　　　　　0
　　　　　　　　　　　1-２　　　　　　　　1
　　　　　　　　　　　3～4　　　　　　　　2
　　　　　　　　　　　5～6　　　　　　　　3
　　　　　　　　　　　7～8　　　　　　　4　
　　　　　　　　　decimal(19,9)

                                         整数部分：　10/9＝1余1　     4个字节+1


新建库studb2 并在库中创建表stuinfo
 要求　
id ：大整型
name: 字符类型　宽度为１５
age:　微小整型， 不能为负数
height 　浮点型　小数为2位(float)
money 浮点型　小数位为４位（decimal)

　２，字符类型　

1,char:定长.
...char(宽度) 宽度取值范围: 1-255
name char(20)　＇Ａ＇-→ ‘A              ‘　也占20个字节　　定长！
‘abc’
‘张无忌’
都是三个字符　
跟字节不一样　英文也就三个字节　中文　gbk 两个字节　utf8三个字节
2 varchar :变长
  varchar(宽度) 宽度取值范围 : 1-65535
name varchar(20)    ‘a’ →  
３，　txet / longtext(4G) /blob/longblob 
4 区别
char 浪费存储空间　，性能高
　varchar: 节省存储空间　，性能低　

5　字符类型的宽度和数值类型宽度的区别
１　数值类型宽度为显示宽度，只用于select查询时显示，和占用存储无关，可用zerofill（显示宽度为三位）　不够三位补三位　　　查看效果　
２　字符类型的宽度超过后无法存储　





　３，枚举类型　
１，单选enum
sex enum(值１，值２．．）sex 也是随便取　按照类型名称

２，多选　
likes set(值１，值２，．．．）　likes是随便取得名字　
＃插入记录时　＇study ,python,mysql’
　４，日期时间类型　




　　　



