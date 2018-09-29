#存放文件　


# /home/tarena/桌面/MongoDB/

from pymongo import MongoClient
import gridfs

conn=MongoClient('localhost',27017)

db=conn.python

fs = gridfs.GridFS(db)

#打开文件１必须二进制　
f = open('/home/tarena/桌面/MongoDB/test2.docx','rb')

fs.put(f.read(),filename='mm.docx')

conn.close()


# for file in files:
#     #打印每个文件名称
#     print(file.filename)
#     if file.filename == 'mm.jpg':
#         with open(file.filename,'wb') as f:
#             #从数据库读取
#             data=file.read()
#             f.write(data)
# conn.close()