# # 1-20的阶乘的和
# def myfac(n):
#     if n == 1:
#         return 1
# #如果n不是１，则递推到下一级求解
#     return n * myfac(n-1)
# print(myfac(20))


# 2. 已知有列表　
# L=[[3,5,8],10,[[13,14],15,18],20]
#1) 写一个函数　print_list(lst) 打印出所有的数字　
# 　　　　print_list(L)           # 3,5,8,10,13

#2) 写一个函数　sum_list(lst)  返回列表中所有数字的和
# print(sum_list(L))
#注　type(x) 函数可以返一个对象的类型
#       type(20) is int # True 
#       type([3,5,8]) is list # True 
#       type(20) is list  False



# def print_list(lst):
#     for x in lst:
#         if type(x) is list:  # 如果x是列表，则再次再印
#             print_list(x)
#         else:
#             print(x)
# L=[[3,5,8],10,[[13,14],15,18],20]
# print_list(L)

# def sum_list(lst):
#     s=0
#     for x in lst:
#         if type(x) is list:
#             s += sum_list(x)
#         else:
#             s += x
#     return s
# L=[[3,5,8],10,[[13,14],15,18],20]
# print(sum_list(L))



# 2. 已知有列表　
# L=[[3,5,8],10,[[13,14],15,18],20]
#1) 写一个函数　print_list(lst) 打印出所有的数字　
# 　　　　print_list(L)           # 3,5,8,10,13

#2) 写一个函数　sum_list(lst)  返回列表中所有数字的和
# print(sum_list(L))
#注　type(x) 函数可以返一个对象的类型
#       type(20) is int # True 
#       type([3,5,8]) is list # True 
#       type(20) is list  False

def print_list(lst):
    l=[]
    for x in lst:
        if type(x) is list:
            for i in x:
                if type(i) in list:
                    for b in i:
                        l.append(b)
L=[[3,5,8],10,[[13,14],15,18],20]
print_list(L)
