# 一个球从１００米高空落下，每次落地后反弹高度是原高度的一半，再落下写程序算出皮球在第十次落地后反弹高度
# 是多高





# one=(1/2)*n
# two=(1/2)/one
# three=(1/2)/two
# four=(1/2)/three



# def high(h):
#     L=[h]
#     s=0
#     while s <= 10:
#         s+=1
#         h=0.5*h
#         L.append(h*2)
#     return h,sum(L)
# print(high(100))


# 分解质因数：输入一个正整数，分解质因数，
# 如输入　
# ９０　
# 则打印　
# '90＝2*3*3*5'
# （质因数是指小数最小能被原数整除的素书　不包括１

# def L(n):
#     x=[]
#     b=2
#     if n == b:
#         return n
#     else:
#         while n >= b:
#             a=n%b
#             if a == 0:
#                 x.append(b)
#                 n=n/b
#             else:
#                 b+=1
#         print(x)
# n=int(input('请输入一个数字'))
# s=L(n)
# d='*'.join(s)
# print(d,'=',n)


修改原学生信息管理程序，加入异常处理语句，让程序在任何情况下都能按逻辑正常执行
如：
输入成绩和年龄时，如果用户输入非法空字符串也不会导致程序崩溃








