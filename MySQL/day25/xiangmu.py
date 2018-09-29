# 7c4a8 d09ca 3762a f61e5 95209 43dc2 6494f 8941b   

from mysqlpython import SJK
from hashlib import sha1
username=input('请输入姓名')
password=input('请输入密码')
#给密码加密
s1=sha1()#创建sha1 加密对象
s1.update(password.encode('utf-8'))
password2=s1.hexdigest()#返回十六进制加密结果
# print(password2)

#和数据库进行匹配
mysql=SJK('db4')
sql_select = 'select password from user where username=%s'

result=mysql.getall(sql_select,[username])
print(result)
#正确会返回一个大元组里面套着一个小元组　里面是密码的加密形式

#错误就是空 用户名错误时候
if len(result) == 0:
    print('用户名不存在')
elif password2 == result[0][0]:#大元组里面是小元组,小元组里面是字符串
    print('登录成功')
else:
    print('密码错误')


