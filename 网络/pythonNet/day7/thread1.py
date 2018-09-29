import threading
from time import sleep 
import os 

a=1

def music():
    global a
    a=10000
    for i in range(5):
        sleep(2)
        print('播放葫芦娃',os.getpid())


    
#创建线程对象　 编程线程函数
t = threading.Thread(target = music)

t.start()

for i in range(5):
    sleep(1.5)
    print('想听灌篮高手',os.getpid())


t.join()

print('mian Thread a=',a)
#线程在进程空间内部，线程修改变量　进程的也会被修改