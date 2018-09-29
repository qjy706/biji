#小文件存储方案
#直接转换为二进制格式插入到数据库　


from pymongo import MongoClient
import bson.binary

# conn = MongoClient('localhost',27017)

# db = conn.small
# myset = db.MM

# f = open('','rb')
# #将图片转换为可存储的二进制格式　

# content = bson.binary.Binary(f.read())

# #插入文档　
# myset.insert({'filename':'mm.jpg','data':content})


# f.close()




#小文件提取出来　

#find返回值是一个游标　，find_one是返回值　直接用　
img = myset.find_one('filename':'mm.jpg')

#将内容写入到本地
with open('mm.jpg','wb') as f:
    f.write(img['data'])

conn.close()
