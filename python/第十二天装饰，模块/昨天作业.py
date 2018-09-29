# 1-20的阶乘的和
# # def myfac(n):
# #     if n == 1:
# #         return 1
# # #如果n不是１，则递推到下一级求解
# #     return n * myfac(n-1)
# # print(myfac(20))

# def myfac(n):
#     s=1 
#     for i in range(1,n+1):
#         s *= i
#     return s 


# def sum_factorial(n):
#     s=0

#     for i in range(1,n+1):
#         s += myfac(i)
#     return s
# print(sum_factorial(20))

# def sum_factorial(n):
#     return sum(map(myfac,range(1,n+1)))


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



# elif s == '5':
#     print_info_by_score_desc(L)
# elif s == '6':
#     print_info_by_score_asc(L)
# elif s == '7':
#     print_info_by_age_desc(L)
# elif s == '8':
#     print_info_by_age_desc(L)


# def print_info_by_score_desc(L):
#     def get_score(d):
#         return d['score']
#     L2 = sorted(L,key=get_score,reverse=True)# 按照成绩倒序
#     output_student(L2)

# def print_info_by_score_asc(L):

#     L2 = sorted(L,key=lambda d:d['score'])
#     output_student(L2)

# def print_info_by_age_desc(L):
#     L2 = sorted(L,key=lambda d:d['age'],reverse=True)
#     output_student(L2)

# def print_info_by_age_desc(L):
#     L2 = sorted(L,key=lambda d:d['age'])
#     output_student(L2)



