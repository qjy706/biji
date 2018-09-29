import gevent 

def foo(a,b):
    print('a = %d,b = %d'%(a,b))
    gevent.sleep(2)#遇到阻塞自动跳转
    print('Running foo again')

def bar():#上面函数暂停２秒　跑到这里运行　　这里运行到睡眠3秒　跑到上面去了　
    print('Running int bar')
    gevent.sleep(3)
    print('Running bar again')
#生成协程

f = gevent.spawn(foo,1,2)
g = gevent.spawn(bar)

#回收协程　
gevent.joinall([f,g])