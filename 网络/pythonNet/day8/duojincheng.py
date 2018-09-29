from socket import *
import os,sys
import signal

HOST = ''
PORT = 8888
ADDR = (HOST,PORT)

s=socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(ADDR)
s.listen(5)

print('等待')

signal.signal(signal.SIGCHLD,signal.SIG_IGN)

while True:
    try:
        c,addr = s.accept()
    except KeyboardInterrupt:
        sys.exit('服务器退出')
    except Exception as e:
        print('Error:',e)
        continue

    pid = os.fork()
    
    if pid == 0:
        s.close()
        client_handler(c)

    else:
        c.close()
        continue
