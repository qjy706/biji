# 模拟斗地主发牌，牌共54张，黑桃('\u2660'),梅花('\u2663')
# 方块('\u2665'),红桃('\u2666')
# A2-10JQK
# 大王　小王　
# 三个人　每个人发17张　底牌留三张　
# 要求　
# 输入回车　打印第一个人的17张牌
# 输入回车　打印第二个人的17张牌
# 输入回车　打印第三个人的17张牌
# 输入回车　打印第四个人的17张牌
# 输入回车　打印三张底牌
# L=['大王','小王']
# for x in ('\u2660','\u2663','\u2665','\u2666'):
#     for i in ('A','2','3','4','5','6','7','8','9','10','J','Q','K'):
#         y=x+' '+i
#         L.append(y)
# import random as R
# R.shuffle(L)
# a=R.sample(L,2)
# print('底牌',a)
# b=L-a
# print('第一个人',R.sample(b,17))
# print('第二个人',R.sample(b,17))
# print('第三个人',R.sample(b,17))


#练习
#写一个函数　get_score(),来获取学生输入的成绩，（０～１００）的整数
# 如果输入异常，则让次函数返回0　否则返回用户输入的成绩　

# def get_score():
#     s=int(input('请输入成绩'))
#     if 0 <= s <= 100:
#         return s
#     else:
#         print('失败')


# # # 方法１　在调用的地方加入异常处理语句，然后进行处理
# try:
#     score=get_score()
# except ValueError:
#     score=0   #输入不合法之后的修改
# print('学生成绩是',score)


# # 方法２　在函数内部
# def get_score():
#     try:
#         s=int(input('请输入成绩'))
#     except ValueError:
#         return 0
#     if 0 <= s <= 100:
#         return s
#     else:
#         return 0
# score=get_score()
# print('学生成绩是',score)


# try:
#     n=int(input('请输入证书'))
# except int:  #错误　，Int类型不能当成错误类型　用于try except 
#     pass

# def fry_egg():
#     print('qq')
#     try:
#         count=int(input('鸡蛋个数'))
#         print('完成',count)
#     finally:
#         print('天然气')

# try:
#     fry_egg()
# except:
#     print('程序出现异常，已转为正常状态')
# print('程序推出')


# x=100
# y=200
# try:
#     newx=x
#     newy=y
#     try:
#         x=int(input('输入一个数字'))
#         y=int(input('输入一个数字'))
#     except:
#         x=newx
#         y=newy     #只要有一个错的　要转一起转
# except:
#     pass
# print(x,y)

# 嵌套
# try:
#     try:
#         n=int(input('整数'))
#     except ValueError:
#         print('在内层try语句内出现值错误，已转为正常状态')
#     else:
#         print('内层try语句没有出现异常')
# except:
#     print('外层try语句内出现值错误，已转为正常状态')
# else:
#     print('外层try语句没有出现异常')


# raise 语句
# def make_except():
#     print('开始')
#     raise ValueError  # 故意发送一个错误报告
#     e=ValueError
#     raise e


#     print('结束')

# try:
#     make_except()
# except ValueError:
#     print('66')
# print('程序结束')


#练习　
# 写一个函数　get_age()用来获取一个人的年龄信息
# 次函数规定用户只能输入１－１４０之间的整数，如果用户输入其他的数则直接触发
#ValueError类型的错误来通知调用这　


# def get_age():
#     try:
#         n=int(input('请输入年龄'))
#         if 0 <= n <= 140:
#             return n
#         else:
#             raise ValueError
#     except ValueError:
#         return '输入的不是0-140的整数！'

# print('年龄是：',get_age())



#assert　语句（断言语句）

# def get_score():
#     s=int(input('请输入学生成绩(0~100)'))
#     assert 0 <= s <= 100,'成绩超出范围'
#     # 等同于　
#     # if (0 <= s <= 100) == False:
#     #     raise AssertionError
#     return s
# try:
#     score=get_score()
#     print('学生成绩为:',score)
# except ValueError:
#     print('用户输得数字不能转为整数')
# except AssertionError:
#     print('用户输入的证书不在范围内')




#为什么要用到异常处理机制？？？

 