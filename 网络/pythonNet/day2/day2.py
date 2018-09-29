套接字传输注意事项

１监听套接字存在客户端即可发起连接，但是最终连接的处理需要accept进行处理


２如果连接的另外一段退出，则recv会立即返回空子串不再阻塞
BrokenPipeError


３　当连接的另一端退出时，再试图send发送就会产生BrokenPipeError


缓冲区目的是减少与磁盘的交互次数　提升读写效率　延长磁盘寿命
缓冲区作用　：协调收发速度，减少交互次数　

先通过send 发送到缓冲区，操作系统自动处理，接受的地方也有一个缓冲区，把内容接受
当缓冲区满的时候　send就会阻塞　
当接受缓冲区没有消息的时候　，　recv也会阻塞等待　　send recv也是阻塞函数

send recv实际上是和缓冲区进行交互，发送缓冲区满时就无法发送，接收缓冲区满时recv才阻塞

tcp 粘包：（udp不会产生粘包）
产生原因　
tcp　套接字以字节流方式传输，没有消息边界，发送和接收并不能保证每次发送都及时的被接受　
根据缓冲区大小设置的　　

影响：如果每次发内容表达一个独立的含义此时可能需要处理粘包防止产生歧义

处理方法
1,每次发送的消息添加结尾标志（人为增加消息边界）
２，发送数据结构体
３，协调收发速度，每次发送后都预留接收时间　sleep




UDP套接字编程　

socket 
    |
bind 
   |            ----- |
recvfrom     |
  |                  |
sendto    ------


创建数据包套接字　
sockfd=socket(AF_INET,SOCK_DGRAM)

sockfd=socket(AF_INET,SOCK_DGRAM)

 绑定地址
sockfd.bind(())

消息的收发
data,addr = sockfd.recvfrom(buffersize)


数据报大于字节则会丢失部分信息　
** 一次接收一个数据报，如果数据报大小大于　buffersize则会丢失部分消息
功能：　接收UDP消息　
参数：　每次最多接受多大的消息　
返回值：　data 接收到的数据　
　　　　　addr  消息发送端的地址　

UDP 也是有发送接收缓冲区的　


sockfd.sendto()

功能：发送udp消息　
参数：data 发送的消息　bytes 格式　
　　　addr 目标地址　端口

返回值：　发送的字节数　

４　关闭套接字　
socket.close()



udp 客户端流程

１，　创建套接字　socket(AF_INET,SOCK_DGRAM)

2.消息收发　
　recvfrom/sendto 

3关闭套接字　
　close()


cookie 
 
1,sys.argv 属性　
功能：获取命令行参数,得到一个列表
命令本身是　argv[0]
后面的参数从argv[1]开始，默认以空格分隔，使用引号引起来的内容算作一个整体　
命令行参数都已字符串放入列表　

python3 客户端.py 192.1.1.1  8888
['客户端.py','192.1.1.1','8888']

2. 在程序第一行加#! /usr/bin/env python3
　　　添加程序的执行权限　
　　　chmod 755 file.py 
   修改后即可通过　./file.py 运行程序　 




TCP 和 UDP 区别　

１．流失套接字使用字节流的方式传输，数据报套接字以数据报形式传输数据
２　TCP会有粘包现象，UDP有消息边界不会形成粘包　
３　TCP可以保障数据传输完整性，UDP则不保证　
４　TCP需要进行listen accept 操作　，UDP 不需要　
５　tcp 收发消息使用连接套接字　recv send 
   udp 使用recvfrom sendto 
6 循环收发　udp 多个客户端可以收发　


补充函数　

sendall(data)
功能：发送tcp 消息
参数：要发送的内容，　bytes格式　
返回值：　成功返回None 失败产生异常　




套接字对象　

s代表一个套接字



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



设置套接字选项
s.setsockopt(level,option,value)
功能：设置套接子选项,丰富或者修改套接字属性功能
参数：　level 选项类别　  SOL_
　　　　　　option 具体选项
　　　　　　value 选项值

需要在bind 之前设置


s.getsockopt(level,option)
功能：获取套接字选项值　
参数　：level 选项类别　SOL_SOCKET 

*如果要设置套接子选项，最好在创建套接字之后立即设置



s.setblocking(False)


udp应用之广播：

广播　：　一点发送　多点接收

广播地址：　一个网段内有一个制定的广播地址　，是该网段的最大地址．
176.8.18.255　　
192.168.1.255

tcp　应用值之http传输

http协议：超文本传输协议　是一个应用层协议　
用途：　网页数据的传输　
　　　　　　数据传输方法：


特点：
１，应用层协议，传输层使用tcp服务
２，简单，灵活，多种语言都有http相关操作接口
３，无状态协议，即不记录用户传输的信息
４，http1.1 支持持久连接　

一端通过http请求的格式发送具体请求内容，另一端接受http请求，按照协议格式解析．
获取真实请求后按照http协议响应格式组织恢复内容，回发给请求方，完成一次数据交互


http请求　(request)
请求格式：

请求行 : 具体的请求类别和请求内容　
　　　　格式：　GET   空格　　　　　 / 　　　 空格    HTTP/1.1 
          请求类别　　　　　　请求内容　　　　　　　　协议版本

　　　请求类别：　　表示请求的种类　
　　　　　　　      GET   :    获取网络资源　　　　www.baidu.com 就是获取网络资源
             POST　　　　　　　提交一定的附加信息，得到返回结果
             HEAD　　　　　　　获取相应头
             PUT　　　　　　　　更新服务器资源
             DELETE　　　　　删除服务器资源
             CONNECT 　　　
             TRACE 　　　　　用于测试
             OPTIONS　　　　获取服务器性能信息

请求头　：  对请求内容的具体描述信息　（键值对形式）　

空行
请求体: 请求参数或者是提交内容　


http响应　(response)

响应格式



响应行　：　反馈相应的情况　
　　　　　格式：　HTTP/1.1        200       　　　　　ok 
　　　　　　　　　　　　协议　　　　　　　　　　　响应码　　　　　　　　附加信息

　　　　　响应码　：响应码的具体情况　
　　　　　　　　　　　　1xx : 提示信息，表示请求成功　
            2xx　：响应成功
            3xx　：响应需要重定向　
            4xx　：客户端错误　
            5xx　：服务端错误
    常见响应码：　２００　成功
    　　　　　　　　　　　４０４　请求内容不存在
    　　　　　　　　　　　４０１　没有访问权限
    　　　　　　　　　　　５００　服务器发生未知错误
    　　　　　　　　　　　５０３　暂时无法执行　

响应头　：对响应内容的具体描述　

空行　/r/n

响应体 : 返回给请求端的具体内容　

要求:
    1.什么是http 协议　
   　２．请求的格式和每一个部分的功能　
    ３．响应的格式和每一部分功能
    ４．常见的请求类型和响应码代表什么　
    
from socket import *
#创建tcp套接字
s=socket()
s.bind(('0.0.0.0',8888))
s.listen(5)
while True:
    c,addr=s.accept()
    print('connect from',addr)

    data=c.recv(4096)
    print('*****************')
    print(data)#浏览器发来的http请求
    print('*****************')
    c.close()

s.close()