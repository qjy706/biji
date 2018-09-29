from socket import *


def handleclient(connfd):
    request=connfd.recv(4096)
    # print(request)
    request_lines=request.splitlines()
    #根据换行符分割
    for line in request_lines:
        print(line.decode())

    try:
        f=open('index.html')

    except IOError:
       #响应头　相应体　空行　发送的东西
        response='HTTP/1.1 404  not found\r\n'
        response += '\r\n'#空行
        response += '====sorry not found===='
    else:
        response='HTTP/1.1 200 ok\r\n'
        response += '\r\n'
        response += f.read()
    finally:
        connfd.send(response.encode())



#创建套接字
def main():
    sockfd=socket(AF_INET,SOCK_STREAM)

    sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

    sockfd.bind(('0.0.0.0',8888))

    sockfd.listen(5)
    print('Listen to the port 8888')

    while True:
        connfd,addr=sockfd.accept()
        #处理请求

        handleclient(connfd)
        connfd.close()

if __name__ == '__main__':
    main()
