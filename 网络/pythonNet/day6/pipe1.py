from multiprocessing import Pipe,Process
import os,time

fd1,fd2 = Pipe()

def fun(name):
    time.sleep(3)
    #向管道写入内容
    fd2.send('hello'+str(name))

jobs =[]
for i in range(5):
    p = Process(target = fun,args = (i,))
    jobs.append(p)
    p.start()

for i in range(5):
    data = fd1.recv()
    print(data)


for a in jobs:
    a.join()


