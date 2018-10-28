Day02回顾
1、数据类型
  1、数值类型
  2、字符类型
  3、枚举类型
  4、日期时间类型
    1、date
    2、time
    3、datetime  # 默认返回NULL
    4、timestamp # 默认返回系统当前时间
2、日期时间函数
  1、NOW()
  2、CURDATE()
  3、CURTIME()
  4、YEAR("时间")
  5、DATE(...)
  6、TIME(...)
  7、日期时间运算
    select ... from 表名 
    where 字段名 运算符 (时间-interval 时间间隔单位)
3、表字段操作
  1、添加(add)
    alter table 表名 add 字段名 数据类型 first | after ..;
  2、删除(drop)
    alter table 表名 drop 字段名;
  3、修改(modify)
    alter table 表名 modify 字段名 新数据类型;
  4、表重命名(rename)
    alter table 表名 rename 新表名;
  5、字段重命名(change)
    alter table 表名 change 原字段名 新字段名 数据类型;
  ## 会受到表中原有数据的限制
4、表记录管理
  1、删除(delete)
    delete from 表名 where 条件;
  2、修改(update)
    update 表名 set 字段名=值1,... where 条件;
5、运算符
  1、数值&&字符&&逻辑比较
    1、数值 ：> >= < <=  =  !=
    2、字符 ：= !=
    3、逻辑 ：and 、or
  2、范围内比较
    1、between 值1 and 值2
    2、in(值1,值2)
    3、not in(值1,值2)
  3、空、非空
    1、空 ：is null
    2、非空 ：is not null
  4、模糊比较(like)
    _ ：1个字符
    % ：0到多个字符
6、SQL查询
  1、order by
    升序 ：ASC
    降序 ：DESC
  2、limit
    1、limit n
    2、limit m,n #从m+1条记录开始,显示n条
    3、分页
      每页显示m条,显示第n页
      limit (n-1)*m,m
  3、聚合函数
    count(...)
  4、group by 分组
    1、select后的字段名如果没有在group by之后出现,必须对其进行聚合处理(聚合函数)
    2、先分组、再聚合
  5、having 
    1、where ：只能操作表中实际存在的字段
    2、having ：能操作由聚合函数生成的显示列
  6、总结
    3、select ... 聚合函数 from 表名
    1、where ...
    2、group by ...
    4、having ...
    5、order by ...
    6、limit ...;
*********************************
Day03笔记
1、SQL查询
  1、distinct : 不显示字段的重复值
    1、语法 ：select distinct 字段1,字段2 from 表名;
    2、示例
      1、表中都有哪些国家
        select distinct country from sanguo;
      2、表中一共有几个国家
        select count(distinct country) as n from sanguo;
    3、注意
      1、distinct和from之间的所有字段值都相同才会去重
  2、查询表记录时可以做数学运算
    1、运算符 ：+ - * / % 
    2、示例
      1、查询时显示所有英雄攻击力翻倍
        select id,name,gongji*2 as new from sanguo;
2、约束
  1、作用 ：保证数据的一致性、有效性
  2、约束分类
    1、默认约束(default)
      插入记录时,不给该字段赋值,则使用默认值
      sex enum("M","F","S") default "S",
    2、非空约束(not null)
      不允许该字段的值为 NULL
      id int not null,
      id int not null default 0,
3、索引
  1、定义
    对数据库中表的一列或多列的值进行排序的一种结构(BTree)
  2、优点
    加快数据的检索速度
  3、缺点
    1、当对表中数据更新时,索引需要动态维护,降低数据的维护速度
    2、索引需要占用物理存储空间
4、索引示例
  1、开启运行时间检测 ：mysql> set profiling=1;
  2、执行查询语句
    select name from t1 where name="lucy99999"; 
  3、查看执行时间 
    show profiles;
  4、在name字段创建索引
    create index name on t1(name);
  5、再次执行查询语句
    select name from t1 where name="lucy100000";
  6、查看执行时间
    show profiles;
5、索引
  1、普通索引(index)
    1、使用规则
      1、可设置多个字段,字段值无约束
      2、把经常用来查询的字段设置为索引字段
      3、KEY标志 ：MUL
    2、创建
      1、创建表时
        create table t1(
	...,
	...,
	index(name),
	index(id));
      2、已有表中
        create index 索引名 on 表名(字段名);
    3、查看索引
      1、desc 表名; -->KEY标志为 MUL
      2、show index from 表名\G;
    4、删除index
      drop index 索引名 on 表名;
  2、唯一索引(unique)
    1、使用规则
      1、可设置多个字段
      2、约束 ：字段值不允许重复,但可以为 NULL
      3、KEY标志 ：UNI
    2、创建
      1、创建表时
        unique(phnumber),
	unique(cardnumber)
      2、已有表
        create unique index 索引名 on 表名;
    3、查看、删除同普通索引
      删除 ：drop index 索引名 on 表名;
  3、主键索引(primary key)&&自增长(auto_increment)
    1、使用规则
      1、只能有1个字段为主键字段
      2、约束 ：字段值不允许重复,也不能为 NULL
      3、KEY标志 ：PRI
      4、通常设置记录编号字段 id,能够唯一锁定一条记录
    2、创建
      1、创建表时
        1、id int primary key auto_increment,
	   name varchar(20) not null
	   )auto_increment=10000,charset=utf8,engine=InnoDB;
	   alter table 表名 auto_increment=10000;
	2、
	  id int auto_increment,
	  name varchar(20),
	  primary key(id)
      2、已有表
        alter table 表名 add primary key(id);
	alter table 表名 modify id int auto_increment;
    3、删除主键
      1、先删除自增长属性(modify)
        alter table 表名 modify id int;
      2、删除主键
        alter table 表名 drop primary key;
6、数据导入
  1、作用 ：把文件系统中内容导入到数据库中
  2、语法格式
    load data infile "文件名"
    into table 表名
    fields terminated by "分隔符"
    lines terminated by "\n";
  3、将socreTable.csv导入到数据库中
    1、在数据库中创建对应的表
      create table score(
      id int,
      name varchar(15),
      score float(5,2),
      phnumber char(11),
      class char(7)
      )character set utf8;
    2、执行数据导入
      1、查看搜索路径
        show variables like "secure_file_priv";
	## /var/lib/mysql-files
      2、拷贝文件
        sudo cp  ~/scoreTable.csv  /var/lib/mysql-files/
      3、执行数据导入
        load data infile "/var/lib/mysql-files/scoreTable.csv"
        into table score
        fields terminated by ","
        lines terminated by "\n";
    3、Mac本配置搜索路径：
      sudo -i
      vi my.cnf
        [mysqld]
        secure_file_priv="/usr/local/mysql/data/"
      系统偏好设置 - 小海豚 - stop - start
      mysql>show variables like "secure_file_priv";
7、数据导出
  1、把数据库表的记录到处到系统文件里
  2、语法格式
    select ... from 表名
    into outfile "文件名"
    fileds terminated by "分隔符"
    lines terminated by "\n";
  3、练习
    1、把MOSHOU库下的sanguo表中,英雄的姓名、攻击值和国家给导出来,sanguo.csv
      1、查看搜索路径
        show variables like "%secure%";
      2、执行数据导出语句
        select name,gongji,country from MOSHOU.sanguo
	into outfile "/var/lib/mysql-files/sanguo.csv"
	fields terminated by ","
	lines terminated by "\n";

	Error: ... secure_file_priv ...
    2、把 mysql 库下的user表中 user、host的值导出到系统文件 user.txt
      select user,host from mysql.user
      into outfile "/var/lib/mysql-files/user.txt"
      fields terminated by "   "
      lines terminated by "\n";
  4、查看、更改文件权限
    1、ls -l score.txt
      -  rw-  rw-  r--   tarena   tarena
        r(4) : 读           所有者   所属组
	w(2) : 写
	x(1) : 可执行
      
        rw- : 所有者权限
	rw- : 同组其他用户文件
	r-- : 其他组的用户权限
    2、chmod 777 score.txt
       chmod 740 score.txt
8、表的复制
  1、语法
    create table 表名 select ... from 表名 where 条件;
  2、示例
    1、复制MOSHOU.sanguo表,sanguo2
      create table MOSHOU.sanguo2 select * from MOSHOU.sanguo;
    2、复制MOSHOU.sanguo中的id、name、country的记录,sanguo3
      create table MOSHOU.sanguo3 select id,name,country from MOSHOU.sanguo; 
    3、复制MOSHOU.sanguo中的name、country,每页显示2条记录,复制第3页的内容
      create table MOSHOU.sanguo4 select name,country from sanguo limit 4,2;
  3、复制表结构
    create table 表名 select ... from 表名 where false;

作业：
  1、把 /etc/passwd 文件导入到数据库 userinfo
    tarena : x  :  1000 : 1000 : tarena,,,:
    用户名  密码   UID    GID    描述
    /home/tarena : /bin/bash
    主目录         登录权限
  
  2、在userinfo表中的第1列添加 id 字段,主键、自增长、显示宽度为3,位数不够用0填充

  001
  002
  003






        

	 

    





        

  
  



    









  2、唯一索引(unique)
  3、主键索引(primary key)
  4、外键(foreign key)



















安装软件 ：sudo apt-get install ...
安装模块/库 ：sudo pip3 install pymysql
安装pip ：pip-0.9.tar.gz
          文件夹 ：文件->setup.py
	  python3 setup.py install




  









      
    
















