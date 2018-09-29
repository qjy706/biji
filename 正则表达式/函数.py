函数　function
优点：
　　　简化代码结构，增加代码的复用度；
　　　修改某个功能或者调试时，修改相应函数．

作用：
　　　用于封装语句块，提高代码的重用性．
　　　定义用户级别的函数．

def　语句　
　　语法：
　　　　　def 函数名（行参列表）
　　　　　    语句块
　　　　　　return 表达式（表达式可以不写，默认返回None)
          作用：创建一个函数，并用函数名变量绑定这个函数．
　　
          语法说明：
　　　　　　　1, 函数名是变量，他用于绑定语句块．
　　　　　　　2, 函数有自己的名字空间，在函数外部不可以访问函数内部的变量，在函数内部可以访问函数外部的变量．（要让函数处理外部的数据需要用到参数给函数传入一些数据）
　　　　　　　３，函数不需要传入参数时，行参列表可以不写．
　　示例：
　　　　　def say_hello():      say_hello是自定义的一个变量，必有左
                          print(‘hello world’)  　右括号，def作用是打包，形成一个　              
                          print(‘hello tarena’)　　大框架，变量say_hello绑定print
                          print(‘hello everyone’)　　语句块
                       say_hello()   　　当调用函数时，函数才会执行，括号是让　　　　　　　　　　　
　　　　　　　　　　　　　　　　语句块去执行


函数调用：
函数名（实际调用传递参数）　　是实参给行参赋值的过程
说明：
　　　函数调用是一个表达式
　　　如果函数内部没有return语句，函数调用完毕后返回None对象
　　　如果函数需要返回其他对象，需要用到return语句

练习：写一个函数，print_even，传入一个参数n代表终止函数，打印　2，4，6，8，n之间的所有偶数．
　　　
def print_even(n):  　#自定义一个变量　print_even
    for i in range(1,n+1):   #def 形成一个大框架　，　整体打包变量绑定  的语句块
         if i % 2 == 0:
             print(i)
print_even(8)             函数名绑定的语句块执行，出现的是偶数，语句块　　　　　　　　．　　　　　　　　　则是函数名下的各种语句，运算
　

return 语句：
　　　语法：
　　　　　　return　［表达式］　　注！　［］可省略

　　　作用：
　　　　　　一般用于结束语句，表达式是返回给函数调用者的信息，表达式不写默认None
　　　　　　用于函数，结束当前函数的执行，返回到调用该函数的地方，
同时返回一个对象的引用关系．

　　　语句说明：　
　　　　　　1   return　语句后跟的表达式可以省略，省略后相当于
                                             return None 
　　　　　　2   如果函数内没有return语句，则函数执行完最后一条语　　　　句后返回None　（相当于最后加了一条　return None语句）
　　　　　def say_hello():     
                          print(‘hello world’)  　　              
                          print(‘hello tarena’)　
                          return 　
                          print(‘hello everyone’)　　
                       say_hello()   