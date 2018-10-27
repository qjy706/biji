import signal 

signal.alarm(sec)
功能：向自身发送时钟信号　－－＞　SIGALRM
参数：sec 时钟事件　多少秒后自身会收到信号　
signal.alarm(sec)

进程中只能有一个进程

同步执行　：按照顺序逐句执行，一步完成再做下一步　
异步执行　：在执行过程中利用内核记录延迟发生或者准备处理的事件．
　　　　　　　　　　这样不影响应用层的持续执行，当事件发生时再
　　　　　　　　　　由内核告知应用层处理


信号是唯一的异步通信方法

SIGHUP   连接断开　
SIGINT   CTRU-C
SIGQUIT   CTRU-\
SIGSTP    CTRL-Z
SIGKILL  终止一个进程
SIGSTOP   暂停一个进程
SIGALRM   时钟信号　
SIGCHLD 　　子进程状态改变时给父进程发出
SIGCHLD SIG_IGN
signal.pause()
功能：阻塞等待接收一个信号　

os.kill(pid,sig)

signal.signal(signum,handler)

signal.signal(signum,handler)
功能：处理信号
参数：signum 要处理的信号　
　　　　　handler 信号的处理方法　
　　　　　　　　STG_DFL 　表示使用默认的方法处理 
#始终默认方法就是终止
        SIG_IGN  表示忽略这个信号　就像没发生一样　
        func 传入一个函数表示用制定函数处理　
    　　　 func() 函数返回值
              def func(sig,frame)
                 sig: 捕获到的信号　
                 frame : 信号对象　

os.kill(pid,信号对象　) 发送信号


 信号量也是一把锁，可以指定信号量为5，
 对比互斥锁同一时间只能有一个任务抢到锁去执行，
 信号量同一时间可以有5个任务拿到锁去执行，
 如果说互斥锁是合租房屋的人去抢一个厕所，
 那么信号量就相当于一群路人争抢公共厕所，
 公共厕所有多个坑位，
 这意味着同一时间可以有多个人上公共厕所，
 但公共厕所容纳的人数是一定的，
 这便是信号量的大小               


信号量（信号灯）

原理：　给定一个数量，对多个进程可见　，且多个进程都可以操作．
　　　　　进程通过对数量多少的判断　执行各自的行为．
#

multiprocessing --> Semaphore()

sem = Semaphore(num)
功能：　创建信号量
参数：　信号量初始值　
返回：　信号量对象　

sem.get_value() 获取信号量　
sem.acquire() 将信号量减１　当信号量为0会阻塞　
sem.release() 将信号量加１　


sem=Semaphore(7)
sem.acquire()
sem.release()



from multiprocessing import Process,Semaphore,Queue,Pipe,Value,Lock
进程同步互斥　

同步是复杂的互斥　互斥是特殊的同步.　


同步是在互斥的基础有序的进行　　
互斥　：互斥是一种制约关系，


临界资源　：　多个进程或者线程都能够操作的共享资源　

临界区　 :  操作临界资源的代码段

Queue 
q=Queue()
q.put()
q.get()

Pipe 
fd1,fd2=Pipe()
send 
recv

Value
a = Value('i',2000)
a.value += 
a.value _=
同步：　消息队列Queue 管道　Pipe 就是一种同步行为　
　　　　同步是一种合作关系　，为完成某个任务，
　　　多进程或者多线程之间形成一种协调，按照约定或条件执行操作临界资源


互斥　：互斥是一种制约关系，当一个进程或者线程使用临界资源时进行上锁处理，当另一个
　　　　　　　　进程使用时会阻塞等待，直到解锁后才能继续使用　

就绪态　等待态　运行太　新建太　结束态

Event 事件　

multiprocessing  -->  Event

#创建事件对象
e = Event() 

#设置事件阻塞 
e.wait([timeout])　　超时时间
套接字的超时　
settimeout()

事件设置　当事件被设置后　e.wait()不再阻塞 e.set()设置完成　wait就不再等待
e.set() 

清除设置　　当事件设置被clear后，e.wait又会阻塞
e.clear()

事件状态判断　
e.is_set()


Lock 锁
lock = Lock()

lock.acquire()
lock.release()

s=Semaphore(5)
s.acquire()
s.release()送

首先还是创建锁的对象　这是一个类　调用方法　acquire release 
事件也是一个锁　

创建对象　
lock = Lock()
锁是一个约定　必须在其他进程都加锁　才会有这个约定

锁是一个约定　必须在其他进程都加锁才有用
lock.acquire()上锁　如果锁已经是上锁状态调用此函数会阻塞

lock.release()解锁　


with lock:   上锁
    ....
    ....

              解锁　



线程　

什么是线程　

线程也是一种多任务编程，可以利用计算机多核资源完成程序的并发执行　

线程又被称为轻量级的进程．

线程特征：
＊线程是计算机多核分配的最小单位　　进程是资源的最小单位  进程是程序运行的一种状态
＊一个进程可以包含多个线程　　线程资源是共享的　是全局变　进程是独立的
＊线程也是一个运行的过程，消耗计算机的资源，多个线程共享进程的资源和空间
＊线程的创建删除消耗的资源都要远远小于进程
＊多个线程之间执行互不干扰　
＊线程也有自己的也有属性，比如指令集　ID 

threading 模块创建线程

threading.Thread()
threading.Thread()
功能：创建线程对象　
参数：name  线程名称　　　默认　Thread-1 
     target 线程函数　
     args 元祖给线程函数传参　
     kwargs 给线程函数键值对传参

threading.Thread(name,target,args,kwargs)

t.start()  启动线程，自动运行线程函数　

t.join([timeout]) 回收线程




多个线程同属于一个进程　进程号一样的

p.pid 
os.getpid()
os.getppid()
os.path.exists()
os.listdir(path)
os.path.getsize()
getpasswd
线程对象属性

t.is_alive() 查看线程状态　

t.name  线程名称

t.setName() 设置线程名称　

t.getName()

threading.currentThread() 获取当前线程对象






t.daemon 属性　
默认情况主线程退出不回影响分支线程执行　
如果设置为True 则分支线程随主线程退出　

设置方法：　
t.daemon = True
t.setDaemon(True)　


判断属性值　
t.isDaemon() 

*要在start前设置，不会join同用




创建自己的线程类　
步骤：
１，继承Thread 
2,加载Thread中的__init__
3,重写run方法



线程通信　

通信方法　　多个线程共享进程的空间，所以线程间通信
　　　　　　　　　使用全局变量完成

注意事项：　线程间使用全局变量往往要同步互斥机制，
　　　　　　　　　保证通信安全　

线程同步互斥方法　

线程的event方法　
#创建事件对象
e = threading.Event()
e.wait([timeout]) 如果e为设置状态则不阻塞，否则阻塞
e.set() 讲e变为设置状态　
e.clear() 清除设置　


线程锁

lock=threading.Lock()创建锁对象
lock.acquire() 上锁
lock.release() 解锁

*也可以通过with上锁，上锁状态调用acquire会阻塞



python线程的GIL问题　(全局解释器锁)


python --> 支持多线程　--> 同步互斥　--> 加锁　--> 
-->  超级锁　给解释器加锁--> 解释器同一时刻只能解释同一线程（效率变低）
-->  


后果：　一个解释器同一时刻只能解释执行一个线程，
　　　　　所以导致python线程效率低下，但是当遇到IO阻塞时
　　　　线程会主动让出解释器，因此python线程更加适合高延迟的io程序开发


解决方法
＊尽量用进程完成并发
＊不适用c解释器　
＊尽量使用多种方案组合的方式进行并发操作，线程用做高延迟IO


jisuanmijixing
test2 


单线程　　９
io密集型　　　４．５　

多线程　并不会比单线程块

