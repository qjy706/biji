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
# kinds=['\u2660','\u2663','\u2665','\u2666']
# numbers=['A']+[str(x) for x in range(2,11)]+list('JQK')
# pokes=['大王','小王']
# for k in kinds:
#     for n in numbers:
#         pokes.append(k+' '+n)
# L=pokes.copy()
# import random
# random.shuffle(L)
# input()#等待键盘输入
# print('第一个人的17张牌子是',L[:17])
# input()
# print('第二个人的17张牌子是',L[17:34])
# input()
# print('第二个人的17张牌子是',L[34:51])
# input()
# print('底牌',L[51:])
# #九九乘法表
# for line in range(1,10):
#     for col in range(1,line+1):
#         print('%d*%d=%2d' % (col,line,col*line),end=' ')
#     print()  #换行



def print_aline(end):
    for col in range(1,end+1):
        print('%d*%d=%2d' % (col,end,col*end),end=' ')
    print()

def print_99():
    for line in range(1,10):

        #打印一行
        print_aline(line)




print_99()
#学生管理项目
# 3. 改写之前的学生信息的程序,要求添加四个功能:
#     | 5)  按学生成绩高-低显示学生信息 |
#     | 6)  按学生成绩低-高显示学生信息 |
#     | 7)  按学生年龄高-低显示学生信息 |
#     | 8)  按学生年龄低-高显示学生信息 |



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

def get_chinese_char_count(x):
    count = 0  # 先假设个数为0
    for ch in x:
        # 如果ch为中文字典,则count 做加一操作
        if ord(ch) > 127:
            count += 1
    return count

    
def output_student(L):
    print("+---------------+----------+----------+")
    print("|     name      |   age    |   score  |")
    print("+---------------+----------+----------+")
    for d in L:
        n = d['name']
        a = d['age']
        s = d['score']
        chinese_cnt = get_chinese_char_count(n)
        print('|%s|%s|%s|' % (n.center(15-chinese_cnt),
                              str(a).center(10),
                              str(s).center(10)
                              )
              )

    # print("|    tarena     |    20    |     99   |")
    # print("|     name2     |    30    |     88   |")
    print("+---------------+----------+----------+")


def del_student(L):
    n = input('请输入要删除的学生的姓名: ')
    print("正在删除....", n)


def modify_student_score(L):
    print("正在修改学生成绩....")


def print_info_by_score_desc(L):
    def get_score(d):  # d是字典
        return d['score']

    L2 = sorted(L, key=get_score, reverse=True)
    output_student(L2)


def print_info_by_score_asc(L):
    def get_score(d):  # d是字典
        return d['score']

    L2 = sorted(L, key=get_score)
    output_student(L2)


def print_info_by_age_desc(L):
    L2 = sorted(L, key=lambda d: d['age'], reverse=True)
    output_student(L2)


def print_info_by_age_asc(L):
    L2 = sorted(L, key=lambda d: d['age'])
    output_student(L2)




def show_menu():
    print("+---------------------------------+")
    print("| 1)  添加学生信息                |")
    print("| 2)  显示学生信息                |")
    print("| 3)  删除学生信息                |")
    print("| 4)  修改学生成绩                |")
    print("| 5)  按学生成绩高-低显示学生信息 |")
    print("| 6)  按学生成绩低-高显示学生信息 |")
    print("| 7)  按学生年龄高-低显示学生信息 |")
    print("| 8)  按学生年龄低-高显示学生信息 |")
    print("| q)  退出                        |")
    print("+---------------------------------+")


def main():
    L = []
    while True:
        show_menu()
        s = input("请选择: ")
        if s == 'q':
            break
        elif s == '1':
            L += input_student()
        elif s == '2':
            output_student(L)
        elif s == '3':
            del_student(L)
        elif s == '4':
            modify_student_score(L)
        elif s == '5':
            print_info_by_score_desc(L)
        elif s == '6':
            print_info_by_score_asc(L)
        elif s == '7':
            print_info_by_age_desc(L)
        elif s == '8':
            print_info_by_age_asc(L)




main()