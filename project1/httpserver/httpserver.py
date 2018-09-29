from socket import *
import sys
#用正则请求更灵活
import re
from threading import Thread
#导入配置文件
from settings import *
import time
import traceback


class HTTPServer(object):
    def __init__(self,addr=('0.0.0.0',80)):
        self.addr = addr
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
        self.bind(addr)

    def bind(self,addr):
        self.ip = addr[0]
        self.port =addr[1]
        self.sockfd.bind(addr)
    #http服务器启动
    def server_forever(self):
        self.sockfd.listen(10)
        print('listen the port %d...'%self.port)
        while True:
            try:
                connfd,addr = self.sockfd.accept()
                print('Connect from',addr)
            except:
                traceback.print_exc()
                sys.exit('服务器退出')
            handle_client = Thread(target = self.handle_request,args=(connfd,))
            handle_client.setDaemon(True)
            handle_client.start()

    def handle_request(self,connfd):
        #接收浏览器请求
        request = connfd.recv(4096)
        request_lines = request.splitlines()
        #获取请求航
        request_line = request_lines[0].decode()

        #正则提取请求方法和请求内容
        pattern = r'(?P<METHOD>[A-Z]+)\s+(?P<PATH>/\S*)'
        #用match匹配 捕获组名字为键　内容为值
        try:
            env = re.match(pattern,request_line).groupdict()
        except:
            response_headlers = 'HTTP/1.1 500 Server Error\r\n'
            response_headlers += '\r\n'
            response_body = 'Server Error'
            response = response_headlers+response_body
            connfd.send(response.encode())
            return
    #      发送给框架WebFrame
    #      将数据发送给WebFrame
    # 　　　　　从WebFrame接收反馈数据
    #      设置两个函数返回值　
    #　　　　　　将请求发给frame 得到返回的数据结果
        status,response_body = self.send_request(env['METHOD'],env['PATH'])
# 根据响应码组织响应头内容
        response_headlers = self.get_headlers(status)
# 将结果组织为http response 发送给客户端
        response = response_headlers + response_body
        connfd.send(response.encode())
        connfd.close()


#和frame交互，发送request获取response 该程序设置为客户端　因为谁先收谁是服务端
#发送注意粘包　
    def send_request(self,method,path):
        s = socket()
        s.connect(frame_addr)

        #向webframe发送method　和 path（请求内容）
        s.send(method.encode())
        time.sleep(0.1)
        s.send(path.encode())
#接受请求
        status = s.recv(1024).decode()
        response_body = s.recv(4096).decode()

        return status,response_body


    def get_headlers(self,status):
        if status == '200':
            response_headlers = 'HTTP/1.1 200 OK\r\n'
            response_headlers += '\r\n'
        elif status == '404':
            response_headlers = 'HTTP/1.1 404 NOT Found\r\n'
            response_headlers += '\r\n'          

        return response_headlers

















if __name__ == '__main__':
    httpd = HTTPServer(ADDR)
    httpd.server_forever()

