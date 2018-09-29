# １，写一个程序，打印电子时间：
# 格式为：
# HH:MM:SS

# import time 


# while True:
#     t=time.localtime()
#     L=time.asctime(t)
#     s=L.split(' ')
#     print(s[3],end='\r')
#     time.sleep(1)




# 2 编写一个闹钟程序，启动时设置定时间，到时间打印一句
# ＇时间到＇，然后退出程序

import time
def alarm(n,m):
    while True:
        t=time.localtime()
        print('%02d:%02d:%02d' % t[3:6],end='\r')
        # if (h,m) == t[3:5]
        if n == t[3] and m == t[4]:
            print('时间到')
            break
hour=int(input('请输入定时小时'))
minute=int(input('请输入分钟'))
alarm(hour,minute)


#L[3:5] 是一个元组　　可以哟你