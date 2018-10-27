import re

正则表达式　

动机　

１　文本处理已经成为计算机的常见工作之一　
２　对文本内容的搜索，定位，提取是逻辑比较复杂的工作　
３　为了快速解决上述问题，产生了正则表达式技术　


定义：　文本的高级匹配模式　，提供搜索，替代等功能．其本质是一系列由特殊符号组成的字串，这个字串即正则表达式　
赋予符号特殊含义　


匹配原理　：　由普通字符和特殊符号组成字符串，通过描述字符的重复和位置等行为，达到匹配某一类字符串的目的

目标：
１　熟练掌握正则表达式符号
２　实现基本的文本搜索，定位　，提取，理解正则用法　
３　能够使用re模块操作正则表达式　

特点：
* 方便文本处理　
* 支持语言众多　
*　使用灵活多样　

python ---> re模块　

regex = compile(r'')

re.findall(pattern,string)
功能：　使用正则表达式匹配目标字符串内容
参数：　pattern 正则表达式　
      string  目标字符串

返回值：　列表，列表中为匹配到的内容　　

元字符的使用　

1.普通字符　

元字符　：　a  b  c  
匹配规则　：　每个字符匹配对应的字符　

逐个为单位　　不是整体　　比如　hello 　h e l l o 
但是匹配的时候是以整体为单位　　
　
In [10]: re.findall('你好','你好悲剧')
Out[10]: ['你好']

In [9]: re.findall('ll','hell123 l1231321')
Out[9]: ['ll']



2 或　

元字符　：　
匹配规则　：　匹配　｜　两边任意一个正则表达式　

In [13]: re.findall('ab|bv','dasdsadsadsadaaasdsaabasdbv')
Out[13]: ['ab', 'bv']

In [3]: re.findall('abc|cde','abcdesadasdsaddad')
Out[3]: ['abc']
重复字符不会多余显示

３　匹配单个字符　

元字符　：　．　
匹配规则　：　匹配除换行外的任意字符

In [5]: re.findall('.d','abcdesadasdsaddad')
Out[5]: ['cd', 'ad', 'sd', 'ad', 'ad']

In [6]: re.findall('..d','abcdesadasdsaddad')
Out[6]: ['bcd', 'sad', 'asd', 'sad', 'dad']

In [7]: re.findall('..d|ab','abcdesadasdsaddad')
Out[7]: ['ab', 'sad', 'asd', 'sad', 'dad']

In [8]: re.findall('q.y','qjyqwewqeqweqqjyqqwewqqjy')
Out[8]: ['qjy', 'qjy', 'qjy']

In [10]: re.findall('q.y','qjyqwewqeqweqqjyqqwewqqj\ny')
Out[10]: ['qjy', 'qjy']
不能匹配换行


４　匹配开始位置　

元字符　：　＾　
匹配规则：　匹配目标字符串的开头位置　
放在正则表达式前部　

In [16]: re.findall('^qjy','qjyqwewqeqweqqjyqqwewqqj\ny')
Out[16]: ['qjy']

n [18]: re.findall('^qjy','qwewqeqweqqjyqqwewqqjny')
Out[18]: []




In [23]: re.findall('^qq|da|.s','qqadadasdsad')
Out[23]: ['qq', 'da', 'da', 'ds']



5 匹配结束位置
元字符　：　$　　放在表达式后面
匹配规则　：　匹配字符串的结束位置

In [26]: re.findall('ad$','qqadadasdsad')
Out[26]: ['ad']

６　匹配重复　

元字符　：　* 
匹配规则: 匹配前面的字符出现０次或多次　
fo* ---->  foooooooooo  f  fo 


In [31]: re.findall('da*','qqadadasdsad')
Out[31]: ['da', 'da', 'd', 'd']


7 匹配重复　

元字符　：　＋　
匹配规则　：　匹配前面的字符出现１次或多次　
fo+ --> fo fooooo
In [37]: re.findall('da+','qqadadadaaaaaasdsad')
Out[37]: ['da', 'da', 'daaaaaa']



匹配py文件　

'.+.py$'


8 匹配重复　

元字符　：　？　
匹配规则：　匹配前面的字符出现0次或者一次



9　匹配重复　
元字符　：　{n}
匹配规则　：　匹配指定的重复次数

In [44]: re.findall('da{2}','qqadadadaaaaaasdsad')
Out[44]: ['daa']


10 匹配重复　
元字符　：　{m,n}
匹配规则：　匹配前面的正则表达式　 m -n次　
fo{2,4} --> foo fooo foooo

In [47]: re.findall('da{1,2}','qqadadadaaaaaasdsad')
Out[47]: ['da', 'da', 'daa']


11 匹配字符集合　

元字符　：　［字符集］
匹配规则　：　匹配任意一个字符集中的字符　

[a-z]
[A-Z]
[_123-Z]

In [50]: re.findall('[asd]','qqadadadaaaaaasdsad')
Out[50]: 
['a','d','a','d','a','d','a','a','a','a','a','a','s','d','s','a','d']
是单个字符　不是一起的字符　

In [55]: re.findall('^[A-Z][a-z]*','Qqadadadaaaaaasdsad')
Out[55]: ['Qqadadadaaaaaasdsad']


re.findall('^[A-Z][a-z]*')
首字母的大写　其余的小写
这里+号不太好　_+号是一个或多个字符　



12. 匹配字符集
   [^...]
元字符　：　[^...]
匹配规则　：　字符集取非，除了列出的字符之外任意一个字符　

[^abc] --> 除　a b c 之外任意字符　

In [52]: re.findall('[^adc]','qqadadadaaaaaasdsad')
Out[52]: ['q', 'q', 's', 's']

除了a b c 之外一个或多个字符　
In [53]: re.findall('[^adc]+','qqadadadaaaaaasdsad')
Out[53]: ['qq', 's', 's']



13. 匹配任意（非）数字字符　

元字符　：　\d     \D
匹配规则　：　\d　　匹配任意数字字符　［０－９］
　　　　　　　　　　\D　　　匹配任意非数字字符　　［＾０－９］
In [60]: re.findall('\d{4}','Qqadadadaaaaaasdsad4545455471156')
Out[60]: ['4545', '4554', '7115']
匹配任意的数字字符　重复四次的



14.　匹配任意（非）普通字符　

元字符　: ＼w    ＼W 
匹配规则　：　＼w 　普通字符　　＼W 非普通字符　


15.匹配任意（非）空字符

元字符　：　\s 匹配任意空字符　[\r\t\n\v\f]
         \S 　匹配任意非空字符　



16 匹配规则：　匹配目标字符串的开头位置　

元字符　: \A   \Z 
匹配规则：　\A　　匹配字符串开头位置　　　^ 
        　\Z   匹配字符串结尾位置　　$ 



绝对匹配　：　正则表达式要完全匹配目标字符串内容　
　　　　　　　　　　在正则表达式开始和结束位置加上　^$(或者\A \Z)．这样
　　　　　　　　　　　正则表达式必须匹配整个目标字符串才有结果　
　　　　　　　　　　'^正则表达式$'

１７　匹配（非）单词边界　

元字符　：　\b     \B

匹配规则　：　\b  匹配单词边界位置　
　　　　　　　　　　　　　　普通字符和非普通字符交界认为是单词边界　


In [82]: re.findall(r'\b4','Qqadadadaaaaaasdsad 4545455471156')
Out[82]: ['4']

In [85]: re.findall(r'\D+\b\d+','Qqadadadaaaaaasdsad 4545455471156')
Out[85]: ['Qqadadadaaaaaasdsad 4545455471156']



r是原始字符串　　转义　


　　　　　　　　　　　\B　　　非单词边界位置　



正则表达式转义字符　

正则中的特殊符号　

. * + ? ^ $ [](字符集合) {}(匹配重复) ()  | \

正则表达式如果匹配特殊字符需要加＼　表达转义

     正则　　　　　　　　　　　　目标字符串
e.g. ＼$＼d+  ----->  $10

In [89]: re.findall('\$\d+','$10')
Out[89]: ['$10']


python中斜杠是有定义的　　两条斜杠是一条斜杠　又是一个转义的过程

               pattern           string
python        '\\$\\d+'           '$d'

In [89]: re.findall('\$\d+','$10')
Out[89]: ['$10']



In [100]: re.findall('\\n\d+','\n10')
Out[100]: ['\n10']


In [105]: re.findall('\\\n','\n')
Out[105]: ['\n']



raw字串：　原始字符串对内容不解释转义，就表达内容原本的意义　

In [105]: re.findall(r'\n','\n')
Out[105]: ['\n']

就想表示＼n 在前面加r


贪婪与非贪婪　

.*?就意味着匹配任意数量的重复，但是在能使整个匹配成功的前提下使用最少的重复
正则表达式有另一条规则，比懒惰／贪婪规则的优先级更高：最先开始的匹配拥有最高的优先权
贪婪模式　：　正则表达式的重复匹配总是尽可能多的向后匹配更多内容

 * + ? {m,n}

非贪婪(懒惰模式　)　：尽可能少的匹配内容

　
In [115]: re.findall(r'ab*?','abbbbbb')　　　　　　　　　　　　　　　
Out[115]: ['a']　　　要学会思考　

贪婪　----->　　非贪婪　　*? +? ?? {m,n}? 
　

正则表达式的子组

可以使用()为正则表达式建立子组，子组可以看做是正则表达式内部操作的一个整体
*子组是在正则表达式整体匹配到内容的前提下才会发生作用，他不影响正则表达式整体去匹配目标内容这一原则
返回第一个匹配到数值　，用group 则是按组来　
In [125]: re.search(r'(ab)+\d+','abababababababab1231213').group()
Out[125]: 'abababababababab1231213'　　只有整体匹配到才有作用　，如果后面不是数字就匹配不出来　



re.search(r'(ab)*','abababababababab').group()
'abababababababab'



子组所用　
１　　作为内部整体可以改变某些元字符的行为　

In [127]: re.search(r'\w+@\w+\.(com|cn)','abc@123.com,tet@123.cn').group()
Out[127]: 'abc@123.com'

In [128]: re.search(r'\w+@\w+\.(com|cn)','abc@123.cn').group()
Out[128]: 'abc@123.cn'
\w+@\w+\.(com|cn)


２　子组在某些操作中可以单独提取出匹配内容　

In [132]: re.search(r'(http|https|ftp)://\S+','http://www.baidu.com').group()
Out[132]: 'http://www.baidu.com'

In [133]: re.search(r'(http|https|ftp)://\S+','http://www.baidu.com').group(1)
Out[133]: 'http'

子组使用注意事项　

*一个正则表达式中可以有多个子组
*子组一般由外到内，由左到右称之为第一，第二，第三．．．子组　
*子组不能重叠，嵌套也不宜很多　

捕获组　和　非捕获组　

格式：　(?P<name>pattern)
n [7]: re.search(r'(?P<dog>ab)\S+','ababababababababdasd').group('dog')
Out[7]: 'ab'

通过名字获取匹配组



正则表达式设计原则　：

１　正确性，能正确匹配到目标内容
２　排他性，除了要匹配的内容，尽可能不会匹配与到其他内容　
３　全面性，需要对目标的各种情况进行考虑，做到不遗漏


In [14]: re.search(r'\d{17}(\w|\d)','34010319940416401x').group()
Out[14]: '34010319940416401x'



re模块　　

dir(re)

regex = compile(pattern,flags = 0)
功能：　生成正则表达式对象
参数: pattern   正则表达式　
　　　　　flags 功能标志位　丰富正则表达式的匹配功能　

返回值：　返回正则表达式对象　

re.findall(pattern,string,flags)
功能：　从目标字符串查找正则匹配内容
参数：　pattern 正则表达式　　
　　　　　　string 目标字符串
　　　　　　flags 标志位
返回：　返回匹配到的内容
　　　　　　如果正则有子组则只返回子组对应内容　


regex.findall(string,pos,endpos)
功能：　从目标字符串查找正则匹配内容　
参数：　string 目标字符串　
　　　　　　pos    匹配目标的起始位置　
　　　　　　endpos 匹配目标的终止位置　
返回值：　返回匹配到的内容
　　　　　　　　如果正则有子组则只返回子组对应内容

>>> regex = re.compile(r'.')#正则表达式　
>>> 
>>> 
>>> regex.findall('asdad',1,3)
['s', 'd']

regex.split(string)


re.split(pattern,string,flags=0)
功能：　根据正则匹配内容切割字符串
参数：　pattern string flags
返回值：　返回列表　列表中为切割的内容
>>> re.split(r'a','asddsadsadasd')
['', 'sdds', 'ds', 'd', 'sd']
>>> 




re.sub(pattern,replaceStr,string,max,flags)
功能：　替换正则匹配到的目标字串部分　
参数：　pattern 正则表达式　　
　　　　　　replaceStr  要替换的内容
　　　　　　string  目标字符串
　　　　　　max  最多替换几处　默认全部替换
　　　　　　flags  标志位　

返回值：　返回替换后的字符串　
s = re.sub(r'\s+','#','hello world nihao china')
hello#world#nihao#china
'\s+'匹配一个或多个空字符

re.subn(pattern,replaceStr,string,max,flags)
功能：　替换正则匹配到的目标字串部分　
参数：　pattern 正则表达式　　
　　　　　　replaceStr  要替换的内容
　　　　　　string  目标字符串
　　　　　　max  最多替换几处　默认全部替换
　　　　　　flags  标志位　

返回值：　返回替换后的元祖　,实际替换了几处
#匹配空字符
s = re.sub(r'\s+','#','hello world nihao china')
('hello#world#nihao#china', 3)
　　

re.finditer(pattern,string,flags)
功能：　替换正则匹配到的目标字串穿　
参数：　pattern 正则表达式　　
　　　　　　string  目标字符串

返回值：返回一个迭代对象，　迭代到的内容是一个match对象　


re.fullmatch(pattern,string,flags)
功能：　完全匹配目标字符串
参数：　pattern,string,flags
返回值：　返回匹配到的match对象，如果没匹配成功返回None



re.match(pattern,string,flags)
功能：　从开头位置匹配目标字符串
参数：　pattern,string,flags
返回值：　返回匹配到的match对象，如果没匹配成功返回None

obj = re.match(r'foo','foo,food on the table')
print(obj.group())



re.search(pattern,string,flags)
功能：正则表达式匹配目标字符串，只匹配第一处
参数：　pattern,string,flags
返回值：　返回匹配到的match对象
　　　　　　　　如果没有则返回None

regex.search(string,pos,endpos)

obj = re.search(r'(foo)+','foo,food on the table')
print(obj.group())

findall 有子组则返回子组匹配




compile对象属性　

 flags：　标志位　
 groupindex: 打印对应对象的正则表达式
 groups：　有多少子组　
 groupindex: 捕获组形成
 太突然　　
 pattern: 





*******************************************************************
match对象属性　
属性变量
pos　　　　　　　　匹配目标字符串的开始位置
endpos　　　　　匹配目标字符串的结束位置
re　　　　　　　　　正则表达式
string　　　　　目标字符串
lastgroup　　最后一组组名
lastindex　　一共几个子组，也可以说是最后一组是第几组　

属性方法
span()　　　　匹配内容的起止位置
start()　　　匹配内容的开始位置
end()　　　　　匹配内容的结束位置

group()
功能：　　获取match对象对应的内容
参数:  　默认为0 表示获取整个正则匹配的内容
　　　　　　　　如果为序列号或者子组名则为获取某个子组匹配的对应内容　
返回值：　返回得到的字串


groupdict()
功能：　获取捕获组字典　组名为键，对应内容作为值的字典　

groups()　　获取每个子组匹配内容

见　regex2.py





flags 参数使用　

re.compile  re.findall  re.search  re.match  
re.finditer  re.fullmatch  re.sub   re.subn   re.split

作用: 辅助正则表达式　，丰富匹配结果　

re.I == IGNORECASE  匹配时忽略字母的大小写　
re.S == DOTALL     作用于元字符.  使其可以匹配换行　
re.M == MULTILINE  作用于^ $ 使其可以匹配每一行开头结尾位置　
re.X == VERBOSE    可以给正则添加注释


使用多个标志位使用按位或连接　　｜　
e.g. 
flags = re.X　| re.I
　








 





　　　　　　



















