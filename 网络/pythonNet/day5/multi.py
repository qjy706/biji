import multiprocessing as mp 
from time import sleep 



a=1

def fun():
    sleep(3)
    global a
    a=10000

    print('a',a)
    print('子进程事件')

#创建进程对象　 进程绑定函数　
p = mp.Process(target = fun)


#启动进程　 函数变成进程时间函数
p.start()

sleep(2)
print('这是父进程')

p.join()


print('parent a',a)