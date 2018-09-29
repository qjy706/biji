from socket import *
import time
import sys

class Ftpclient(object):
    def __init__(self,s):
        self.s = s

    def do_list(self):
        self.s.send(b'L')
        data=self.s.recv(1024).decode()
        if data == 'ok':
            b=self.s.recv(1024).decode()
            print(b)
            a=self.s.recv(1024).decode()
            file = a.split('#')
            for i in file:
                print(i)
        else:
            #由服务器发送失败原因
            print(data)

    def do_get(self,filename):
        self.s.send(('G '+filename).encode())
        data = self.s.recv(1024).decode()
        if data == 'ok':
            p = open('filename','wb')
            while True:
                d = self.s.recv(1024)
                if d == b'##':
                    break
                p.write(d)
            p.close()
            print('%s 下载完毕\n'%filename)
        else:
            print(data)

    def do_put(self,filename):
        self.s.send(('P '+filename).encode())
        try:
            p = open('filename','rb')
        except:
            print('文件不存在')
            return
        data=self.s.recv(1024).decode()
        if data == 'ok':
            while True:
                d = p.read(1024)
                if not d:
                    self.s.send(b'##')
                    break
                self.s.send(d)
        print('文件发送完毕')

    def do_quit(self,filename):
        self.sockfd.send(filename.encode())












def main():
    if len(sys.argv) < 3:
        print('请按照正确格式输')

    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    ADDR = (HOST,PORT)
    s = socket()
    try:
        s.connect(ADDR)
    except:
        print('连接服务器失败')
        return

    ftp = Ftpclient(s)
    while True:
        print('======= 命令选项 =======')
        print('******  list  *******')
        print('****** get file******')
        print('******put file*******')
        print('******  list  *******')
        print('=======================')
        print('获取文件请输入get　文件名称')

        cmd = input('请输入')

        if cmd == 'list':
            ftp.do_list()
        elif cmd[:3] == 'get':
            filename=cmd.split(' ')[-1]
            ftp.do_get(filename)
        elif cmd[:3] == 'put':
            filename=cmd.split(' ')[-1]
            ftp.do_put(filename)
        elif cmd.strip() == 'Q':
            filename = cmd.strip()
            ftp.do_quit(filename)
        else:
            print('请输入正确命令')
            continue

if __name__ == '__main__':
    main()



















if __name__ == '__main__':
    main()