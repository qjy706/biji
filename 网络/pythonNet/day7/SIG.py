import signal
import time 

signal.alarm(3)
time.sleep(2)
signal.alarm(5)
#时钟信号放进内核中执行　之后返回给应用层 异步　
#一个进程只能挂起一个时钟，第二个时钟会把第一个覆盖掉

signal.pause()#阻塞等待信号



while True:
    time.sleep(1)
    print('等待时钟信号')



