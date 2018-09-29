# from multiprocessing import Pool
# from time import sleep 


# def fun(n):
#     sleep(1)
#     print('执行pool map 事件')
#     return n*n

# pool=Pool(4)
# #使用map将时间放入进程池
# # r是返回值　函数返回值　
# r=pool.map(fun,range(10))
# pool.close()
# pool.join()

# print(r)

from multiprocessing import Pool
from time import sleep

def fun(n):
    sleep(1)
    print('执行')
    print(n*n)

pool = Pool(5)

L=[]

for i in range(10):
    r=pool.apply_async(fun,(i,))


pool.close()
pool.join()





