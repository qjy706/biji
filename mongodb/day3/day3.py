时间数据类型　

mongo中存储事件大多为　ISODate

存储当前时间方法　
　１．new Date() 自定生成当前时间　
> db.class2.insert({book:'Python入门',date:new Date()})

　２．ISODate() 

 3. Date() 将系统时间转换为字符串　
> db.class2.insert({book:'Python疯狂',date:Date()})



指定时间

ISODate()
功能：　生成mongo 标准时间类型数据　
参数：　如果不传参默认为当前时间　
　　　　　　传参表示指定时间　


指定一个时间　
> db.class2.insert({book:'Python崩溃',date:ISODate('2018-07-01 11:15:56')})


时间戳　

           
valueOf()

> db.class2.insert({book:'Python666',date:ISODate().valueOf()})



Null类型　

值　　Null

1 如果某个域存在却没有值　可以赋值为null
> db.class2.insert({book:'Python死去活来',price:null})

2 可以查找某个域不存在的情况　
e.g. 如果date域不存在也能find到　


Object (内部文档)

文档内部某个域的值还是一个文档数据　则这个文档就是内部文档类型数据　

> db.class4.insert({name:'鲁迅',sex:'m',book:{title:'狂人日记',price:46.8}})



查找有狂人日记的信息　

这里注意bool.title没办法被电脑读取　必须要加字符串　

> db.class4.find({'book.title':'狂人日记'},{_id:0})

更新也可以用　

db.class4.update({'book.title':'狂人日记'},{$set:{'book.title':'百草园'}})




数组的下标操作方式

可以通过  域名.下标  的方式具体操作数组的某一项

e.g.  查找数组 0 项大于90的文档
db.class2.find({'score.0':{$gt:90}},{_id:0})

e.g.  将score 第1项改为10
db.class2.update({name:'小红'},{$set:{'score.1':10}})




将小红年龄改为１２岁　兴趣爱好变为跳舞画画

> db.class.update({name:'zhangsan'},{$set:{age:12,hobby:['draw','sing']}})

追加小明爱好唱歌

> db.class.update({name:'Tom'},{$push:{hobby:'sing'}})

追加小王兴趣爱好　　吹牛　　打篮球　


小李兴趣多了跑步和唱歌　但是要确保和以前不重复　
> db.class.update({name:'Lisi'},{$addToSet:{hobby:{$each:['running','sing']}}})



将班级所有男同学年龄加１
 db.class.update({sex:'m'},{$inc:{age:1}},false,true)




删除小明sex属性　
> db.class.update({name:'James'},{$unset:{sex:
... ''}})




修改小刘的年龄为15　如果不存在该同学则添加，同时添加兴趣爱好和性别男

> db.class.update({name:'xiaoliu'},{$set:{age:15},$setOnInsert:{sex:'m',hobby:['sing','running']}},true)

　
删除小李兴趣中的第一项
 db.class.update({name:'xiaoliu'},{$pop:{hobby:-1}})



删除小红兴趣中的画画和唱歌

{$pullAll:{hobby:['draw','dance']}}



索引　

指建立指定键值及所在文档存储位置的对照清单，使用索引可以方便我们进行快速查找，减少遍历次数，提高查找效率　


ensureIndex() 
功能：　创建索引
参数：　索引域和索引选项　

根据name域创建索引
> db.class4.ensureIndex({name:1})

*１　表示正序索引　　
*-1 表示逆序索引　

查看集合中索引　

db.collection.getIndexes() 


自定义索引名称　

对域创建索引命名
db.collection.ensureIndex({},{name:'myIndex'})


删除索引

db.collection.dropIndex('index')
功能　删除索引　
参数　要删除的索引名称或者键值对



> db.class3.dropIndex('myIndex')


db.collection.dropIndexes()
功能：　删除所有索引

*_id是系统自动创建的主键索引　不能删除　




索引类型　

复合索引　
　　　　根据多个域创建一个索引　

　　　　复合索引创建一个索引表　比单个索引创建单个索引表更优

　　　　> db.class3.ensureIndex({name:1,age:-1},{name:'name_age'})

数组索引　子文档索引　

    如果对某个域的值为数组或者子文档的域创建索引，那么通过数组或者子文档中某一项进行查找也是索引查找

    e.g. 
    如果对score创建了索引那么该查找就是索引查找

    db.class3.find({'score.1:88'})


唯一索引　

　　　　创建索引的域要求值不能够重复　
　　　　　
　　　　　> db.class3.ensureIndex({age:1},{unique:true})

　　　　*当对某个域创建了唯一索引就不能插入重复的值


稀疏索引　　

　　　　db.class3.ensureIndex({age:1},{sparse:true})

索引约束　
　　　* 索引表需要占用一定的数据库磁盘空间　
   * 当对数据进行增　删　改等写入操作时索引也需要更新，降低了数据修改的

综上：　数据量较小时不适合创建索引，当数据库进行频繁的修改操作而不是查找操作时也不适合创建索引，
　　　　　　针对一个集合并不是创建索引越多越好　　　



聚合操作　

　　　　　　对文档的筛选结果进行整理统计　

db.collection.aggregate()
      
功能：　完成聚合操作　
参数：　聚合条件 --> 聚合操作符完成　


聚合操作符　

$group 分组聚合　需要配合具体的分组统计选项　

　　　　$sum : 求和　    

# > db.class3.aggregate({$group:{_id:'$age',num:{$sum:1}}})
# { "_id" : 24, "num" : 1 }   有一个24加１　
# { "_id" : 22, "num" : 1 }
# { "_id" : 21, "num" : 3 }
# { "_id" : 20, "num" : 3 }
# { "_id" : 12, "num" : 1 }
# { "_id" : 19, "num" : 2 }
# { "_id" : 2, "num" : 1 }

可以求个数　
> db.sanguo.aggregate({$group:{_id:'$country',num:{$sum:1}}})
{ "_id" : "魏国", "num" : 2 }
{ "_id" : "吴国", "num" : 1 }
{ "_id" : "蜀国", "num" : 4 }


也可以求和　

每个国家攻击力和
> db.sanguo.aggregate({$group:{_id:'$country',num:{$sum:'$gongji'}}})
{ "_id" : "魏国", "num" : 785 }
{ "_id" : "吴国", "num" : 100 }
{ "_id" : "蜀国", "num" : 1668 }


　　　　$avg 求平均

> db.sanguo.aggregate({$group:{_id:'$country',gongji:{$avg:'$gongji'}}})
{ "_id" : "魏国", "gongji" : 392.5 }
{ "_id" : "吴国", "gongji" : 100 }
{ "_id" : "蜀国", "gongji" : 417 }


　　　　$max 最大值

> db.sanguo.aggregate({$group:{_id:'$country',gongji:{$max:'$gongji'}}})
{ "_id" : "魏国", "gongji" : 666 }
{ "_id" : "吴国", "gongji" : 100 }
{ "_id" : "蜀国", "gongji" : 1000 }
$代表取该域的值　

    $min 最小值　



$project  修改文档的显示效果

> db.sanguo.aggregate({$project:{_id:0,name:1,gongji:1}})
{ "name" : "诸葛亮", "gongji" : 120 }
{ "name" : "司马懿", "gongji" : 119 }
{ "name" : "关羽", "gongji" : 188 }
{ "name" : "赵子龙", "gongji" : 360 }
{ "name" : "孙权", "gongji" : 100 }
{ "name" : "貂蝉", "gongji" : 666 }
{ "name" : " ", "gongji" : 1000 }



　第二种方法　
> db.sanguo.aggregate({$project:{_id:0,name:'$name',gongji:'$gongji'}})
{ "name" : "诸葛亮", "gongji" : 120 }
{ "name" : "司马懿", "gongji" : 119 }
{ "name" : "关羽", "gongji" : 188 }
{ "name" : "赵子龙", "gongji" : 360 }
{ "name" : "孙权", "gongji" : 100 }
{ "name" : "貂蝉", "gongji" : 666 }
{ "name" : " ", "gongji" : 1000 }


$match 
数据筛选　
$match 值得用法用query 

> db.sanguo.aggregate({$match:{gongji:{$gt:200}}})


$limit 
 筛选前几条文档　
 db.sanguo.aggregate({$limit:3})


$skip 
跳过几条文档显示后面的内容
db.sanguo.aggregate({$skip:3})


$sort

排序　


正序　　１　
> db.sanguo.aggregate({$sort:{gongji:1}})
{ "_id" : ObjectId("5ba2254c74a3072ca19e66c0"), "id" : 5, "name" : "孙权", "gongji" : 100, "fangyu" : 60, "sex" : "男", "country" : "吴国" }
{ "_id" : ObjectId("5ba2247f74a3072ca19e66bd"), "id" : 2, "name" : "司马懿", "gongji" : 119, "fangyu" : 25, "sex" : "男", "country" : "魏国" }
{ "_id" : ObjectId("5ba2247f74a3072ca19e66bc"), "id" : 1, "name" : "诸葛亮", "gongji" : 120, "fangyu" : 20, "sex" : "男", "country" : "蜀国" }
{ "_id" : ObjectId("5ba2247f74a3072ca19e66be"), "id" : 3, "name" : "关羽", "gongji" : 188, "fangyu" : 60, "sex" : "男", "country" : "蜀国" }
{ "_id" : ObjectId("5ba2254c74a3072ca19e66bf"), "id" : 4, "name" : "赵子龙", "gongji" : 360, "fangyu" : 88, "sex" : "男", "country" : "蜀国" }
{ "_id" : ObjectId("5ba2254c74a3072ca19e66c1"), "id" : 6, "name" : "貂蝉", "gongji" : 666, "fangyu" : 10, "sex" : "女", "country" : "魏国" }
{ "_id" : ObjectId("5ba225ad74a3072ca19e66c2"), "id" : 7, "name" : " ", "gongji" : 1000, "fangyu" : 99, "sex" : "男", "country" : "蜀国" }


聚合管道　

聚合管道指的是将上一个聚合的操作结果给下一个聚合继续操作　

db.collection.aggregate([{聚合},{},{}])   填写多个聚合操作　将上一个聚合的结果给下一个


> db.sanguo.aggregate({$match:{country:'蜀国'}},{$project:{_id:0}},{$sort:{gongji:1}})
{ "id" : 1, "name" : "诸葛亮", "gongji" : 120, "fangyu" : 20, "sex" : "男", "country" : "蜀国" }
{ "id" : 3, "name" : "关羽", "gongji" : 188, "fangyu" : 60, "sex" : "男", "country" : "蜀国" }
{ "id" : 4, "name" : "赵子龙", "gongji" : 360, "fangyu" : 88, "sex" : "男", "country" : "蜀国" }
{ "id" : 7, "name" : " ", "gongji" : 1000, "fangyu" : 99, "sex" : "男", "country" : "蜀国" }
> 


> db.sanguo.aggregate([{$group:{_id:'$country',num:{$sum:1}}},{$match:{num:{$gt:1}}}])
{ "_id" : "魏国", "num" : 2 }
{ "_id" : "蜀国", "num" : 4 }
．．

　