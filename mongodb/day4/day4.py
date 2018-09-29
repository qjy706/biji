固定集合　

mongodb中可以创建大小固定的集合，称之为固定集合　

特点：　能够淘汰早期数据　（大小固定　集合满的时候早期数据会被淘汰）
　　　　　　插入和顺序查找速度更快
　　　　　　可以控制集合的空间大小

使用：　临时缓存　
　　　　　　日志处理

创建固定集合　

db.createCollection(collection,{capped:true,size:10000,max:1000})

capped:true  表示创建固定集合　
size : 表示指定集合的大小，字节
max : 指定集合存放文档上限　

size max 两者取最小　


文件存储

１　存储文件路径　

e.g.
> db.log.insert({filename:'test.zip',size:60.0,path:'/home/tarena/桌面/MongoDB/test.zip'})
优点：　节省数据库空间　
　　　　　　操作简单快捷　
缺点：　当数据库或者文件位置发生变化时，需要修改数据库内容


２　存储文件本身　
　　　将文件以二进制的形式存储到数据库中　

优点：数据库在文件就在，不会受到迁移等影响　
缺点：占用数据库空间大　
　　　　　存取效率低


GridFS 存储大文件　

大文件：　在mongodb中认为　>16m　的文件为大文件  

GridFS 方法　　
　　　在mongodb中以两个集合配合的方法存储文件　 
   fs.files :　　存储文件相关信息（文件名，文件类型）　
   fs.chunks:  分块存储文件实际内容　

存储文件格式　

命令行操作　
（先进文件文件夹里面）
mongofiles -d dbname put file 

dbname : 要将文件存入的数据库　，如果不存在自动创建
file :  要保存的文件　


tarena@tedu:~/桌面/MongoDB$ mongofiles -d 666 put test.zip



创建数据库思路　　两个集合配合　



提取文件　

mongofiles -d dbname get file 


e.g.
tarena@tedu:~/桌面/MongoDB$ mongofiles -d 777 get test2.docx 


优缺点　

优点：　操作方便　提供较好的存储命令　使用数据库存储文件方便移植

缺点：　读写效率低


游标　
cursor  

通过获取操作数据库的返回结果　，得到返回结果对象　
通过游标可以进一步获取操作结果数据．


> use stu
switched to db stu
> 
> var cursor=db.class0.find()

> cursor.hasNext()
true

> cursor.next()
{ "_id" : ObjectId("5ba0b2b45e44b3522980ed95"), "kobe" : 99, "james" : 98 }


将返回结果赋给一个js 变量　，作为查找结果游标　

var cursor = db.class0.find()

查看是否有下一个结果　
cursor.hasNext()

获取下一个结果　
cursor.next()


python --> pymongo 模块

安装：　sudo pip3 install pymongo

操作步骤：　

1. 创建mongodb的数据库连接对象
conn = pymongo.MongoClient('localhost',27017)

2. 生成数据库对象　(__setitem__ __getitem__)
#对象属性绑定
db = conn.stu 
db = conn['stu']#也是一种调用方法　

３．生成集合对象　

myset = db.class0
myset = db['class0']

4 集合操作　（增删改查索引聚合）
插入操作　插入新的文档

insert()
insert_many()
insert_one()
save()#跟insert差别是_id问题　如果_id不存在　都是插入　如果id已经存在　，就是替换

５　关闭数据库连接

conn.close()


#遵循python格式　字典的键是引号
myset.insert({'name':'张铁林','king':'乾隆'})


查找操作　
find() 
功能：　查找数据内容
参数：　同mongo shell find() 
返回一个结果游标


cursor=myset.find({},{'_id':0})#变量cursor是可遍历的 
print(cursor)
for i in cursor:
    # print(i)
    print(i['name'],'-------',i['king'])


find_one()
功能：　查询第一条符合条件的文档　
参数：　同find 
返回值：返回一个字典


*在pymongo所有操作符的用法同mongo shell相同，只是操作时加入引号

cursor对象属性　

next()
limit()
skip()
count()
sort()
pymongo
for i in cursor.sort([('age',1),('name',-1)]):
    print(i)

mongo shell --> sort({age:1,name:-1})
　


*使用for　或者next 使用游标位置不再指向来头位置的时候调用　limit skip sort 就会报错　


修改　
update(query,update,upsert=False,multi=False)


update_many()　　里面的upsert函数自动为true 
update_one()




删除操作　

remove(query,multi=True)#mongo里面默认false
mulit默认是true 表示删除所有query过滤文档　
设置为false表示只删除第一个


python True --> true 
       False --> false
       None --> null 




复合操作　

变量.find_one_and_delete({"King":'咸丰'})
#查找咸丰并删除





索引操作　




聚合操作　
aggregate([])



import gridfs
GridFS()
功能：　生成frid数据库对象　
