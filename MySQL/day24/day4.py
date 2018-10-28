Day 04 

1, 索引（外键）　
　foreign key 
１,定义：让当前表的字段值在另一张表的范围内去选择　
２．　语法格式
create table 表名(xxxxxxxxx,foreign(参考字段名字）
references 主表(被参考字段名)  
on delete 级联动作  
on updata 级联动作;

 create table jftab( id int primary key,  name varchar(20) not null,class char(5),money smallint);

 create table bjtab(stu_id int,name varchar(20),money smallint,foreign key(stu_id) references jftab(id) on delete cascade on updata cascade);

３　使用规则　
　　１　主表，从表字段数据类型要一致　
　　２　主表中被参考字段一般是主键　

４　示例　

　１，表１　缴费信息表（财务）jftab
　　　　id 姓名　班级　缴费金额
　　　　　１，唐伯虎　AID07 　300　
　　　　　２，点秋香　AID07　 300
　２，表２　学生信息表（班主任）bjtab 
　　　　　stu_id 姓名　缴费金额　
　　　　　３　祝枝山　300　（报错）　只能添加主表关联字段记录的值



删除外键　
　alter table 表名　drop foreign key 外键名;
   外键名查看：show create table 表名；

主键绑定一个外键　必须先删掉外键　再删主键


４　已有表添加　

alter table 表名　add foreign key(字段) references 主表（关联字段
on delete 级联动作　
on update 级联动作


alter table bjtab add foreign key(stu_id) reference jftab(id) 
on delete set null
on update set null;



5 　级联动作　
　　１，　cascade 
　　　　数据级联删除，级联更新（参考字段）　
　　２，　restrict (默认)  
　　　　从表中有相关联记录，不允许主表操作，
　　３，　set null 　
　　　　主表删除更新时候　主表相关联记录字段值为null




２　嵌套查询（子查询）
     １．定义：把内层查询结果作为外层的查询条件　
　２．语法：
　　　select …..from 表名where 字段名 运算符　（select ..from 表名 where 条件）;　
　

　３．把攻击力小于平均攻击值的名字和攻击值显示出来，
　　　１，先求平均值　
　　　　　select avg(gongji) from sanguo;
　　　２，找结果　
　　　　　select name ,gongji from sanguo where gongji< 值;


select name,gongji from sanguo where gongji<(select avg(gongji) from sanguo);


找出每个国家攻击力最高的英雄的名字和攻击值

select country,max(gongji) from sanguo gourp by country

select country,name,gongji from sanguo 
where (country,gongji) in (select country,max(gongji) from sanguo group by country) ;



gongji 不能用＝　因为=号是等于一个数值 group 返回的是三个国家最高攻击数字　用in 



３　多表查询
　１，两种方式：
　　　１，笛卡尔积：不加where 条件
　　　　select ….from t1,t2; 
　　　　１，记录多的表的每一条记录，去匹配另一张表的所有记录
　　　　２，２张表记录条数相同，则后表的每条记录去匹配前表　

　　　２，加where 条件　
　　　　select ...from 表１，表２　where 条件;  
　　　　　
　２，显示省，市详细信息
　　　　select sheng.s_name,city.c_name from sheng,city where sheng.s_id=city.cfather_id;
　　　
  　３，
select sheng.s_name,city.c_name,xian.x_name from sheng,city,xian
    ->　where 
    -> 　sheng.s_id=city.cfather_id and city.c_id=xian.xfather_id;



连接查询


１，内连接（inner join) 
　１，语法格式　
　　　select 字段名1,字段名２…from 表１ inner join 表２ on 条件;　
　　　显示省　市详细信息　
mysql> select sheng.s_name,city.c_name from sheng inner join city on sheng.s_id=city.cfather_id;

　　　显示省　市　县信息　
mysql> select sheng.s_name,city.c_name,xian.x_name from sheng 
    -> inner join city inner join xian on sheng.s_id=city.cfather_id and 　　　　　xian.xfather_id=city.c_id;

或

mysql> select sheng.s_name,city.c_name,xian.x_name from sheng  
inner join city on sheng.s_id=city.cfather_id 
inner join xian on city.c_id=xian.xfather_id;

l





２，外连接
　１，左连接(left join)
　　１，以左表为主　显示查询结果　
　　２，select 字段名……    from 表１
　　　　left join 表２ on 条件　
　　　　left join 表３ on 条件　
　　３，　要求省　市详细信息　要求省全部显示　


select sheng.s_name,city.c_name from sheng 
    -> left join city on sheng.s_id =city.cfather_id;

显示　省　市　县　详细信息　

select sheng.s_name,city.c_name,xian.x_name from sheng 
left join city on sheng.s_id =city.cfather_id
left join xian on city.c_id=xian.xfather_id;




　２，右连接(right join)

以右表为主显示查询结果，用法同左连接
select sheng.s_name,city.c_name,xian.x_name from sheng 
right join city on sheng.s_id =city.cfather_id
right join xian on city.c_id=xian.xfather_id;


５　锁　
　　１　目的：解决客户端并发访问的冲突问题　
　　２　不上锁就有不确定性

　　３　锁分类
　　　１，锁的类型　
　　　　　读锁（共享锁）
　　　　查询(select): 加读锁之后，别人不能更改表记录，但可以查询　
　　　２，写锁（互斥锁，排他锁）
　　　　　更新（update)：加写锁之后别人不能查，不能改　

　　　２，锁粒度　
　　　　１，行级锁：　innoDB  一个存储引擎
　　　　　　select : 加读锁，锁１行
　　　　　　update: 加写锁，锁１行
　　　　　　　
　　　　２，表级锁：MyISAM 
　　　　　　select :加读锁　，锁一张表
　　　　　　update: 加写锁　，锁一张表　



６，存储引擎（engine:处理表的处理器）　
　１，查看存储引擎
　　show engines;
　２，查看已有表的存储引擎
　　show create table 表名;

　３，创建表指定存储引擎
　　create table 表名(…) engine =引擎,character set utf8;

　４，已有表更改（一般不改）；
　　alter table 表名 engine=引擎; 

常用存储引擎特点　
１，InnoDB 特点
　　１，支持事务，支持外键，支持行级锁　
　　２，共享表空间
root@tedu:/var/lib/mysql/db4# ls sheng*
sheng.frm  sheng.ibd
　　　　表名.frm　表结构和索引信息　
　　　　表名.ibd　表记录　
　　

２，MyISAM特点　

　　１，支持表级锁
　　２，独享表空间　
　　　表名．frm 　　表结构　
　　　表名．MYD     表记录　mydata
              表名.   MYI       表索引信息　myindex   索引占用物理存储空间

３，Memory 存储引擎
　　１，数据存储在内存里，速度快
　　２，服务器重启，mysql服务重启后表记录消失　

４，如何决定使用哪个存储引擎
　　１，执行查询操作多的表　MyIASM（使用InnoDB浪费资源）
我来查询　一张表　－＞　读锁
其他人　可以进来　查询但不能写
　　２，执行写操作多的表　InnoDB 　
             



7　MySQL用户帐号管理　
　１，开启MySQL远程连接（该配置文件）　
　　　１，sudo -i 
　　　２，cd /etc/mysql/mysql.conf.d/
　　　３，cp mysqld.cnf  mysqld.cnf.bak2
　　　４，subl(vi)  mysqld.cnf
　　　　　#bind-address=127.0.0.1
　　　　　　把前面＃去掉　保存退出
　　　　　　按a →  改内容-→ 按esc →  按shift +: →  wq
　　　５，/etc/init.d/mysql restart 


　２，用root 用户添加授权用户　
　　　１，用root 用户登录mysql 
　　　　　mysql -uroot -p123456 
　　　２，授权　
mysql>                   grant 权限列表 on 库名.表名    to   "用户名"@"%" identified by "密码" with grant option;
　　　　　
　　　　　　权限列表：　all privileges , select  , update
                           库名．表名：　db4.*  ,*.*(所有库所有表）

３　示例　
添加授权用户　tiger ,密码123　，对所有库所有表有所有的权限,可从任何ip连接数据　


添加授权用户，　tabbit   密码　123　对db4所有表　只有select 权限
任何id 去连接　
　３，


