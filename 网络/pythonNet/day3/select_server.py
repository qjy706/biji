from select import select
from socket import *

s=socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',8888))
s.listen(5)
s.setblocking(False)
print(s.fileno())


rlist=[s]
wlist=[]
xlist=[]


while True:
#提交监测我们关注的io等待io发生 循环关注
    rs,ws,xs = select(rlist,wlist,xlist)
    print('有io事件发生')

    # c,addr=rs[0].accept()#每次返回的数值应该只有一个　可以用索引
    for r in rs:
        if r == s:
            c,addr=r.accept()
            print('connect from ',addr)
            rlist.append(c)#添加到关注列表
        else:
            data=r.recv(1024)
            if not data:
                rlist.remove(r)
                r.close() 
            else:
                print(data.decode())
                #讲客户端套接字放入wlist列表
                # wlist.append(r)
                r.send(b'Receive your message')

    # for w in ws:
    #     w.send(b'Receive your message')
    #     wlist.remove(w)

    # for x in xs:
    #     if x is s:
    #         s.close()

    