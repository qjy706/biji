from socketserver import *

#先创建服务器类　

class Server(ForkingMixIn,TCPServer):
#class Server(ForkingTCPServer):
#class Server(ThreadinggMixIN,TCPServer):
#class Server(ThreadingTCPServer):
    pass 

#TCPServer 与　StreamRequestHandler相对应
class Handler(StreamRequestHandler):
    #重写一个handler函数　
    def handler(self):
        #self.request == accept返回的套接字　
        print('Connect from ',self.request.getpeername())
        while True:
            data = self.request.recv(1024)
            if not data :
                break
            print(data.decode())
            self.request.send(b'Receive')


if __name__ == '__main__':
    server_addr = ('0.0.0.0',8888)



    #创建服务器对象　需要传入自己的服务器地址和端口
    server = Server(server_addr,Handler)

    #启动服务器　
    server.serve_forever()


