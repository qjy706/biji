from socket import *

s=socket(AF_INET,SOCK_STREAM)


#获取套接字地址族类型
print(s.family)

#:获取套接字类型
print(s.type)

#设置端口立即释放
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

#获取套接字选项值
print(s.getsockopt(SOL_SOCKET,SO_REUSEADDR))

s.bind(('0.0.0.0',9999))
#获取绑定地址
print(s.getsockname())

#获取套接字的文件描述符
#每一个IO事件操作系统都会分配一个不同的正整数作为编号，改正整数即为这个IO文件描述符
print(s.fileno())


#标准化输出！！！

s.listen(5)
c,addr=s.accept()
print('Connect from',c.getpeername())
d=c.recv(1024).decode()
print(d)



#设置套接字选项
# s.setsockopt(level,option,value)
# 功能：设置套接子选项,丰富或者修改套接字属性功能
# 参数：　level 选项类别　  SOL_
# 　　　　　　option 具体选项
# 　　　　　　value 选项值

# 需要在bind 之前设置


#s.getsockopt(level,option)
#功能：获取套接字选项值　
# 参数　：level 选项类别　SOL_SOCKET 
# 
# *如果要设置套接子选项，最好在创建套接字之后立即设置