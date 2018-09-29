查看班级中年龄大于１０岁学生信息
> db.class.find({age:{$gt:10}},{_id:0})
　
查看班级中年龄在８－１１岁之间的学生信息　
> db.class.find({age:{$in:[8,11]}},{_id:0})
> db.class.find({age:{$gt:8,$lt:11}},{_id:0})


查看班级中年龄１０岁且为男生的学生信息　
> db.class.find({age:10,sex:'m'},{_id:0})


查看班级中小于７岁或者大于１４岁的学生
多个条件用中括号
> db.class.find({$or:[{age:{$lt:7}},{age:{$gt:14}}]},{_id:0})

查看班级中年龄为８岁或者１１岁的学生
> db.class.find({$or:[{age:8},{age:11}]},{_id:0})


找到有２项兴趣爱好的学生　

> db.class.find({hobby:{$size:2}},{_id:0})


找到兴趣中有draw的学生

> db.class.find({hobby:'draw'},{_id:0})


找到既喜欢画画又喜欢跳舞的学生

> db.class.find({hobby:{$all:['draw','dance']}},{_id:0})




统计兴趣有４项的学生人数　
> db.class.find({hobby:{$size:4}},{_id:0}).count()



找出本班年龄第二大的学生　

> db.class.find({},{_id:0}).sort({age:-1})[1]

> db.class.find({},{_id:0}).sort({age:-1}).skip(1).limit(1)

查到本班学生兴趣爱好涵盖哪些方面

> db.class.distinct('hobby')




找到年龄最大的三个学生

> db.class.find({},{_id:0}).sort({age:-1}).limit(3)




删除所有年龄大于１６或者小于７岁的学生除非他的爱好有三项以上　
> db.class.remove({$or:[{age:{$gt:16}},{age:{$lt:7}},{hobby:{$size:2}}]})






> db.sanguo.insert([{id:1,name:'诸葛亮',gongji:120,fangyu:20,sex:'男',country:'蜀国'},
... {id:2,name:'司马懿',gongji:119,fangyu:25,sex:'男',country:'魏国'},
