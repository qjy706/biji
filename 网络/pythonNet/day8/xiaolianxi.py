# import time 
# import threading

# s1=threading.Semaphore(5)

# def foo():
#     s1.acquire()#是信号类里面的方法
#     time.sleep(2)
#     print('ok',time.ctime())
#     s1.release()

# for i in range(20):
#     t1=threading.Thread(target = foo)
#     t1.start()

# class Num(object):
#     def __init__(self):
#         self.num = 0
#         self.lock = threading.Lock()

#     def add(self):
#         self.lock.acquire()
#         self.num+=1
#         num=self.num
#         self.lock.release()
#         return num

# n=Num()

# class jdThread(threading.Thread):
#     def __init__(self,item):
#         super(self.__class__,self).__init__()
#         self.item = item

#     def run(self):
#         time.sleep(2)
#         value=n.add()
#         print(self.item,value)

# for item in range(5):
#     t = jdThread(item)
#     t.start()
#     t.join()



# class Num:
#     def __init__(self):
#         self.num = 0
#         self.sem = threading.Semaphore(value = 3)
#         #允许最多三个线程同时访问资源
 
#     def add(self):
#         self.sem.acquire()#内部计数器减1
#         self.num += 1
#         num = self.num
#         self.sem.release()#内部计数器加1
#         return num
     
# n = Num()
# class jdThread(threading.Thread):
#     def __init__(self,item):
#         threading.Thread.__init__(self)
#         self.item = item
#     def run(self):
#         time.sleep(2)
#         value = n.add()
#         print(self.item,value)
 
# for item in range(100):
#     t = jdThread(item)
#     t.start()
#     t.join()

from multiprocessing import Process,Semaphore
import time,random

def go_wc(sem,user):
    sem.acquire()#计数器减掉1　直到０位置说明有三个进程进入房间运行
    print('%s 占到一个茅坑' %user)
    time.sleep(2) #模拟每个人拉屎速度不一样，0代表有的人蹲下就起来了
    sem.release()#计数器加1 直到变成３三个程序出来了　把信号换回去　换下三个






if __name__ == '__main__':
    sem=Semaphore(3)
    p_1=[]
    for i in range(10):
        p=Process(target=go_wc,args=(sem,i))
        p.start()
        p_1.append(i)

    for i in p_1:
        p.join()
