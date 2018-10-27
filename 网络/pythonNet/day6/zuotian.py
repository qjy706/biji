import os
from multiprocessing import Process

filename = './byte.png'

size = os.path.getsize('filename')
os.path.getsize(路径)

def copy1():
    f = open(filename,'rb')

    n = size // 2

    fw = open('file1.png','wb')

    while True:
        if n < 1024:
            data = f.read(n)
            fw.write(data)
            break
        data = f.read(1024)
        fw.write(data)
        n -= 1024
    fw.close()
    f.close()

def copy2():
    f = open(filename,'rb')
    fw = open('file2.png','rb')
    f.seek(size//2,0)#从这个字节开始，向文件尾部读取
    while True:
        data = f.read(1024)
        if not data:
            break
        fw.write(data)
    fw.close()
    f.close()

p1 = Process(target = copy1)
p2 = Process(target = copy2)
p1.start()
p2.start()
p1.join()
p2.join()



    