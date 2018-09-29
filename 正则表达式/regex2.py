import re 

p = r'(?P<dog>ab)cd(?P<pig>ef)'
regex = re.compile(p)



#获取match对象
match_obj = regex.search('abcdefgfdsf',pos=0,endpos=6)

print(match_obj.pos)#匹配目标字符串的开始位置
print(match_obj.endpos)#匹配目标字符串的结束位置
print(match_obj.re)#正则表达式
print(match_obj.string)#目标字符串
print(match_obj.lastgroup)#最后一组组名
print(match_obj.lastindex)#一共几个子组，也可以说是最后一组是第几组　

print('******************************************************')
print(match_obj.start())#匹配内容的开始位置
print(match_obj.end())#匹配内容的结束位置
print(match_obj.span())#匹配内容的起止位置
print(match_obj.group())
print(match_obj.group(1))
print(match_obj.group('dog'))
print(match_obj.groups())
print(match_obj.groupdict())




0
6
re.compile('(?P<dog>ab)cd(?P<pig>ef)')
abcdefgfdsf
pig
2
******************************************************
0
6
(0, 6)
abcdef
ab
ab
('ab', 'ef')
{'dog': 'ab', 'pig': 'ef'}
