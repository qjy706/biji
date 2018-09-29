from signal import *
import time

def handler(sig,frame):
    if sig == SIGALRM:
        print('接收到时钟信号')
    elif sig == SIGINT:
        print('就不结束')


alarm(5)
#时钟信号调用函数　捕获到时钟信号时候会传给函数　handler
#同理　捕获到不同的信号可以传给不同的函数　可以写不同的
#处理信号方法　

signal(SIGALRM,handler)
signal(SIGINT,handler)



while True:
    print('waiting for a signal')
    time.sleep(2)