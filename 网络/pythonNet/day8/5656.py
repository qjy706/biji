from socket import *
import os 
import sys 


def main():
    sockfd = socket()
    sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    sockfd.bind('',8000)
    sockfd.listen(5)
    signal.signal(signal.SIGCHLD,signal.SIG_IGN)
    while True:
        try:
            c,addr=sockfd.accept()
        except KeyboardInterrupt:
            sockfd.close()
            sys.exit('服务器退出')
        except Exception:
            continue
        pid = os.fork()
        if pid == 0:
            sockfd.close()
            ftp.FtpServer(c)



