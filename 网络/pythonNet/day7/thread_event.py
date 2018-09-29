import threading 
from time import sleep

s = None
e=threading.Event()


def bar():
    print('拜山头')
    global s
    s = '天王盖地虎'

def foo():
    print('说出口令就是自己人')
    sleep(2)
    if s == '天王盖地虎':
        print('我是座山雕,自己人')
    else:
        print('打死他')
    e.set()#等foo 验证完毕其他的再执行

def fun():
    print('呵呵..')
    sleep(1)
    global s 
    s = '小鸡炖蘑菇'



b = threading.Thread(target = bar)
f = threading.Thread(target = foo)
b.start()
f.start()
e.wait()#运行b f 之后其他内容不许执行　验证完再执行
fun()
f.join()
b.join()

