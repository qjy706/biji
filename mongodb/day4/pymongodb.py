from pymongo import MongoClient
conn=MongoClient('localhost',27017)
db=conn.grade
myset=db.class3

# 索引操作　

#想创建索引的域

#默认创建正向索引
# index = myset.ensure_index('name')
#打印索引名称
# print(index)

#创建逆向索引
# index = myset.ensure_index([('name',-1)])

#获取当前集合中索引　
# for i in myset.list_indexes():
#     print(i)

#删除所有索引
# myset.drop_indexes()

#通过索引名称删除索引
# myset.drop_index('name_1')

#复合索引
# myset.ensure_index([(('name',1),('age',-1))])

#唯一索引
# myset.ensure_index('name',name='MyIndex',unique=True)

#稀疏索引　
# myset.ensure_index('age',sparse = True)

myset1=db.class1


#聚合
# L=[{'$group':{'_id':'$King','count':{'$sum':1}}},{'$match':{'count':{'$gt':1}}}]
# cursor = myset.aggregate(L)
# for i in cursor:
#     print(i)


#grade库　下面class 
#为所有人添加score域，值为{'chinese':88,'match':77,'english':78}
from random import randint

cursor = myset1.find()

for i in cursor:
    print(i)
    myset1.update({'_id':i['_id']},{'$set':{'score':{'chinese':randint(60,80),'match':randint(60,80),'english':randint(60,80)}}},multi = True)













conn.close()