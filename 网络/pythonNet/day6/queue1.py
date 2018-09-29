from multiprocessing import Queue,Process
from time import sleep

# q=Queue(3)

# q.put(1) 
# print(q.empty())
# q.put(2)
# print(q.full())
# q.put(3)
# print(q.qsize())
# property(q.get())

#创建消息队列　
q = Queue()
#fd1,fd2=Pipe()默认双向  send recv
def fun1():
    sleep(1)
    data='666'
    q.put(data)

def fun2():
    sleep(10)
    print('收到消息:',q.get())

p1 = Process(target=fun1)
p2 = Process(target=fun2)
p1.start()
p2.start()
p1.join()
p2.join()

# q.put()
# q.get()

# q=Queue()

# p = Process(target = fun )
q= Queue()
q.put()
q.get()