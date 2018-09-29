from socket import *
import os 
import sys
import time
import signal

HOST=''
PORT=8000
ADDR=(HOST,PORT)
FILE_PATH = '/home/tarena/桌面/笔记/网络/pythonNet/day8/FILE_PATH/'

class Ftpserver(object):
    def __init__(self,c):
        self.c = c

    def do_list(self):
        file_list = os.listdir(FILE_PATH)
        if not file_list:
            self.c.send('文件库为空'.encode())
            return
        else:
            self.c.send(b'ok')
            time.sleep(0.1)
            self.c.send('正在处理'.encode())
            time.sleep(2)

        files=''
        for file in file_list:
            if file[0] != '.' and os.path.isfile(FILE_PATH+file):
                files = files + file + '#'
        self.c.sendall(files.encode())

    def do_get(self,filename):
        try:
            p = open(FILE_PATH+filename,'rb')
        except:
            self.c.send('文件不存在'.encode())
            return
        self.c.send(b'ok')
        time.sleep(0.5)
        while True:
            data = f.read(1024)
            if not data:
                self.c.send(b'##')
            self.c.send(data)
        print('文件发送完毕')

    def do_put(self,filename):
        p = open(FILE_PATH+filename,'wb')
        self.c.send(b'ok')
        while True:
            data=self.c.recv(1024)
            if data == '##':
                print('接收完成')
                break
            p.write(data)
        p.close()
        


















def main():
    s=socket()
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(ADDR)
    s.listen(5)
    #处理子进程瑞出
    signal.signal(signal.SIGCHLD,signal.SIG_IGN)
    print('waiting......')
    while True:
        try:
            c,addr = s.accept()
        except KeyboardInterrupt:
            s.close()
            sys.exit('服务器退出')
        except Exception as e:
            print('Error:',e)
            continue

        print('已连接到客户端',addr)
        pid = os.fork()
        #创建了一个子进程
        if pid == 0:
            #父进程的套接字可以关闭了　因为子进程单独运行
            s.close()
            #创建对面的套接字
            ftp=Ftpserver(c)
            while True:
                #recv是阻塞函数
                data = c.recv(1024).decode()
                if not data or data[0] == 'Q':
                    c.close()
                    sys.exit('客户端退出')#子进程跟着退出
                elif data[0] == 'L':
                    ftp.do_list()
                elif data[0] == 'G':
                    filename=data.split(' ')[-1]
                    ftp.do_get(filename)
                elif data[0] == 'P':
                    filename=data.split(' ')[-1]
                    ftp.do_put(filename)

                    

        else:
            #这时候对面套接字关闭　等待下一个客户端连接
            c.close()
            continue











if __name__ == '__main__':
    main()