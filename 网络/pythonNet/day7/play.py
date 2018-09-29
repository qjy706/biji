from multiprocessing import Pool
from time import sleep,ctime




pool = Pool(4)

def w(x):
    for i in range(5):
        print('%d-----%d'%(i,x))


for i in range(4):
    pool.apply_async(func=w,args=(i,))

pool.close()

pool.join()