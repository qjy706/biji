import os 
from time import sleep
print('*'*10)

a=1

pid = os.fork()
#子进程只会执行下面代码 
if pid < 0:
    print('创建进程失败')

elif pid == 0:
    print('这是新的进程')

    print('a=',a)
#子进程会把父类创建的内存空间一起拷贝 a=1 
#print 不占用内存空间 只是打印一下　
    a=10000
#a=10000只在子进程内存空间修改
l
else:
    sleep(1)
    print('这是原有进程')
    print('parent a = {}'.format(a))
#子进程和父进程各自运行　谁抢占时间片　谁运行　　　父类等待态　
#　先执行子进程


print('演示完毕')
# 这是原油进程
# 演示完毕
# 这是新的进程
# 演示完毕


#理解为两个进程　
#每个进程空间独立，各自占有一定的虚拟内存
#进程之间运行互不影响，各自独立运行　
