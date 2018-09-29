from pymongo import MongoClient

#创建数据库连接
conn = MongoClient('176.8.18.212',27017)

#创建数据库对象绑定的是一个属性　
db = conn.stu

#创建集合对象
# 库　集合　文档　
myset = db.class5#conn.stu.class5
# print(dir(myset))
# myset.insert({'name':'张铁林','king':'乾隆'})
# myset.insert([{'name':'张国立','king':'康熙'},{'name':'陈道明','king':'康熙'}])
# myset.insert([{'name':'陈建斌','king':'雍正'},{'name':'唐国强','king':'雍正'}])
# myset.save({'_id':1,'name':'聂远','king':'乾隆'})


#查找操作　
# cursor=myset.find({},{'_id':0})
# print(cursor)
# for i in cursor:
#     # print(i)
#     print(i['name'],'-------',i['king'])

# one = myset.find_one({'name':'张铁林'},{'_id':0})
# print(one)

#操作符使用　
myset1 = db.class

# query={'$or':[{'age':{'$lt':25}},{'sex':'w'}]}
# cursor = myset1.find(query,{'_id':0})

# for i in cursor:
#     print(i)


#游标包含三条数据,可以跟着后面继续操作　limit(3).skip(2)
# for i in cursor.skip(2).limit(3):
#     print(i)

#固定格式
# for i in cursor.sort([('age',1),('name',-1)]):
#     print(i)
#

#修改年龄
# myset1.update({'name':'Tom'},{'$set':{'age':'30'}})

# myset.update({'name':'梁家辉'},{'$set':{'King':'咸丰'}},upsert=True)

# myset.update_one({'King':'康熙'},{'$set':{'KingName':'玄烨'}})


#删除操作　

# myset.remove({'KingName':'玄烨'})


#删除一个符合条件的文档
# myset.remove({'King':'康熙'},multi=False)


#复合操作　

myset.find_one_and_delete({'King':'咸丰'})
 




#关闭连接
conn.close()