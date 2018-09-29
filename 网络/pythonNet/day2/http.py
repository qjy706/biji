from socket import *
#创建tcp套接字
s=socket()
s.bind(('0.0.0.0',10000))
s.listen(5)
while True:
    c,addr=s.accept()
    print('connect from',addr)

    data=c.recv(4096)
    print('*****************')
    print(data)#浏览器发来的http请求
    print('*****************')

    #组织响应内容
    data='''HTTP/1.1 200 ok
    Content-Encoding: gzip
    Content-Type: text/html

    <h1>Welcome to tedu</h1>
    '''
    c.send(data.encode())
    c.close()

s.close()