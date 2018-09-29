from multiprocessing import Event

#创建事件对象　
e=Event()

#事件状态判断
print(e.is_set())

#设置事件阻塞 
e.wait(3)

e.clear()
e.wait()
