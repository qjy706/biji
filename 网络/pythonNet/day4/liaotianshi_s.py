from socket import *
from select import *
import os

s=socket(AF_INET,SOCK_STREAM)

s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

s.bind(('0.0.0.0',5000))

s.listen(10)

rlist=[s]
wlist=[]
xlist=[]

while True:
    rs,ws,xs=select(rlist,wlist,xlist)
    for rs in rlist:
        if rs == s:
            c,addr=s.accept()
            rlist.append(c)
            print('{} enter romm '.format(addr))

        else:
            try:
                data=recv(4096)
                for x in rs:
                    if x != s and x != c:
                        try:
                            x.send(data)
                        except:
                            x.close()
                            rlist.remove(x)

            except:
                print('客户端　{} 已经下线'.format(addr))
                c.close()
                rlist.remove(c)
s.close()

#一个进程占用计算机　核心　称为占用时间片

