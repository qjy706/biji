# 想象成列表　每一行都是列表　中间用逗号分隔　
# 先得到每一个列表　
# 转成字符串　以最长一个字符串居中显示
# 第二行　
def getnextline(L):
    #此函数将用一层的列表Ｌ计算下一层然后返回
    # L=[1,3,3,1],则返回[1,4,6,4,1]
    line=[1]  #最左侧的1 
    #计算中间数字
    for i in range(len(L)-1):  # i绑定Ｌ的索引　最右的１不用管
        line.append(L[i]+L[i+1])  # 由上一行算下一行中间的数值
    #在最后放入一个1
    line.append(1)
    return line


def getyanghuilist(n):   #代表行数
    L=[]
    line= [1]  #第一行
    for x in range(n):　　
        L.append(line)　　# 当前行放进去
        #计算出下一行　准备放入
        line=getnextline(line)
    return L
def list_to_srting(L):
    '''将函数任意给定一个列表　，将其转换为字符串
    如　Ｌ＝［１，２］　则返回＇１，２＇'''
    L2=[str(x) for x in L]
    return ' '.join(L2)

#得到最下面一行占几个字符宽度
max_char=len(list_to_srting(L[-1]))
#居中显示
 

