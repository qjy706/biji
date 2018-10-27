# import os 
# from time import sleep

# pid = os.fork()

# if pid < 0:

#     print('create process')

# elif pid == 0:
#     sleep(3)
#     print('child process exit',os.getpid())
#     os._exit(2)

# else:
#     pid,status = os.wait()
#     print(pid,status)
#     #获取子进程退出状态 ps._exit(2)
#     print(os.WEXITSTATUS(status))
#     while True:
#         pass


# setsockopt



import os 
from time import sleep

pid = os.fork()

if pid < 0:

    print('create process')

elif pid == 0:
    sleep(3)
    print('child process exit',os.getpid())
    os._exit(2)

else:
    while True:
        sleep(1)
        #通过非阻塞形式捕获子进程退出
        pid,status = os.waitpid(-1,os.WNOHANG)
        print(pid,status)
        #获取子进程退出状态 ps._exit(2)
        print(os.WEXITSTATUS(status))
        if pid != 0:
            break
        #设置为非阻塞状态，没有捕获到退出运行下面程序
        #捕获到退出会打印
    while True:
        pass
#几乎是单进程了


pid = os.fork()

if pid < 0:
    print('create process')

elif pid == 0:
    pid1 = os.fork()
    if pid1 < 0:
        print('create process')
    elif pid1 == 0 :
        pass
    else:
        sys.exit('父进程退出')
