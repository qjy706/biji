import signal
from time import sleep


signal.alarm(5)
#使用默认方法处理信号
# signal.signal(signal.SIGALRM,signal.SIG_DFL)


signal.signal(signal.SIGALRM,signal.SIG_IGN)
signal.signal(signal.SIGINT,signal.SIG_IGN)



while True:
    sleep(2)
    print('摁ctrl c啊')
    print('等待时钟....')


