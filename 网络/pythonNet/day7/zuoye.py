from multiprocessing import Process
from signal import *
from time import sleep,ctime
import os
import sys 


def talk(sig,frame):
    if sig == SIGINT:
        SIGUSR1=SIGINT
        os.kill(os.getppid(),SIGUSR1)
    elif sig == SIGQUIT:
        os.kill(os.getppid(),SIGUSR2)
    elif sig == SIGUSR1:
        print('到站了，请下车')
        sys.exit('售票员下车了')

def shoupiaoyuan():
    while True:
        signal(SIGINT,talk)
        signal(SIGQUIT,talk)
        signal(SIGUSR1,talk)


p=Process(target = shoupiaoyuan)
p.start()
print(p.pid)

def siji(sig,frame):
    if sig == SIGUSR1:
        print('老司机开车了')
    elif sig == SIGUSR2:
        print('车速有点快，系好安全带')
    elif sig == SIGTSTP:
        os.kill(p.pid,SIGUSR1)#发送信号

while True:
    signal(SIGUSR1,siji)
    signal(SIGUSR2,siji)
    signal(SIGTSTP,siji)
    signal(SIGINT,SIG_IGN)
    signal(SIGQUIT,SIG_IGN)
#signal.signal(sin,handler)

p.join()








