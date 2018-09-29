from threading import Thread
from time import sleep
#线程函数　

def fun(sec):
    print('线程属性测试')
    sleep(sec)
    #获取当前线程对象的getName()属性获取名称
    print('%s 线程结束' % currentThread().getName())


#创建线程

thread = []
for i in range(3):
    t = Thread(target = fun,args=(2,))
    thread.append(t)
    t.start()




#设置线程名称
thread[1].setName('Tarena')

#回收线程
for i in thread:
    i.join()
