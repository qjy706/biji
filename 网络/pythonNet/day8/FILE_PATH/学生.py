# L = []  # 创建一个新的列表，用此列表准备保存学生信息
# # 录入学生信息
# while True:
#     n = input("请输入姓名: ")
#     if not n:
#         break
#     a = int(input("请输入年龄: "))
#     s = int(input('请输入成绩: '))
#     # 创建一个新的字典，把学生的信息存入字典中
#     d = {}  # 每一次都重新创建一个新的字典
#     d['name'] = n
#     d['age'] = a
#     d['score'] = s
#     L.append(d)

# print(L)  # 打印结果


# print("+---------------+----------+----------+")
# print("|     name      |   age    |   score  |")
# print("+---------------+----------+----------+")
# for d in L:
#     n = d['name']
#     a = d['age']
#     s = d['score']
#     print('|%s|%s|%s|' % (n.center(15),
#                           str(a).center(10),
#                           str(s).center(10)
#                           )
#           )

# # print("|    tarena     |    20    |     99   |")
# # print("|     name2     |    30    |     88   |")
# print("+---------------+----------+----------+")


def input_student():
    L = []  # 创建一个新的列表，用此列表准备保存学生信息
    # 录入学生信息
    while True:
        n = input("请输入姓名: ")
        if not n:
            break
        a = int(input("请输入年龄: "))
        s = int(input('请输入成绩: '))
        # 创建一个新的字典，把学生的信息存入字典中
        d = {}  # 每一次都重新创建一个新的字典
        d['name'] = n
        d['age'] = a
        d['score'] = s
        L.append(d)
    return L

    
def output_student(L):
    print("+---------------+----------+----------+")
    print("|     name      |   age    |   score  |")
    print("+---------------+----------+----------+")
    for d in L:
        n = d['name']
        a = d['age']
        s = d['score']
        print('|%s|%s|%s|' % (n.center(15),
                              str(a).center(10),
                              str(s).center(10)
                              )
              )

    # print("|    tarena     |    20    |     99   |")
    # print("|     name2     |    30    |     88   |")
    print("+---------------+----------+----------+")


L = input_student()
print(L)
output_student(L)  # 打印表格


def xiugai():
    word=input('请输入学生姓名')
    for x in l:
        if word == x['name']:
            x['name']=[word]
            a=input('请输入修改的学生的年龄')
            b=input('请输入修改的学生的成绩')
            x['age']=[a]
            x['score']=[b]
    return l
xiugai(l)


def shanchu():
    word=input('请输入学生姓名')
    for x in l:
        if word == x['name']:







def main():
    l=[]
    while Ture:

        print(    '+-------------------------+')
        print(    '|' '1'  '添加学生信息'       '|')
        print(    '|' '2'  '显示学生信息'       '|')
        print(    '|' '3'  '删除学生信息'       '|')
        print(    '|' '4'  '修改学生信息'       '|')
        print(    '|' 'q'  '退出'              '|')
        print(    '+-------------------------+')
        s=input('请选择')
        if s == 'q':
            break
        elif s == '1':
            l += input_student()
        elif s == '2':
            l += output_student(L)
        elif s == '4':
            xiugai(l)
        elif s == '3':
            shanchu(l)


main()
