
#装饰
# def fn(n):
#     def fx():
#         print('wudi')
#         n()
#     return fx

# def dazhongxiang(n):
#     def fy():
#         print('789')
#         n()
#     return fy

# @dazhongxiang
# @fn
# def myfun():
#     print('asda')
# myfun()



def f1(a, *args, b, **kwargs):
     return a + b
print(f1.__name__ )