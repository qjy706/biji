import re 
finditer
it = re.finditer(r'\d+','2008-2018 10年，中国发生了翻天覆地的变化')
for i in it:
    print(i.group())

findmatch
# 因为有#号　不能完全匹配　　会返回none 需要用try处理
try:
    obj = re.fullmatch(r'\w+#','abcdef123#')
    print(obj.group())
except AttributeError as e:
    print(e)


#match  只能匹配起始位置的内容
obj = re.match(r'foo','foo,food on the table')
print(obj.group())


#search
obj = re.search(r'(foo)+','foo,food on the table')
print(obj.group())