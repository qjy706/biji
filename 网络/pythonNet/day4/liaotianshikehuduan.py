from socket import *
from select import *

s=socket()

s.connect(('127.0.0.1',5000))


while True:
    rlist=[s]
    wlist=[]
    xlist=[]

    rs,ws,xs=select(rlist,wlist,xlist)
    