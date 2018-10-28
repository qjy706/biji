Day 21

回顾　
数据库特点　
１，关系型数据库　
２，跨平台的
３，支持多种编程语言







day22 


1, ，数据类型　
２，字符类型　
３，枚举类型　
４，日期时间类型　


４，日期时间类型　
　　１，　date ;  ＂YYYY-MM-DD＂　
　　２，　datetime: ＂YYYY-MM-DD HH:MM:SS＂　
不给这个字段赋值　会返回NULL
　　３，　timestamp:  ＂YYYY-MM-DD HH:MM:SS＂
不给这个字段赋值　会返回系统默认时间　 
         ４，　time :  ＂HH:MM:SS＂　

注意　：　
datetime : 不给值默认返回　NULL

timestamp; 不给值默认返回系统当前时间　 添加当前时间　now()

　



日期时间函数　

１　now() 返回服务器当前时间　　
２　curdate() 当前日期　
３　date（＂1999-09-09　09：09：09＂）　提取　年月日　
４    time (“xxxx”)  提取时分秒
　
５　year(“...”) 提取　年　
6　month(‘...’) 提取　月
7 day (‘xxx’) 日




+------+----------+----------+-------+------------+---------------------+
| id   | username | password | money | birthday   | cztime              |
+------+----------+----------+-------+------------+---------------------+
|    1 | 用户1    | 123456   |   555 | 1995-05-20 | 2018-08-30 09:40:30 |
|    2 | 用户2    | 123456   |   600 | 1992-02-20 | 2018-08-30 09:54:45 |
|    3 | 用户3    | 123456   |   800 | 1990-03-03 | 2018-07-02 09:00:00 |
|    4 | 用户4    | 123456   |   666 | 1985-02-28 | 2018-07-02 09:10:10 |
+------+----------+----------+-------+------------+---------------------+


select username from t2 where date(cztime)="2018-08-30";


２　日期时间函数　

３　日期时间运算　
　１，语法格式　
select * from 表名
where 字段名　运算符(时间-interval 时间间隔单位);
时间间隔单位　
1 day 
2 day 
1 day | 3 hour | 1 minute | 2 year | 3 month



2 示例 
1, 查询一天以内的充值记录
select * from t2 where 
cztime >=(now()-interval 1 day); 现在时间去减时间　

２，　查询一年以前　

３　查询一天以前，　三天以内的充值记录　
mysql> select * from t2 where
    -> cztime >=(now()-interval 3 day) and cztime <= (now()-interval 1 day);
Empty set (0.00 sec)




４，表字段的操作　（添加　删除　添加到指定位置）

１，语法　alter table 表名　…; 

２，添加字段(add) 　
 alter table 表名 add 字段名 数据类型; 默认最后一个位置　
 alter table 表名 add 字段名 数据类型 first ; 添加第一个位置　
 alter table 表名 add 字段名 数据类型 after 字段名; 字段名后面位置

３，删除字段(drop) 
alter table 表名 drop 字段名;

４，修改字段数据类型(modify):
alter table 表名 modify 字段名　新数据类型;(修改书库类型的时候，要注意字符限制　，　int 改成　tinyint 　就要注意　之前的数据受到限制) 


５，修改表的名字(rename) 
  alter table 表名 rename 新表名; 


6, 修改字段名（change) 
alter table 表名　change 原字段名　新字段名　数据类型;
  
7　练习　
１，　在　db2 库中创建表　stutab ,字段有３个：
name  age  phnumber  

2 在表中第一列添加一个　id 字段　
alter table t2 add id int first;
3 把　phnumber 的数据类型改为 char(11) 
alter table t2 modify phnumber char(11) 
4 在表中最后一列添加一个字段　address 
alter table t2 add address int;
5 删除表中age字段　
alter table t2 drop age
　


5　表记录操作　
１　删除表记录(delete) 
     １　delete from 表名　where　条件;
　２　注意　一定要加where 条件　不加where 条件全部删除表记录　

２　更新表记录(update)_ 
      1  　update 表名　set 字段１＝值１ where 条件
        

6　运算符操作　
１　操作比较＆＆字符比较＆＆逻辑比较　
　　１　，　数值比较：　 =  !=  > >=  < <= 
　　２　，　字符比较：　=  != 
　　３　，　逻辑比较：　
　　　　　　１　，　and 
　　　　　　２　，　or   
　　　　　　　　　where country=’蜀国’ or ‘country=’魏国’;



２　范围内比较
　１，　between 值１　and 值２　
　２，　in(值１，值２)   数字　字符都可以
　３，　not in（值１，值２）　不在里面　
３，练习　
　１，　查找攻击值在100-200之间蜀国英雄信息
　２，　查找蜀国和吴国以外的国家的女英雄信息
　３，　查找id 为　１，３，５的蜀国的英雄　和貂蝉的信息
select * from sanguo where (id in(1,3,5) and country='蜀国') or name='貂蝉';
括号是一起的判断条件　　

7，表字段　，表记录操作　
　　　　　表字段(alter table 表名)　　　　　　　表记录　
增　　　    add                                                               insert into  表名．．
删                 drop                                                                 delete from 表名
改                 modify                                                          update 表名set ...
查　             desc 表名                                                           select * from 表名




３，　匹配空　和　非空　
　１，　空：　is null
    ２，　非空：is not null 
练习，　
　　１，查找姓名为null　的蜀国男英雄信息　
select * from sanguo where name is null and country in('蜀国') and sex in('男')
　　２，查找姓名为＇＇的英雄信息
　　
　　３，在所有蜀国英雄中查找攻击力大于１５０并且名字不为空的英雄攻击值　姓名　
　 select gongji,name,country from sanguo where gongji>150 and name !='' and country in('蜀国');

查找魏蜀　两国英雄中攻击力小于２００　并且　防御力　小于　８０的英雄信息　　　　
 select * from sanguo where country not in('吴国') and gongji < 200 and fangyu < 80;


　　４　注意　
　　　　１，　null 空值　，只能用is  is not 去匹配　
　　　　２，　　＇＇:  空字符串，　只能用＝  !=  去匹配：

４　模糊查询（like) 
　　１，where 字段名　like 表达式
　　２，表达式　
　　　　１，　_:匹配单个字符　
　　　　２，　%: 匹配０到多个字符　
　　３，　练习　
　　　　select name from sanguo where name like ‘_%_’;匹配两个以上的

　　　　select name from sanguo where name like ‘%’;
匹配所有,但不包括NULL
                  select name from sanguo where name like ‘___’;三个字符的名字
                  select name from sanguo where name like ‘赵%’;


show tables like ‘%r%’;  hero 













7，　SQL高级查询　
　１，总结
　　　select … 聚合函数 from 表名         3
              where                                               1
              group by … 　                                    2
              having…….                                     4
              order by…….                                  5
               limit….;                                          6
　　　　

2 order by : 给查询结果进行排序　
   1, order by 字段名　ASC/DESC 
       ASC(默认)：　升序　
　　DESC ：降序

　３　练习
　　　１．　将所有英雄按防御值从高到低排序
　　　　　select * from sanguo order by fangyu desc;
　　　２，　将蜀国英雄按攻击值从高到低排序　
　　　
　　　３，　将魏蜀两国英雄中名字为３个字的　按防御值升序排序　


３　limit  （永远放在SQL命令的最后写）
         １ 显示查询记录的条数　
　　２　用法　
　　　　limit n; →  显示　n 条记录　
　　　　limit m,n;   →    从第m+1条记录开始，显示n条
　　　３　练习　
　　　　在蜀国英雄中　查找防御值倒数第２名到倒数第四名的英雄姓名　　
防御　国家

select name,fangyu,country from sanguo where country in('蜀国') order by fangyu asc limit 1,3;

2 在所有蜀国名字不为null英雄中，查找攻击值前三名的英雄的姓名　攻击　和国家　

select name,gongji,country from sanguo where name is not null and country in('蜀国')  order by gongji desc limit 0,3;

  4 分页　
　  每页显示5条记录，显示第４页的内容
       每页显示n条记录，显示第m页的内容　
　
　   15条起始　limit 15,5 显示第４页　
    前３页是１５条　
　     第一页　limit 0,5; 
　     第二页　limit 5,5;
         第三页    limit 10,5;
         第四页    limit 15,5;
　     第m页　limit (m-1)*n,n


　4 聚合函数　
　 １　分类　
      avg(字段名）:   求该字段的平均值　
　 sum(字段名) :     求该字段的和　
      max(字段名) :    最大值
　min(字段名)：　最小值
      count(字段名）：　统计该字段记录的个数
　
２，练习　
　　１，　所有英雄攻击力最大值　
　
　select max(gongji) from sanguo;
| max(gongji) |
+-------------+
|        1005 |
+-------------+


 select max(gongji) as max from sanguo;　起了一个别名


+------+
| max  |
+------+
| 1005 |








5，Group by :  给查询的结果进行分组　
　１，查询三国表中都有哪些国家　
　　　select country from sanguo group by country;
+---------+
| country |
+---------+
| 吴国    |
| 蜀国    |
| 魏国    |
+---------+
3 rows in set (0.01 sec)

　２，计算每个国家的平均攻击力　
select country,avg(gongji) from sanguo group by country;

先分组　再聚合　　再去重　
蜀国　　　200　　　蜀国
蜀国
蜀国
魏国
魏国　　200　　　魏国
吴国　　100　　　吴国
先分组再聚合函数　再去重　　聚合是根据每组进行聚合　有多少组聚合多少东西

３　注意　
　１　select 之后的字段名如果没有在group by之后出现，则必须要对该字段进行聚合处理


　４，查找所有国家中英雄数量最多的前两名　
select country,count(id) from sanguo group by country order by count(id) desc limit 0,2;

country as 变量名字


先分组！
在聚合！！！


6 , having 语句　 
      １　作用　：　　对查询的结果进行进一步的筛选
　  ２　练习　　having avg(gongji) 
               1 找出平均攻击力大于105的国家的前两名，显示国家名和
平均攻击力

mysql> select country,avg(gongji) from sanguo 
group by country having avg(gongji)>105 order by avg(gongji) desc limit 2;

　　
　　where 只能操作实际存在的字段



１　having 语句通常和group by语句联合使用　，过滤由group by 语句返回的记录集
２．where 只能操作表中实际存在字段，having 语句可操作由聚合函数生成的显示列




select user_id   count(comment_id) as c from comment group by user_id   order by c DESC limit0,10;



本站发表的所有评论数最多的用户及评论数　，　并按评论数从高到低排序
select user_id count(user_id) as c from comment group by user_id order by c ;

select user_id       count(id) as c from comment group by user_id  order by c;


+------+------------+---------+
| id   | article_id | user_id |
+------+------------+---------+
|    1 |      10000 |   10000 |
|    2 |      10001 |   10001 |
|    3 |      10002 |   10000 |
|    4 |      10003 |   10015 |
|    5 |      10004 |   10006 |
|    6 |      10025 |   10006 |
|    7 |      10009 |   10000 |




select user_id,count(id) from comment group by user_id order by count(id) desc;