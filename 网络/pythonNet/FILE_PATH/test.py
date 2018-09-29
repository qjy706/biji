# def mypow(x, y):
#     return x ** y


# s=0
# for i in map(pow,range(1,10),range(9,0,-1)):
#     s+=i

# print(s)
# def fn(n):
#     return n 

# L=list(filter(fn,range(1,100)))
# print(L)

#filter返回的是一个可迭代对象 用Ｌ绑定
# def isodd(x):
#     return x % 2 == 1

# for x in filter(isodd, range(10)):
#     print(x)   # 1 3 5 7 9

# L = list(filter(isodd, range(10)))   # L = [1, 3, 5, 7, 9]
# print("L =", L)


# def sushu(n):
#     if n < 2:
#         return False
#     for i in range(2,n):
#         if n % i == 0:
#             return False
#     return True

# L=list(filter(sushu,range(100)))
# print(L)

L=[-1,-5,-10,231,89,44.11]：
s=sorted(L,key=abs)
print(s)