# 100下坠　，每次弹起高度是原高度的一般　弹十次的高度　　和总的距离


def high(n):
    s=0
    L=[n]
    while s <= 10:
        h=n/2
        s+=1
        L.append(h)
    return L,sum(L)