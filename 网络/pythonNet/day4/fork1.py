import os 

from time import sleep

pid = os.fork()

if pid < 0:
    print('6666')

elif pid == 0:
    print('child pid ',os.getpid())
    print('father pid ',os.getppid())

else:
    print('child pid',pid)
    print('pid',os.getpid())

