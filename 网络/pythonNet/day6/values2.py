from multiprocessing import Process,Array
import os 
import time 

# shm = Array('i',[1,2,3,4,5])
# print(shm) 
#
#创建共享内存，开辟五个整形空间
# shm = Array('i',5)

#存入字符串，要求bytes格式　
shm = Array('c',b'hello')

def fun():
    for i in shm:
        print(i)
    shm[0]=b'h'

p = Process(target = fun)
p.start()
p.join()

for i in shm:
    print(i)
print(shm.value)#只有字符串才能这么打印
print(os.getpid())
while True:
    time.sleep(2)
    print('b')


