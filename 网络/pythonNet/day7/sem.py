from multiprocessing import Semaphore,Process,Pool
from time import sleep
import os 

#创建信号量
#信号量限制多少进程使用
sem = Semaphore(3)

#pool=Pool(n)
# r=pool.apply_async(fun,(i,))
# r=pool.map(fun,iter)
#把程序放入进程池中　，进程池数量根据ｎ确定　
# pool.close()
#pool.join()

def fun():
    print('进程%d等待信号量'%os.getpid())
#消耗一个信号量　

#信号变成0　剩下的一个进程会阻塞　等待信号添加　进行下一步
    sem.acquire()
    print('进程%d消耗信号量'%os.getpid())
    sleep(3)
    sem.release()
    print('进程%d添加信号量'%os.getpid())


jobs=[]
for i in range(10):
    p = Process(target = fun)
    jobs.append(p)
    p.start()

for i in jobs:
    i.join()

print(sem.get_value())