from multiprocessing import Process,Event
from time import sleep

def wait_event():
    print('1想操作临界区')
    e.wait()
    print('开始操作临界区资源',e.is_set())
    with open('file') as f:
        print(f.read())

def wait_event_timeout():
    print('2也想操作临界区')
    e.wait(2)#时间阻塞
    if e.is_set():
        with open('file') as f:
            print(f.read())
    else:
        print('不能读取')

#事件对象
e = Event()
p1 = Process(target=wait_event)
p1.start()

p2 = Process(target=wait_event_timeout)
p2.start()

print('主进程操作')
with open('file','w') as f:
    sleep(3)
    f.write('i love China')
#只要运行到这一步　，子进程就不再等待　直接运行  wait(2)两秒
e.set()
print('释放临界区')

p1.join()
p2.join()

