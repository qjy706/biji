from jisuanmijixing import *

import time

t = time.time()

#单进程

# for i in range(10):
#     count(1,1)

# print('Line cpu',time.time() -t)

# io密集型




#多线程　
import threading 


# counts=[]
# for x in range(10):
#     th=threading.Thread(target = count,args=(1,1))
#     counts.append(th)
#     th.start()

# for i in counts:
#     i.join()

# print('thread cpu',time.time()-t)


#线程的io操作
def io():
    write()
    read()

counts=[]
for x in range(10):
    th=threading.Thread(target = io)
    counts.append(th)
    th.start()

for i in counts:
    i.join()

print('thread cpu',time.time()-t)