１如果子进程从父进程拷贝对象，对象和网络或者文件相关联，
那么父子进程会使用同一套对象属性，相互有一定的关联性　

２，如果在子进程中单独创建对象，则和父进程完全没有关联

#属性
p.is_alive() 判断进程生命周期状态，处于生命周期得到True
　　　　　　　　　　　　　否则返回False 

p.name 进程名称　默认为Process-1 
p.pid 　进程的PID号　
pcb 进程控制块　

p.pid 进程的pid号
os.getpid()　当前进程pid 
os.getppid()父进程pid 



p.daemon = False　　　join 是一个阻塞函数　会影响到主进程的运行　可以用守护　主进程退出　紫禁城也退出　
默认状态下是False 此时主进程退出不会影响子进程执行　
如果设置为True 则子进程会随着主进程结束　而结束　
必需在start 之前设置　　
一般不和join一起使用

线程是　t.setDaemon(True)
进程是　


创建自定义进程类

１　继承Process

2  编写自己的__init__,同时加载父类的init方法　

3 　重写run方法，可以通过生成的对象调用start 自动运行　

多进程：　
优点：　可以使用计算机多核，进行任务的并发执行，提高执行效率
　　　　　　空间独立，数据安全
　　　　　　运行不受其他进程影响，创建方便

缺点：　进程的创建和删除消耗的系统资源较多　



进程池技术：　
产生原因　：如果有大量的任务需要多进程完成，则可能需要
　　　　　　　　　　频繁的创建删除进程，给计算机带来较多的资源消耗．
　　　　　　　　　普通的进程创建删除不太合适

原理：创建适当的进程放入进程池，用来处理待处理事件，
　　　　　处理完毕后进程不销毁，仍然在进程池中等待处理其他事件
　　　　　进程的复用降低了资源的消耗　

使用方法　
１，创建进程池　，在池内放入适当的进程，  p = Pool(4)  p.apply_async(func,args=(a,))  p.close() p.join()
２，将事件加入到进程池等待队列
３，不断取进程执行事件，直到所有事件执行完毕
４，关闭进程池，回收进程　

from multiprocessing import Pool

multiprocessing import Pool


Pool(processes)
功能：　创建进程池对象
参数：表示进程池中有多少进程　
跟信号量很像　

pool=Pool(n)
pool.apply_async(fun,args)

变量=pool.apply_async(func,args,kwds)
功能：将事件放入到进程池队列　
参数：func 事件函数　
　　　　　args 以元祖形式给func传参　 (i,)
　　　　　kwds 以字典形式给func传参　

#关闭进程池
pool.close()
功能：关闭进程池


pool.join()
功能：　回收进程池

pool.map(func,iter)
功能：　将要做的事件放入进程池
参数：　func 要执行的函数　
　　　　　　iter 可迭代参数　
返回的是一个可迭代的列表　

信号量　
sem = Semaphore(3)

    sem.acquire()
    sem.release()

进程间通信　（IPC）

原因：　进程空间相互独立，资源无法相互获取，此时在不同进程间
　　　　　通信需要专门方法

进程间通信方法：管道，消息队列，共享内存，信号，信号量，套接字

fd1,fd2 = Pipe()
fd1.send
fd2.recv

管道通信　　Pipe 
通信原理：　在内存中开辟管道空间，生成管道操作对象，
　　　　　　　　　多个进程使用＇同一个＇管道对象进行操作即可实现通信


fd1,fd2 = Pipe(duplex = True)
功能　：　创建管道
参数　：　默认表示双向管道　
　　　　　　　如果设置为False 则为单项管道　

返回值：　表示管道的两端　
　　　　　　　　如果是双向管道，都可以读写
　　　　　　　如果是单项管道，则fd1 只读　　fd2只写


fd.recv()
功能　：从管道读取信息　    
返回值：读取到的内容
＊　如果管道为空则阻塞


fd.send(data)
功能：　向管道写入内容
参数：　要写入的内容
＊　可以发送python数据类型　


消息队列　

队列：　先进先出　取出和存入顺序保持一样　
通信原理：　在内存中建立队列数据结构模型，多个进程都可以
　　　　　　　　通过队列存入内容　但是取出内容顺序和存入顺序
　　　　　　　　保持一致　


q = Queue(maxsize = 0)
功能：创建消息队列
　参数：表示最多存放多少信息．默认表示根据内存分配存储
返回值：　队列对象　


p.put(data,[block,timeout])
功能：　向队列存储消息
参数：data 要存的内容
　　　　　　block 默认队列满时会阻塞，设置为False 则非阻塞
　　　　　　timeout 超时时间　

data = q.get([block,timeout])
功能：获取队列消息


q.full() 判断队列是否为满
q.empty()　判断队列是否为空
q.qsize() 判断队列中消息数量　
q.close() 关闭队列


共享内存　
效率比较高　但不能存储多条消息

通信原理　：　在内存中开辟一块空间，对多个进程可见　
　　　　　　　　　　　进程可以写入输入，但是每次写入的内容会覆盖之前的内容

obj = Value(ctype,obj) 只能存放单个数值
功能：　开辟共享内存空间
参数：　ctype 要存储的数据类型　
　　　　　　obj   共享内存的初始化数据　
返回：　　共享内存对象　fi

obj.value 即为共享内存值，对其修改即修改共享内存

obj = Array(ctype,obj)
功能：　开辟共享内存空间
参数：　ctype 要存储的数据格式　
　　　　　　obj 初始化存入的内容，比如列表，字符串　
　　　　　　　　　　如果是整数则表示开辟空间的个数

返回值：　返回共享内存对象　　
　　　　　　＊　可以通过遍历过户每个元素的值
　　　　　　　e.g 　［１，２，３］　－－－－＞　obj[1] == 2
      *  如果存入的是字符串　
      　　　obj.value 表字符串的首地址　

'b'     signed char      int     1    
'B'     unsigned char   int     1    
'u'     Py_UNICODE  Unicode character   2   (1)
'h'     signed short     int     2    
'H'     unsigned short  int     2    
'i'     signed int  int     2    
'I'     unsigned int    int     2    
'l'     signed long     int     4    
'L'     unsigned long   int     4    
'q'     signed long long    int     8   (2)
'Q'     unsigned long long  int     8   (2)
'f'     float   float   4    
'd'     double  float   8    


http1.1 持久链接
　　　　　　　　　　　　管道　　　　　　　　　　　　　　　消息队列　　　　　　　　　　　　共享内存　

开辟空间　　　　　内存　　　　　　　　　　　　　　　　内存　                内存

读写方式　　　　　两端读写　　　　　　　　　　　　先进先出　　　　　　　　　　　　　覆盖之前内容
　　　　　　　　　　　　双向／单向　　　　　　　　　　　

效率　　　　　　　　一般　　　　　　　　　　　　　　　　　一般　　　　　　　　　　　　　　　　较高　

应用　　　　　　　　多用于父子进程　　　　　　　　　广泛灵活　　　　　　　　　　　　需要注意互斥进行互斥操作　
　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　第三方队列　　　　　　　　　　　
kill -l
信号通信
一个进程向另一个进程发送一个信号来传递某种讯息，接受者根据接收到的信号进行相应的行为　

kill -l 查看系统信号
kill -sig PID 向一个进程发送一个信号　

kill -9 20715 

p.pid 当前进程号 

SIGHUP   连接断开　
SIGINT   CTRU-C
SIGQUIT   CTRU-\
SIGSTP    CTRL-Z
SIGKILL  终止一个进程
SIGSTOP   暂停一个进程
SIGALRM   时钟信号　
SIGCHLD 　　子进程状态改变时给父进程发出

python 发送信号　

signal.signal 处理信号 pid 

os.kill(pid,sig)
功能；　发送信号　
参数：　pid 目标进程　
　　　　　　sig 要发送的信号　

import os 
os.kill(p.pid )


作业　
１回顾进程间通信方法　
２复习类的使用　
３ 
fork multiprocessing

对进城使用和原理进行总结　


from multiprocessing import pool, Process,Queue,Pipe,Value

p = Process(target =  , args=())

q=Queue
q.put()
q.get()


fd1,fd2=Pipe()

fd.send()
fd.recv()


pool=Pool(n)

r=pool.apply_async(fun,args())
or 
r=pool.map(fun,iter)

pool.close()
pool.join()


