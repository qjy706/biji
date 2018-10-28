# abcdefghi jklmnqpqr stuvwxyz*





def main():
    s = input('请输入月份和日子,用空格隔开')
    a = input('请输入信息')
    m = int(s.split(' ')[0])
    d = int(s.split(' ')[1])
    shuai(m,d,a)


def shuai(m,d,a):
    L1 = ['a','b','c','d','e','f','g','h','i']
    L2 = ['j','k','l','m','n','q','p','q','r']
    L3 = ['s','t','u','v','w','x','y','z','*']
    L=[L1,L2,L3]
    if m % 3 == 0:
            L[0],L[1],L[2] = L3,L1,L2
    elif m % 3 == 2:
            L[0],L[1],L[2] = L2,L3,L1

    s = 0 
    d = d -1
    if d % 8 == 0; 

    for x in L:
        i  =  0
        for i in L[i]:














if __name__ == '__main__':
    main()








