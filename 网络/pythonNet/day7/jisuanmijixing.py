#计算密集型

def count(x,y):
    c = 0
    while c < 6000000:
        c += 1
        y += 1
        x += 1

#io密集函数
def write():
    f = open('test.txt','w')
    for i in range(1000000):
        f.write('hello\n')
    f.close()

def read():
    f = open('test.txt')
    lines = f.readlines()
    f.close()