#! /usr/bin/env python3 

import os 
from time import sleep 

a=1

pid=os.fork()

if pid < 0:
    print('创建失败')

elif pid == 0:
    b=1
    s=0
    while b < 10:
        s += a
        b += 1

    print('s=',s)

else:
    sleep(1)
    print('父进程结束')

