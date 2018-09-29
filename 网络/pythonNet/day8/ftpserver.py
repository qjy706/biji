#! /usr/bin/env python3 

import os,sys 
from socket import *
import signal

class Sock:
    def __init__(self,host='0.0.0.0',port=9999):
        self.host=host
        self.port=port

    def sock(self):
        self.s=socket()
        self.s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
        self.s.bind((self.host,self.port))
        self.s.listen(5)

    def acc(self):
        self.sock()
        while True:
            try:
                self.c,self.addr = self.s.accept()
            except KeyboardInterrupt:
                sys.exit('服务器退出')
            except Exception as e:
                print('Error:',e)
                continue
            self.pid = os.fork()
            if self.pid == 0:
                self.s.close()
                self.client_handler(self.c)
            else:
                self.c.close()
                continue

    def client_handler(self,c):
        print('处理子进程请求',c.getpeername())
        try:
            while True:
                data = c.recv(1024)
                if not data:
                    break
                print(data.decode())
                c.send('收到请求'.encode())
        except (KeyboardInterrupt,SystemError):
                self.sys.exit('客户端推出')
        except Exception as e:
            print(e)
        c.close()
        sys.exit(0)

    def osfrok(self):
        self.acc()

s=Sock()
s.osfrok()


