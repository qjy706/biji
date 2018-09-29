mysql  select * from table where

mongodb  db.collection.find(query,field)

参数：　query 查找条件　相当于where子句　
　　　　　　field 查找的域
返回值：　查找到的所有文档　

query: 以键值对方式传递参数．如果是空{}表示查找所有内容　

e.g  
> db.class3.find({sex:'w'})



field:　以键值对方式给出要查找（不查找）的域　
　　　　　　　以域名为键，以　0,1值分别表示不查找和查找　

*如果某一个或者多个域设置为０　表示这些域不查找　其他域均查找　

*如果某一个或多个域设置为１　表示这些域查找，其他域不查找　

*_id　除非设置为０　否则均会查找（人为设置０　才会不查找）

*除id域其他域不能有的设置１有的设置０


> db.class3.find({sex:'w'},{name:1,age:1})
查找结果只有name  age域　




findOne(query,field)
功能：　查找第一条符合条件的文档　
参数：　同find 
返回值：　返回查找到的文档　



query 更多的筛选用法　（相当于where子句）　

操作符：　使用$符号注明的一个特殊字符串　表达一定的含义，比如$lt 表示小于　

操作符就是特殊的字符串　

比较操作符使用

$eq 等于　==
查找年龄等于１８的任务信息
> db.class3.find({age:{$eq:18}},{_id:0})


$lt 小于　＜　　（字符串也可以比较大小　按asc值）

> db.class3.find({name:{$lt:'Alice'}},{_id:0})


$lte 小于等于　<=
小于kobe的人物信息
> db.class3.find({name:{$lte:'Kobe'}},{_id:0})




$gt 大于　

大于１６　小于１９
> db.class3.find({age:{$gt:16,$lt:19}},{_id:0})

*在mongodb中所有都可以　？＂写多个括号　



$gte 大于等于　>= 


$ne != 
性别不等于'm'的　

db.class3.find({sex:{$ne:'m'}},{_id:0})
*使用ne查找也会找到该域不存在的文档　

$in 　包含　
e.g.

找到年龄为[10,20,30]
db.class3.find({age:{$in:[10,20,30]}},{_id:0})


$nin 不包含




逻辑操作符　

$and 
1. 在query 如果写多个条件默认即为and 关系　
> db.class3.find({age:{$lt:18},sex:'m'},{_id:0})


2.　逻辑与　　$and 

３．　逻辑或　$or 




４  逻辑非　　$not
查找年龄不小于１８岁的
> db.class3.find({age:{$not:{$lt:18}}},{_id:0})

5   $nor  not(a or b) 既不也不　not(a) and not(b)

连接多项文档用中括号　　



db.class3.find({$nor:[{name:{$lt:Lucy}},{age:{$gt:18}}]},{_id:0})


逻辑条件混合　

年龄大于１７　并且　为男性　　或者姓名叫Abby 

 db.class3.find({$or:[{age:{$gt:17},sex:'m'},{name:'Abby'}]},{_id:0})


年龄不大于１８　或者为女性　 并且　姓名大于Lucy
$not:{$gt}　　　　　　　　　　　　

# db.class3.find({$and:[{$or:[{age:{$lte:18}},{sex:'w'}]},{name:{%gt:'Lucy'}}]},{_id:0})


db.class3.find({$or:[{age:{$lte:18}},{sex:'w'}],name:{$gt:'Lucy'}},{_id:0})


Array
[1,2,3,4]

*数组是有序的数据集合
*mongo中数组也可以有多重数据元素混合
> db.class2.insert({name:'阿宝',age:8,sex:'m',score:[56,49,67]})
分数这个域就是数组

e.g. 只要sroce数组中包含小于60的元素即可查询过滤　
db.class3.find({score:{$lt:60}},{_id:0})


$all 
既包含49又包含６７

查找数组同时包含多项的文档


e.g. 查找同时包含49 67
db.class2.find({score:{%all:[49,67]}},{_id:0})


$size 
通过数组元素个数查找　


查找数组元素两个的文档
> db.class2.find({score:{$size:2}},{_id:0})
{ "name" : "百合", "age" : 9, "sex" : "w", "score" : [ 89, 77 ] }


$slice 
显示数组中指定项　跟显示相关的写第二个参数


> 
> db.class2.find({},{_id:0,score:{$slice:2}})　显示数组前两项　
{ "name" : "阿宝", "age" : 8, "sex" : "m", "score" : [ 56, 49 ] }
{ "name" : "阿荣", "age" : 7, "sex" : "w", "score" : [ 92, 88 ] }
{ "name" : "阿哲", "age" : 9, "sex" : "m", "score" : [ 67, 76 ] }
{ "name" : "百合", "age" : 9, "sex" : "w", "score" : [ 89, 77 ] }


> db.class2.find({},{_id:0,score:{$slice:[1,2]}})　数组索引下表　１到２　
{ "name" : "阿宝", "age" : 8, "sex" : "m", "score" : [ 49, 67 ] }
{ "name" : "阿荣", "age" : 7, "sex" : "w", "score" : [ 88, 91 ] }
{ "name" : "阿哲", "age" : 9, "sex" : "m", "score" : [ 76, 83 ] }
{ "name" : "百合", "age" : 9, "sex" : "w", "score" : [ 77 ] }




$exists   
通过某个域是否存在筛选　


寻找不存在sex域的文档　
> db.class2.find({sex:{$exists:false}},{_id:0})
{ "name" : "小程", "age" : 9 }



$mod 余数查找　

> 查找年龄为单数　且分数数组为三个的文档　

> db.class2.find({age:{$mod:[2,1]},score:{$size:3}},{_id:0})
{ "name" : "阿荣", "age" : 7, "sex" : "w", "score" : [ 92, 88, 91 ] }
{ "name" : "阿哲", "age" : 9, "sex" : "m", "score" : [ 67, 76, 83 ] }



$type
找出指定类型的文档　
查看mongo官网　
２是字符

查看名字类型是字符的文档　
> db.class2.find({name:{$type:2}},{_id:0})



查找结果的操作函数

db.collection.distinct　(filed)
功能：查看某个域的值范围　


> db.class3.distinct('name')


pretty()
把查询结果作为一个集合对象　

db.collection.find().pretty()



limit(n)
功能：　显示前n条结果　　




skip(n)
功能：跳过前n条显示后面的查询结构　 

> db.class3.find().skip(5)
跳过前五条文档，显示后面的查询结果



> db.class3.find().skip(5).limit(3)
显示跳过五条之后的查询结果的前三


count() 
功能：　统计查询结果数量　

*在统计数量时要给出一定query条件　

db.class3.find({sex:'w'}).count()
性别为女的查询结果数量　


sort({field:1/-1})
功能：　对查找结果排序　
参数：　以键值对表示按照哪个field排序　
　　　　　　１　表示升序
　　　　　－１　表示降序　


> db.class2.find({},{_id:0}).sort({age:1})
{ "name" : "阿荣", "age" : 7, "sex" : "w", "score" : [ 92, 88, 91 ] }
{ "name" : "阿宝", "age" : 8, "sex" : "m", "score" : [ 56, 49, 67 ] }
{ "name" : "阿哲", "age" : 9, "sex" : "m", "score" : [ 67, 76, 83 ] }
{ "name" : "百合", "age" : 9, "sex" : "w", "score" : [ 89, 77 ] }
{ "name" : "小程", "age" : 9 }

　按照年龄升序排序

－１则是降序　


复合排序　

e.g　按照年龄升序排序，年龄相同按照姓名降序　

> db.class2.find({},{_id:0}).sort({age:1,name:-1})

函数的连续调用

返回结果一致既可以连续调用　




删除文档：
mysql : delete from table where ...

mongodb : db.collection.remove(query,justOne)(justOne只删除一个)
参数：　query　用法同find 
　　　　　　justOne 布尔值　默认为false表示删除所有符合条件的文档　
　　　　　　　　　　　　　　　　　　　　设置为true　则表示只删除一条


删除所有不存在sex域的文档　
> db.class1.remove({sex:{$exists:false}})



删除第一条性别的w的文档　
db.class2.remove({sex:'w'},true)



删除id为　　的文档　
db.class2.remove({_id:{$not:{$type:7}}})


删除class中所有文档　
db.class1.remove({})




练习　：　
１　创建数据　名称　grade 
２　创建集合　名称　class 
3  集合中插入若干文档　文档格式　
{name:'zhangsan',age:10,sex:'m',hobby:['a','b']}
年龄范围　６－１５
爱好选择　draw sing dance basketball football pingpang computer 
每个同学选择2-5项　

４　查找练习　
查看班级所有学生信息
> db.class.find()

查看班级中年龄为８岁的学生信息　
> db.class.find({age:8},{_id:0})

查看班级中年龄大于１０岁学生信息　

查看班级中年龄在８－１１岁之间的学生信息　
查看班级中年龄１０岁且为男生的学生信息　
查看班级中小于７岁或者大于１４岁的学生
查看班级中年龄为８岁或者１１岁的学生
找到有２项兴趣爱好的学生　
找到兴趣中有draw的学生
找到既喜欢画画又喜欢跳舞的学生
统计兴趣有４项的学生人数　
找出本班年龄第二大的学生　
查到本班学生兴趣爱好涵盖哪些方面
找到年龄最大的三个学生
删除所有年龄大于１６或者小于７岁的学生除非他的爱好有三项以上　





修改文档　

mysql update table set .. where 修改哪条文档　

mongodb  db.collection.update(query,update,upsert,multi)

update(query,update,upsert,multi)
功能：　修改文档
参数：　query　　筛选条件　同find 
      update   要修改成什么内容，通常配合修改操作符使用（修改器）使用
      upsert  布尔值　默认是false　　如果query没有筛选到文档则不做任何操作　
      　　　　　　　　如果设置为true 则如果query没有筛选到匹配文档则根据query和update内容插入新的文档　
又是一种插入文档方法
　　　　　　multi  布尔值　默认false 表示如果有多条符合条件文档则只修改一条
　　　　　　　　　　　　　　如果设置为true则表示修改所有符合条件文档　（设置时需要把第三个传参写上）


> db.class2.update({name:'阿宝'},{$set:{age:18}})



upsert 设置为true 如果没有匹配文档　则会创建一个新的文档　
> db.class2.update({name:'Jame'},{$set:{age:15}},true)


讲三国改为mongo版０

insertMany 
save

