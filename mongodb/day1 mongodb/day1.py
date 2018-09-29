MongoDB(芒果数据库)

数据库优点　　数据结构化存储，降低冗余
　　　　　　　　　　提高增删改查效率　
　　　　　　　　　　方便扩展，方便程序调用　

缺点      数据库往往需要指令或语句操作，相对复杂　


数据：　能够输入到计算机中被识别处理的信息的集合

数据结构：　组成一个数据集合的数据之间的关系

数据库：　按照一定的数据结构，存储数据的仓库．数据库是在数据库管理系统管理和控制下，在一定介质上的数据集合

数据库管理系统：数据库管理软件，用于建立维护操作数据库　

数据库系统　　有数据库和数据库管理系统高等开发工具组成的集合


关系型数据库　
采用关系模型来组织数据结构的数据库　（二维表）

Oracle DB2 SQLserver Mysql SQLite 

与非关系型数据库相比　
        关系型数据库容易理解，逻辑类似常见表格　
        使用方便，都是用sql语句　sql语句非常成熟　
        数据一致性高，冗余低，数据完整性好　便于操作　
        技术成熟，功能强大，支持很多复杂操作

缺点　：　
　　　　　　　　每次操作都要进行sql语句解析，消耗较大　
　　　　　　　　不能很好的满足并发需求，特别是海量数据爆发，关系型数据库读写能力不足
　　　　　　　　关系型数据库往往每一步都要进行加锁的操作，也造成了数据库的负担　
　　　　　　　　数据一致性高，有时也会使数据的存储不灵活
有多少字段每次都要读取多少字段





非关系型数据库　　NoSql --> not only sql 

优点　：　高并发　，读写能力强　
　　　　　　　弱化数据结构一致性，使用更加灵活　
　　　　　　　有良好的可扩展性　

缺点：　　通用性差　没有sql语句那样通用的语句　
　　　　　　　操作灵活，导致容易出错和混乱　
　　　　　　　没有外键关联等复杂操作　
　　　　　　


Nosql 的使用情况　
１．　对数据存储灵活性要求高，一致性要求低
２．　数据处理海量并发，要求瞬间效率速度比较高
３．　数据比较容易建立Nosql模型　
４．　网站临时缓冲存储，爬虫应用　


Nosql分类
 
１　键值型数据库  Redis 
２　文档性数据库　　MongoDB 
３　列存储数据库  HBase
４　图形数据库

MongoDB数据库　

标签：　非关系型数据库　　文档型数据库　　最像关系型的非关系型数据库

特点：　
１．　是由c++编写的数据库管理系统
２．　支持丰富的数据操作，增删改差索引聚合　
３．　支持丰富的数据类型　
４．　使用方便　可以很好的扩展．相对比较成熟　
５．　支持众多的编程语言接口（python PHP c++ c＃）

要求　：　
１．关系型数据库和非关系型数据库都有什么优点　
２．MonDB是一个什么样的数据库　

MonDB的安装　

自动安装　
sudo apt-get install mongodb 

默认安装位置　：　/var/lib/mongodb
配置文件位置　：　/etc/mongodb.conf 
命令集位置　：　　/usr/bin   /usr/local/bin

手动下载　
１．下载安装包
www.mongodb.com
２．解压安装包
/usr/local /opt
3.将解压后的MongoDB文件中的bin目录添加到环境变量
PATH=$PATH:/opt/mongodb..../bin
export PATH

将以上两句写入启动脚本，/etc/rc.local

 4.重启　


Mongodb 命令　

设置数据库存储位置
mongod --dbpath 目录

将存储位置设置为dbs 
mongod --dbpath dbs


设置数据库监听端口　

mongod --port 8080
*默认监听端口 27017
　
mongo
进入数据库交互操作界面　

mongo shell　:用来操作mongodb数据库的界面　
　　　　　　　　　　　　　　在这里可以使用mongo语句操作数据库内容

组织结构　：　键值对--> 文档--> 集合 --> 数据库

ID     NAME    AGE 
1      lily    17
2      Lucy    12  
上面是二维表　



{'id':1
 'name':lily
 'age':17
}
文档里面是键值对　
多个文档是集合　
集合产生数据库


mysql 和 mongodb  概念对比　

mysql           mongodb            含义

database         database          数据库

table           collection         表/集合　

column           field             字段/域　

row              document          记录/文档

index            index              索引



创建数据库　

use databaseName 

e.g. 创建一个名字为stu的数据库　
use stu 

* use 实际为选择使用哪个数据库　当数据库不存在时会自动创建
* use 后并不会立即创建数据库，而是需要等到插入数据时数据库才会创建　　

查看系统中的数据库　

show dbs 


插入
db.class.insert({'name':'Lily','age':17,'sex':'w'})

系统数据库说明：

admin :存储用户信息　
local: 存储本地数据
config : 存储分片信息

数据库命名规则
１　使用utf-8字符　（mongo默认支持utf-8）
２　不能含有空格　．　／　＼　'\0' 字符
３　长度不能超过６４字节
４　不能和系统数据库重名　


db : mongodn的全局量，代表当前正在使用的数据库
     会用到db来引出一系列方法　像是一个对象　

*如果不选择使用任何数据库　db代表test 直接插入数据就会建立test数据库


数据库的备份和恢复　(linux)

备份  mongodump -h host -d dbname -o bak(bak是指定的文件夹　没有就会创建)
mongodump -h 127.0.0.1 -d test -o bak


恢复　　mongorestore -h dbhost:port -d dbname path
mongorestore -h 127.0.0.1:27017 -d res bak/test 

数据库监测　(linux)
mongostat 

insert query update delete  每秒增差改删的次数
flushes　　每秒和磁盘交互次数
vsize　　虚拟内存
res 　　　　物理内存
time    时间



mongotop 监控数据库读写时长

ns      数据表　  
total   总时间
read    读时间     
write 　　写时间


删除数据库　


db.dropDatabase()
删除db所代表的数据库　

方法全是小驼峰法　


创建集合　

方法１　
db.createCollection(collection_name)

 db.createCollection('class1')

show collections


方法２　
当向一个集合中插入数据的时候如果集合不存在则自动创建
db.collection_name.insert(...)

> db.class2.insert({'a':1})


查看数据库中集合　
show collections
show tables

集合命令规则
１　合法的utf-8
２　不能有'\0'
3  不能以system.开头，因为这是系统保留集合前缀　
４　不能和关键字重名


删除集合　
db.collect_name.drop()

e.g 删除class2集合　
　　　db.class2.drop()


集合的重命名

db.collection.renameCollection('new_name')


文档里面是键值对　
mongodb中数据的组织形成　---> 文档

mongodb文档　：　是以键值对的形式组成的一组数据，类似python中字典描述数据的方式　

键：　即文档的域，表达了一个键值对的含义　

键的命名规则：
1. utf-8格式字符串　
2. 不能使用'\0'
3. 一个文档中的键不能重复　

值　即文档存储的数据　

＊文档中键值对是有序的
＊文档中键值对严格区分大小写　
　

类型　　　　　　　　　　　　　　　　　　　　　　　　值　


整形　　　　　　　　　　　　　　　　　　　　　　整数1  2  3　
布尔类型　　　　　　　　　　　　　　　　　　　true false
浮点型　　　　　　　　　　　　　　　　　　　　　　小数　

Array                     数组（类似python列表）

Date                     　时间日期　
Timestamp                 时间戳

String                      字符串　
Symbol                    特殊字符串
Binary data                二进制字串

Null                       null 空值　
Object                     内部文档（对象）
code                       js代码
regex                      正则子串　
ObjectId                   自动生成ID标记


 "_id" : 当mongodb插入文档时如果不指定_id域则自动生成_id域．
 　　　　　　　　值如果不自己制定即会自动生成一个ObjectId值

 24位16进制　使用ObjectId经过算法处理保证其唯一性　

'5ba0b2b45e44b3522980ed95'
8位文档创建时间，6位　机器ID ４位进程id  ６位计数器　


集合中的文档　

１　文档的域不一定一样　比如一个文档是电话　一个文档是姓名　
　　　　　　　　　　　　一个文档有一个键值对　一个文档有三个键值对　

　　＊个数不同
　　＊域不相同
　　＊数据类型不同

２　集合中文档各自比较独立　，相互并不影响　


集合创建原则　：
　　１．　集合中的文档要描述同一类事物　
　　２．　数据库中同一类数据尽量集中存放在相同集合
　　３．　集合中的文档嵌套层数不要太多　


插入文档 (没有表时候新建表)
db.collection.insert()
功能：　插入一个文档　
参数:　　要插入的文档

＊插入操作中键可以不加引号　
＊查看插入结果　db.collection.find()



查看集合所有内容　
db.collection.find()


插入多条文档　
参数用中括号里面放入多个文档
> db.class3.insert([{name:'Kobe',age:19,sex:'m'},{name:'Abay',age:18,sex:'w'}])

其他插入方法　

insertOne() 插入一条文档　
db.collection.insertOne()
db.collection.insertMany()


save插入文档　

db.collection.save()
如果正常插入与insert用法相同　

db.class3.save([{name:'Sunny',age:20,sex:'m'},{name:'Alice',age:22,sex:'w'}])

如果插入数据是由_id域，且_id域值存在时则会修改原有文档，如果该值不存在则正常插入　


获取集合对象方法　

db.class0 ===>  db.getCollection('class0')

db.getCollection('class0').find()


作业：
１　对＇要求＇问题进行总结，描述
２　练习数据库的创建删除，集合创建删除　
３．练习数据插入操作
４．复习mysql基本增删改差操作　
