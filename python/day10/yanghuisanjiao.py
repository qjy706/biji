# 3. 写程序打印杨辉三角 (只打印6层)
#         1
#        1 1
#       1 2 1
#      1 3 3 1
#     1 4 6 4 1
#   1 5 10 10 5 1
# l[0]+l[1]
# l[1]+l[2]



# def get_yh(n):
#     L=[]
#     line=[1]
#     for i in range(n):
#         L.append(line)
#         line=get_next_line(line)
#     return L

# def get_next_line(line):
#     L=[1]
#     for i in range(len(line)-1):
#         L.append(line[i]+line[i+1])
#     L.append(1)
#     return L

# L=get_yh(6)
# print(L)


#阶乘

# def jiecheng(n):
#     if n == 1:
#         return 1
#     return n*jiecheng(n-1)

# s=jiecheng(8)
# print(s)


# 一个球从１００米高空落下，每次落地后反弹高度是原高度的一半，再落下写程序算出皮球在第十次落地后反弹高度
# 是多高


# def high(n):
#     L=[]
#     h=50
#     s=0
#     while s <= n:
#         L.append(50)
#         h=0.5*h
#         s+=1
#     return h
# s=high(10)
# print(s)





# 2. 写一个实现迭代器协议的类,让此类可以生成从b 开始的n个素数
#   class Prime:
#       def __init__(self, b, n):
#           ...
#       def __iter__(self):
#          ....

#   L = [x for x in Prime(10, 4)]
#   print(L)  # L = [11, 13, 17, 19]


class Prime(object):
    def __init__(self,b,n,L=[],s=0):
        self.b=b
        self.n=n
        self.count=0

    def __iter__(self):
        print('被调用')
        return self

    def isprimy(self,x):
        if x < 2:
            return False
        for i in range(2, x):
            if x % i == 0:
                return False
        return True


    def __next__(self):
        print('被调用')
        if self.count > self.n:
            raise StopIteration
        while True:
            if self.isprimy(self.b):
                r=self.b
                self.b += 1
                self.count += 1
                return r
            self.b += 1

L = []
it = Prime(10,4).__iter__()
while True:
    try:
        x = next(it)
        L.append(x)
    except StopIteration:
        break
print(L)

L = [x for x in Prime(10, 4)]
print(L)  # L = [11, 13, 17, 19]



def __iter__(self):
    return self

def __next__(self):
    if self.count >= lem(self.data):
        raise StopIteration

    r = self.data[self.count]
    self.count += 1
    return r