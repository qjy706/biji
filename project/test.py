def work(data):
    p = open('dict.txt')
    for i in p:
        name=i.split(' ')
        if data == name[0]:
            print(i)

if __name__ == '__main__':
    data = input('请输入')
    work(data)