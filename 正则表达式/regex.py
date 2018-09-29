#! /usr/bin/env python3 

import re 


pattern = r'(ab)cd(ef)'
s = 'abcdefghigkihgfhabcdef'


#re模块直接调用
# l=re.findall(pattern,s)
# print(l)

#compile对象调用
# regex = re.compile(pattern)
# l=regex.findall(s)
# print(l)

#tarena@tedu:~/桌面/pythonNet/正则表达式$ ./regex.py 
# [('ab', 'ef'), ('ab', 'ef')]

#split 
# l=re.split(r'\s+','hello  world nihao china')
# print(l)


s = re.subn(r'\s+','#','hello world nihao china')
print(s)
