import re 

# s = 'hello world'
# #单个字符对应　，　但是最后是整体匹配　
# p = r'Hello' 
# #大小写不能相互匹配
# regex = re.compile(p,flags = re.I)
# #忽略大小写　
# s=regex.search(s).group()
# print(s)



s = '''hello world
hello kitty 
你好,北京'''


p = r'^h.+'
# p = r'^你好'
# 

#忽略大小写　
#regex = re.compile(p,flags =re.I)
regex = re.compile(p,flags =re.I|re.S)
# regex = re.compile(p,flags =re.M)

try:
    s = regex.search(s).group()
except:
    print('no')
else:
    print(s)