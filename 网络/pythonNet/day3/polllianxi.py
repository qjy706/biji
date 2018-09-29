from socket import *
from select import *

#创建套接字作为我们关注的IO
s=socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',8888))
s.listen(5)
s.setblocking(False)

p=poll()

fdmap={s.fileno():s}

p.register(s,POLLIN|POLLERR)

while True:
    events=p.poll()

    for x,y in events:
        if x == s.fileno():
            c,addr=s.accept()
            print('connect from ',addr)
            p.register(c,POLLIN)
            fdmap[c.fileno()]=c

        elif y & POLLIN:
            data=fdmap[x].recv(4096)
            if not data:
                p.unregister(x)
                fdmap[x].close()
                del fdmap[x]
            else:
                print(data.decode())
                fdmap[x].send(b'Receive')


