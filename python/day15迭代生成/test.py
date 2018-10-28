# def fun():
#     s = 0
#     while s < 10:
#         s += 1
#         yield s
# for i in fun():
#     print(i)
# it=iter(fun())
# try:
#     while True:
#         s = next(it)
#         print(s)
# except:
#     pass


#yield　在函数内部　，函数变成可迭代对象　用　迭代器iter　next 或者遍历都可以


# L=[2,3,5,7,9]
# gen=(x**2 for x in L)

# it = iter(gen)
# L[0]=1
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
def input_to_list():
    L=[]
    while True:
        s=input('请输入')
        if not s :
            break
        L.append(s)
    return L

def list_to_file(lst,filename='input.txt'):
    try:
        fw=open(filename,'w')
        for s in lst:  # 绑定的字符串写入到文件中
            fw.write(s)
            fw.write('\n')  #换行符号
        fw.close()
    except OSError:
        print('写入文件失败')
L=input_to_list()
list_to_file(L)


def input_to_list():
    L=[]
    while True:
        s = input('请输入')
        if nor s:
            break
        L.append(s)
    return L

def list_to_file(lst,filename=''):
    try:
        fw=open(filename,'w')
        for s in lst:
            fw.write(s)
            fw.write('\n')
        fw.close()
    except:
        print('写入失败')
L=input_to_list()
