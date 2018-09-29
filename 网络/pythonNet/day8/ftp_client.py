from socket import *
import sys 
import time 

#基本文件操作功能

class FtpClient(object):
    def __init__(self,sockfd):
            self.sockfd = sockfd

    def do_list(self):
        self.sockfd.send(b'L')#发送请求
            #等待回复　
        data=self.sockfd.recv(1024).decode()
        if data == 'ok':
            data = self.sockfd.recv(4096).decode()
            files = data.split('#')
            L=[]
            for file in files:
                L.append(file)
            print(L)
        else:
            #由服务器发送失败原因
            print(data)
    def do_get(self,filename):
        self.sockfd.send(('G '+filename).encode())
        data = self.sockfd.recv(1024).decode()
        if data == 'ok':#可以想象成三次握手　发送请求　回复确定　再次发送文件
            fd = open(filename,'wb')
            while True:
                data = self.sockfd.recv(1024)
                if data == b'##':
                    break
                fd.write(data)
            fd.close()
            print('%s 下载完毕\n'%filename)

        else:
            print(data)

    def do_put(self,filename):
        self.sockfd.send(('P '+filename).encode())
        data = self.sockfd.recv(1024).decode()
        if data == 'ok':
            try:
                fd = open(filename,'rb')
            except:
                print('文件不存在')
                return
            while True:
                data = fd.read(1024)
                if not data:
                    time.sleep(0.1)
                    self.sockfd.send(b'##')
                    break
                self.sockfd.send(data)
            print('发送完毕')
            fd.close()

    def do_quit(self,filename):
        self.sockfd.send(filename.encode())








def main():
    if len(sys.argv) < 3:
        print('argv is error')
        return
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    ADDR = (HOST,PORT)#文件服务器地址
    sockfd = socket()

    try:
        sockfd.connect(ADDR)
    except:
        print('连接服务器失败')
        return
    ftp=FtpClient(sockfd)#功能类对象
    while True:
        print('======= 命令选项 =======')
        print('******  list  *******')
        print('****** get file******')
        print('******put file*******')
        print('******  list  *******')
        print('=======================')

        cmd = input('请输入命令')

        if cmd == 'list':
            ftp.do_list()
        elif cmd[:3] == 'get':#命令输入get xxx
            filename = cmd.split(' ')[-1]
            ftp.do_get(filename)

        elif cmd.strip() == 'Q':
            filename = cmd.strip()
            ftp.do_quit(filename)

        elif cmd[:3] == 'put':#命令输入put xxx
            filename = cmd.split(' ')[-1]
            ftp.do_put(filename)
        else:
            print('请输入正确命令')
            continue
#调用    

if __name__ == '__main__':
    main()