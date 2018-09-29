from socketserver import *

#先创建服务器类　
#多线程udp并发


class Server(ThreadingMixIn,UDPServer):
#class Server(ForkingTCPServer):
#class Server(ThreadinggMixIN,TCPServer):
#class Server(ThreadingTCPServer):
    pass 

#TCPServer 与　StreamRequestHandler相对应
class Handler(DatagramRequestHandler):
    #重写一个handler函数　
    def handler(self):
        #self.request == accept返回的套接字
        print(self.client_address)
        print(self.request)
        while True:
            data=self.rfile.reandline(1024)
            #用来读取发送的内容
            print(self.client_address)
            if not data :
                break
            print(data.decode())
            self.wfile.write(b'6666')

if __name__ == '__main__':
    server_addr = ('176.8.18.212',8888)



    #创建服务器对象　需要传入自己的服务器地址和端口
    server = Server(server_addr,Handler)

    #启动服务器　
    server.serve_forever()