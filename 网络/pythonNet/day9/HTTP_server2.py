#coding=utf-8
'''
http server v2.0
1.多线程并发
2.可以请求简单数据
3.能进行简单请求解析
4.结构使用类进行封装
'''


#1 socket tcp 套接字　
# ２　http协议的请求响应格式　
# ３　线程并发的创建方法　
# ４　类的基本使用


#os.listdir(PATH)
from socket import *
from threading import Thread
import sys
import traceback


#httpserver 类　封装具体的服务器功能　
class HTTPServer(object):
    def __init__(self,server_addr,static_dir):
        self.server_address = server_addr
        self.static_dir = static_dir
        self.ip = server_addr[0]
        self.port = server_addr[1]
        #创建套接字
        self.create_socket()

    def create_socket(self):
        #这时候套接字也是属性了
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
        self.sockfd.bind(self.server_address)

#运行等待客户端连接
    def serve_forever(self):
        self.sockfd.listen(5)
        print('listen the port %d'%self.port)
        while True:
            try:#没必要self.connfd　跟connfd没区别　
                connfd,addr = self.sockfd.accept()
            except KeyboardInterrupt:
                self.sockfd.close()
                sys.exit('服务器退出')
            except Exception:
                traceback.print_exc()#错误的详细信息
                continue
            #创建新的线程　处理请求 #需要把connfd进行带入　以免新的客户端过来之后修改connfd　这是类变量
            clientThread = Thread(target = self.handleRequest,args=(connfd,))
            clientThread.setDaemon(True)
            clientThread.start()
#客户端请求函数 根据请求内内容返回具体的东西
    def handleRequest(self,connfd):
        #接收客户端请求
        request = connfd.recv(4096)
        print(request)
        #解析请求内容
        requestHeaders = request.splitlines()#按照\r\n行分割
        print(requestHeaders)
        #查看请求头 因为请求头在第一行　
        print(connfd.getpeername(),':',requestHeaders[0])

        #获取请求的具体内容
        #　　　　格式：　GET     空格　　 /        　　　HTTP/1.1 
        # 请求类别　　　　　　请求内容　　　　　　　　协议版本
        getRequest = str(requestHeaders[0]).split(' ')[1]
        if getRequest == '/' or getRequest[-5:] == '.html':
        #结尾五个肯定是.html
            self.get_html(connfd,getRequest)
        else:
            self.get_data(connfd,getRequest)
        connfd.close()


    def get_html(self,connfd,getRequest):
        if getRequest == '/':
            filename = self.static_dir + '/index.html'
        else:
            filename = self.static_dir + getRequest
        try:
            f=open(filename)
        except Exception:
            response='HTTP/1.1 404  not found\r\n'
            response += '\r\n'#空行
            response += '====sorry not found===='
        else:
            response='HTTP/1.1 200 ok\r\n'
            response += '\r\n'
            response += f.read()
        finally:
            connfd.send(response.encode())

    def get_data(self,connfd,getRequest):
        urls = ['/time','/tedu','/python']
        if getRequest in urls:
            responsehead='HTTP/1.1 202  ok\r\n'
            responsehead += '\r\n'#空行
            if getRequest == '/time':
                import time 
                responsebody = str(time.ctime())
            elif getRequest == '/tedu':
                responsebody = 'welcome to tedu'
            elif getRequest == '/python':
                responsebody = '人生苦短'

        else:
            responsehead='HTTP/1.1 404  not found\r\n'
            responsehead += '\r\n'#空行
            responsebody = 'sorry not found'

        response = responsehead+responsebody
        connfd.send(response.encode())

if __name__ == '__main__':
    #服务器地址
    server_addr = ('0.0.0.0',8000)
    #静态网页文件　（可以写静态网页文件夹路径)
    static_dir = '/home/tarena/桌面/笔记/网络/pythonNet/day9/static'
# 创建服务器对象 可参照sock_class_server.py
    httpd = HTTPServer(server_addr,static_dir)

#启动服务器
    httpd.serve_forever()