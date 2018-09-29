from socket import *
import sys
import os 
import time 
from threading import Thread
import traceback


class Tanks(object):
    def __init__(self,ADDR,file_path,keymap):
        self.addr = ADDR
        self.host = ADDR[0]
        self.port = ADDR[1]
        self.file_path = file_path
        self.keymap = keymap
        self.create_s()

    def create_s(self):
        self.s = socket()
        self.s.setblocking(SOL_SOCKET,SO_REUSEADDR,1)
        self.s.bind(self.addr)

    def start(self):
        self.s.listen(10)
        print('listen the port {}'.format(self.port))
        while True:
            try:
                c,addr = self.s.accept()
            except KeyboardInterrupt:
                self.s.close()
                sys.exit('服务器退出')
            except:
                traceback.print_exc()
                continue

        tanksThread = Thread(target = self.handler ,args=(c,))
        tanksThread.setDaemon(True)
        tanksThread.start()

    def handler(self,c):
        user={}
        msg = c.recv(4096).decode()
        name = msg.split(' ')[0]
        password = msg.split(' ')[1]

        for i in user:
            if i != name:
                c.send('用户不存在,正为您创建用户'.encode())
                time.sleep(2)
                user[name]=password
                c.send('正在为您登录'.encode())
                time.sleep(2)
                continue
            else:
                self.play(c)

    def play(self,c):
        pass

    def up(self):
        pass

    def down(self):
        pass

    def right(self):
        pass

    def left(self):
        pass





















if __name__ == '__main__':
    ADDR = ('',8000)
    file_path = ''
    keymap = {'a': tanks.left,'d': tanks.right,
    'w': tanks.up,
    's': tanks.down,
    'Left': tanks.left,
    'Right': tanks.right,
    'Up': tanks.up,
    'Down': tanks.down}
    tanks=Tanks(ADDR,file_path,keymap)
    tanks.start()





