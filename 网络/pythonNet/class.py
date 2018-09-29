from socket import *
from select import *

class Tcp:
    def __init__(self,AF=AF_INET,SOCK=SOCK_STREAM):
        self.AF=AF
        self.SOCK=SOCK
        self.s=socket(self.AF,self.SOCK)

    def open(self,addr=('0.0.0.0',5000),l=5):
        self.s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
        self.s.bind(addr)
        self.s.setblocking(False)
        self.s.listen(l)

    def clos(self):
        self.s.close()


    def select(self):
        self.open()
        rlist=[self.s]
        wlist=[]
        xlist=[]
        print('waiting')
        while True:
            #循环关注
            rs,ws,xs=select(rlist,wlist,xlist)
            #遍历　
            for r in rs:
                if r == self.s:
                    c,addr=r.accept()
                    print('connect from {}'.format(addr))
                    #该客户端的套接字放进被动列表
                    rlist.append(c)
                else:
                    try:
                        data=r.recv(4096)
                        print(data.decode())
                        r.send(b'666')
                    except:
                        r.close()
                        rlist.remove(r)


s=Tcp()

s.select()
        