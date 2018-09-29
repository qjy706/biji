回顾　

信号处理　　signal() 
异步通信方式　同步执行　异步执行　

信号量　semaphore()



4 什么是线程　
t=threading.Tread()
t.start()
t.join()

进程

p=multiprocessing.Process(target= xxx)

进城线程的区别和联系　os Tread Process

１，两者都是多任务编程方式，都能够使用计算机的多核资源
２．进程的创建删除消耗的计算机资源比线程要多
３．进城空间独立，数据相互不干扰，有专门的IPC（进程通讯）Pipe Queue Value，线程使用全局变量进行通信　
４　一个进城可以创建多个线程分支，两者之间存在包含关系　
５　多个线程共用线程的资源，在资源操作时往往需要同步互斥
６　进程线程在系统中都有自己特有的属性，ID，代码段，栈区（运行的内存区域）的等资源

使用场景
＊　需要创建较多并发，同时任务关联性比较强的时候，一般用多线程
＊不同的任务模块可能更多使用进程　
＊使用进程线程需要考虑数据的处理复杂度，比如进程间通信是否方便，同步互斥是否过于复杂



同步是复杂的互斥　互斥是特殊的同步　  同步是按照某种顺序依次完成（其他也是在等待）　互斥是一个进程在运行时　其他等待　
临界资源是是指允许一个资源访问的资源
临界区是程序代码
可以用锁来限制程序竞争　　一个程序完成之后才进入下一个程序　
互斥是一个进程执行　其他进程等待　同步也是互斥，但是必须按照一种特殊的顺序运行，以实现程序的特殊功能
互斥锁 同时只允许一个线程更改数据，
Semaphore是同时允许一定数量的线程更改数据 ，比如厕所有3个坑，那最多只允许3个人上厕所，后面的人只能等里面有人出来了才能再进去，如果指定信号量为3，那么来一个人获得一把锁，计数加1，当计数等于3时，后面的人均需要等待。一旦释放，就有人可以获得一把锁

要求：
１．进程线程的区别和联系　进程独立存在　信息独立　线程在进程中　
２．进程间通信方式都知道哪些，有什么特点 管道　共享内存　消息队列
３．同步互斥意义是什么，什么情况下用
４．给一个情形，分析下用进程还是线程
５．一些常见概念挖掘，僵尸进程   　进程状态(就绪态，运行态，等待态）　GIL　


服务器模型
硬件服务器　　主机　集群

厂商　ibm 惠普　联想　


软件服务器　　编写的服务端应用程序，在硬件服务器上运行，一般依托于操作系统，给用户提供一套完整的服务

httpserver --> 处理http请求

webserver -- > 网站后端应用服务器程序

邮箱服务器　-- > 邮件处理　

ftp文件服务器　--> 文件的上传下载　

功能：网络连接　逻辑处理　数据交互　数据传输　
　　　　　协议的实现　

结构：　c/s 客户端服务器模型　
　　　　　 b/s 浏览器服务器类型
　
服务器目标：　处理速度更快，并发量更高，　安全性更强　

硬件：　更高的配置　，更好的集成分部技术　更好的网络优化　和　网络安全技术　

软件：　占用资源更少　，运行更稳定，算法更优良　安全性更好，并发性更高　更容易扩展
．
循环模型　：　循环接收客户端请求　，处理请求．同一时刻只能处理一个请求，处理完毕后再处理下一个
　　　　　　　　　　优点　实现简单　占用资源少　
　　　　　　　　　　缺点　无法同时处理多个客户端任务　
　　　　　　　　　　适用情况：　处理的任务可以短时间完成，不需要建立并发，更适合udp使用　

并发模型　：　能够同时处理多个客户端请求　
　　　　　　　　　　　　　　　io并发　　io多路复用
                   优点　　单进程程序　资源消耗少　io处理速度快　
                   缺点　　不能适用cpu密集型程序



　　　　　　　　　　　多进程／多线程并发：　为每个客户端创建单独的进程线程，执行请求

　　　　　　　　　　　　　优点：　每个客户端可以长期占有服务器运行程序
　　　　　　　　　　　　　　　　　　　　能够使用多核资源，可以处理io或者cpu运算
　　　　　　　　　　　　　缺点：　消耗系统资源高　


多进程并发模型　：　

使用fork实现多进程并发　
１，创建套接字，绑定监听
２，等待接收客户端请求
３，　创建新的进程处理客户端请求（为每个客户端创建单独的进程线程，执行请求）
４，原有进程继续等待新的客户端连接
５，如果客户端退出则关闭子进程



ftp 文件服务器　

项目功能
＊　服务端　和客户端　，要求启动一个服务端可以同时处理多个客户端请求　
＊功能：　可以查看服务端文件库中所有的普通文件　
　　　　　　　从客户端可以下载文件库的文件到本地　
　　　　　　　可以将本地文件上传到服务端文件库　
　　　　　　　　退出
＊客户端使用print在终端打印简单的命令提示　，通过命令提示发起请求　

技术分析　　（fork　tcp 并发）

每个功能单独封装　整体功能写在一个类中　

如何搭建整日架构　完成网络通讯
　　　　　　　　　　

功能分析　
１，　获取文件列表　
　　　　客户端，　＊　发送请求
　　　　　　　　　　　　＊　得到回复判断能否获取列表　
　　　　　　　　　　　　　　接收文件名称列表
　　　　客户端　　＊接受请求　
　　　　　　　　　　　＊判断请求类型　
　　　　　　　　　　　＊判断能否满足请求　回复信息确认
　　　　　　　　　　　＊执行请求发送文件列表　



os.listdir(path)　获取目录中文件列表
os.path.isfile() 判断是否为普通文件
os.path.isdir() 判断是否为目录




文件的下载
　　　客户端：　＊发送请求　（文件名）
　　　　　　　　　　＊　得到回复判断能否
　　　　　　　　　　＊　下载文件　

服务端　　　　　　　接受请求　
　　　　　　　　　　　　判断请求类型　
　　　　　　　　　　　　判断能否满足请求，回复信息确认
　　　　　　　　　　　执行请求发送文件　




完成文件服务器的上传功能　

复习HTTP协议　和　HTTPserver第一版　

进程线程网络总结，难点程序在写一遍　