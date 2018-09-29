# os.fork() 

# from multiprocessing import Pool

# def w():
#     return 'v'

# pool=Pool(5)

# r=pool.apply_async(func = w)

# pool.close()

# pool.join()


# print(r.get())


from multiprocessing import Pool
from time import sleep


def f(x):
    for i in range(10):
        print ('%s --- %s ' % (i, x))
        sleep(1)
#f变成了四个f　分别运行程序　

def main():
    pool = Pool(processes=3)    # set the processes max number 3
    for i in range(11,20):
        result = pool.apply_async(f, (i,))
    pool.close()
    pool.join()
    if result.successful():
        print ('successful')
main()

# def f(x):
#     for i in range(5):
#         print("{} ---- {}".format(i,x))
#         sleep(1)
# #f可以分成四个进程同时进行　　下面的代码也就四个一次性运行
# pool=Pool(4)
# for x in range(5):
#     r=pool.apply_async(f,(x,))#这是一个进程　
# 这是一个循环的进程



# pool.close()
# pool.join()

from multiprocessing import Process,Pipe
from time import sleep
#Pipe默认双向
fd1,fd2 = Pipe()

def fun(name):
    sleep(3)
    fd2.send('hello'+str(name))

jobs=[]
for i in range(5):
    p = Process(target = fun ,args=(i,))
    jobs.append(i)
    p.start()

for i in range(5):
    data=fd1.recv()
    print(data)





