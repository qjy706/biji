IO input output 
在内存中存在数据交换的操作都可以认为是IO操作　
在内存中存在数据交换的操作都可以认为是IO操作
和终端交互　：input print 
和磁盘交互　：　read write 
和网络交互　： recv send 

send recv都是与缓冲区交互

IO密集型程序　：在程序执行过程中存在大量IO操作，
　　　　　　　　　　　　　而cpu运算操作较少．消耗cpu较少　，运行效率较低

IO问题：　数据传输读写速度比较慢
　　　　　　　　易遇到阻塞



计算密集型程序（ＣＰＵ密集型程序）：
在程序执行中cpu运算较多，IO操作相对较少

IO分类　
阻塞IO　　　　　　　　　非阻塞IO   　　　　　　　　　IO多路复用

阻塞IO :  阻塞IO是IO的一种默认形态，是效率较低的一种IO．

input sleep 等待执行　就是一种阻塞IO 达到某种条件继续运行
在内存中进行阻塞操作

阻塞情况　　某些条件没有达成造成的阻塞

1..因为某种条件没有达成造成的阻塞

e.g.  accept input recv send sleep

2..处理IO数据传输时间较长形成的阻塞　
　　　　e.g.   网络传输过程，文件读写过程

   
非阻塞IO ：

通过修改IO事件的属性　使其变为非阻塞状态
（让一些条件阻塞函数不再阻塞）

非阻塞IO往往和循环判断一起使用　



超时检测：　 timeout

　　　　　　　将原本阻塞的函数设置一个最长阻塞时间，
　　　　　　如果时间内条件达成，如果仍然阻塞　则视为超时　
　　　　　　继续向下运行或产生异常　

s.settimeout(sec)
设置套接字的超时间　

s.settimeout(sec)
# select(...[timeout])   join()

io在内存中进行数据交换

IO多路复用　

有几个io事件，　１，２，３　
１，每个io条件相互之间没有影响　（连接套接字跟每个客户端都会创建一个连接套接字　互相没有影响）
２，三个io 事件随即发生随机阻塞　



如果把１，２，３放进内核中，调用哪个就运行哪个返回应用程序


定义：同时监控多个io事件，当哪个io事件准备就绪，就执行哪个io事件，
　　　　　以此形成可以同时操作多个io的行为
　　　　　避免一个io阻塞，造成所有io都无法执行　

io准备就绪：　是一种io必然要发生的临界状态　

１，将io设置为关注io　
２，将关注io提交给内核监测　
３，处理内核给我们反馈的准备就绪的io　

具体方案　select poll epoll 

select  --->  windows linux unix 

poll --->  linux unix 

epoll --->  linux unix 

import select  

rs,ws,xs=select(rlist,wlist,xlist[,timeout])
功能：监控io事件，阻塞等待io事件发生　

参数：rlist  列表　存放我们监控等待处理的io事件

     wlist　　列表　send write 可以主动操作的io事件 客户端连接套接字既可以收　也可以主动操作

     xlist　　列表　我们要关注出错处理的io 

     timeout 超时时间　　

返回值：rs 列表　rlist中准备就绪的io 
       ws 列表　wlist中准备就绪的io 
       xs 列表　xlist中准备就绪的io

注意：　
１．　wlist 中如果有io事件则select 立即返回为ws
2.  在处理io过程中不要处理一个客户端长期占有服务端使服务端
　　　　无法运行到select 的情况　
３．io多路复用占用计算机资源少，io效率高




位运算


整数之间进行二进制位运算
＆　按位与
｜　按位或
＾　按位异或
<< 左移
>> 右移　

11 1011 
14 1110

11 & 14  1010    10  一0则０
11 | 14 　1111    15　　一一则一
^ 　　　　　　　0101    5    相同为０不同为１

11 << 2  101100  44    11*2*2 
11 >> 2  10      2     有点像地板除

端口重用　　按位与的应用




poll 
１，将io设置为关注io　
２，将关注io提交给内核监测　
３，处理内核给我们反馈的准备就绪的io　

1,创建poll对象

p=select.poll([timeout])

2.添加注册事件　

p.register(s,POLLIN|POLLERR)

POLLIN  　POLLOUT 　POLLERR　　POLLHUP 　　　　POLLNVAL 
rlist    　wlist　   xlist    　断开　　　　　　　无效数据

p.unregister(s)  从关注事件中移除　


3. 阻塞等待IO发生　
events=p.poll()
功能：监控io事件，阻塞等待io事件发生　
返回值：　events 是一个列表，列表中每一个元素都是一个元祖
　　　　　　　代表一个发生的io事件　
[(fileno,　　　　　　　　　　　　　　　　event),(),().....]
就绪IO的文件描述符　　　　　　　　　　　具体就绪事件

整型的文件描述符

*需要通过整型文件描述符(fileno)找到对应的io对象　
{s.fileno():s} 


