#阻塞服务
# from socket import *

# from time import sleep,ctime 

# s=socket()
# s.bind(('0.0.0.0',9999))
# s.listen(5)

# #将套接字设置为非阻塞
# s.setblocking(False)

# while True:
#     print('waiting.....')
#     try:
#         c,addr=s.accept()
#     except BlockingIOError:
#         sleep(2)
#         print(ctime())
#         continue

#     else:
#         while True:
#             data=c.recv(4096).decode()
#             if not data:
#                 break
#             print(data)
#             c.send(ctime().encode())
#     c.close()
# s.close()



# from socket import *
# from time import sleep,ctime

# s=socket()
# s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
# s.bind(('0.0.0.0',9999))
# s.listen(5)

# s.setblocking(False)

# while True:
#     print('waiting.....')
#     try:
#         c,addr=s.accept()
#     except BlockingIOError:
#         sleep(2)
#         print(ctime())
#         continue
#     else:
#         print('connect from {}'.format(addr))
#         while True:
#             data=c.recv(1024).decode()
#             if not data:
#                  break
#             print(data)
#             c.send(ctime().encode())
#         c.close()
# s.close()

#阻塞
# from socket import *
# from time import ctime,sleep

# s=socket()
# #释放端口
# s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
# s.bind(('0.0.0.0',9999))
# s.listen(5)
# #设置为非阻塞
# s.setblocking(False)

# while True:
#     print('waiting....')
#     try:#有无客户端链接
#         c,addr=s.accept()
#     except BlockingIOError:#没有的话就会报错　但是继续上一层循环
#         sleep(2)
#         print(ctime())
#         continue
#     else:
#         print('connect from {}'.format(addr))
#         while True:
#             data=c.recv(1024).decode()
#             if not data:
#                 break
#             print(data)
#             c.send(ctime().encode())
#         c.close()
# s.close()





# import socket
# import select 
# # import Queue
# # Create a TCP/IP socket, and then bind and listen
# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.setblocking(False)
# server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# server_address = ("0.0.0.0", 10001)
 
# print("Starting up on %s port %s" % server_address)
# server.bind(server_address)
# server.listen(5)
# message_queues = {}
# #The timeout value is represented in milliseconds, instead of seconds.
# timeout = 1000
# # Create a limit for the event
# READ_ONLY = ( select.POLLIN | select.POLLPRI | select.POLLHUP | select.POLLERR)
# READ_WRITE = (READ_ONLY|select.POLLOUT)
# # Set up the poller
# poller = select.poll()
# poller.register(server,READ_ONLY)
# #Map file descriptors to socket objects
# fd_to_socket = {server.fileno():server,}
# while True:
#     print("Waiting for the next event")
#     events = poller.poll(timeout)
#     print("*"*20)
#     print(len(events))
#     print(events)
#     print("*"*20)
#     for fd ,flag in  events:
#         s = fd_to_socket[fd]
#         if flag & (select.POLLIN | select.POLLPRI) :
#             if s is server :
#                 # A readable socket is ready to accept a connection
#                 connection , client_address = s.accept()
#                 print(" Connection " , client_address)
#                 connection.setblocking(False)
                 
#                 fd_to_socket[connection.fileno()] = connection
#                 poller.register(connection,READ_ONLY)
                 
#                 #Give the connection a queue to send data
#                 message_queues[connection]  = Queue.Queue()
#             else :
#                 data = s.recv(1024)
#                 if data:
#                     # A readable client socket has data
#                     print("  received %s from %s " % (data, s.getpeername()))
#                     message_queues[s].put(data)
#                     poller.modify(s,READ_WRITE)
#                 else :
#                     # Close the connection
#                     print("  closing" , s.getpeername())
#                     # Stop listening for input on the connection
#                     poller.unregister(s)
#                     s.close()
#                     del message_queues[s]
#         elif flag & select.POLLHUP :
#             #A client that "hang up" , to be closed.
#             print(" Closing ", s.getpeername() ,"(HUP)")
#             poller.unregister(s)
#             s.close()
#         elif flag & select.POLLOUT :
#             #Socket is ready to send data , if there is any to send
#             try:
#                 next_msg = message_queues[s].get_nowait()
#             except Queue.Empty:
#                 # No messages waiting so stop checking
#                 print(s.getpeername() , " queue empty")
#                 poller.modify(s,READ_ONLY)
#             else :
#                 print(" sending %s to %s" % (next_msg , s.getpeername()))
#                 s.send(next_msg)
#         elif flag & select.POLLERR:
#             #Any events with POLLERR cause the server to close the socket
#             print("  exception on" , s.getpeername())
#             poller.unregister(s)
#             s.close()
#             del message_queues[s]



# from socket import *
# from select import *
# from time import sleep,ctime
# #创建一个连接套接字
# s=socket()
# #释放端口　这一步要在绑定之前进行
# s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
# #绑定端口
# s.bind(('0.0.0.0',8888))
# #套接字监听
# s.listen(5)
#设置非阻塞
# s.setblocking(False)

# #创建一个列表　里面放进需要关注的套接字
# rlist=[s]
# wlist=[]
# xlist=[]
# print('waiting')
# while True:
# #关注ＩＯ发生
#     rs,ws,xs=select(rlist,wlist,xlist)
#     #每个客户端调用会返回一单个元素的列表
#     for r in rs:
#         if r == s:
#              c,addr=r.accept()
#             print('connect from ',addr)
#              rlist.append(c)
#              #把客户端套接字加入进关注列表
#         else:
#              data=r.recv(4096)
#              if not data:
#                   rlist.remove(c)
#                  r.close()
#              else:
#                 print(data.decode())
#                 r.send(b'Receive your message')

    # for r in rs:
    #     if r == s:
    #         c,addr=r.accept()
    #         print('connect from',addr)
    #         rlist.append(c)
    #     else:
    #         data=r.recv(4096)
    #         if not data:
    #             rlist.remove(r)
    #             r.close()
    #         else:
    #             print(data.decode())
    #             r.send('已收到消息'.encode())




# from socket import *
# from select import *
# from time import sleep,ctime
# #创建一个连接套接字
# s=socket()
# #释放端口　这一步要在绑定之前进行
# s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
# #绑定端口
# s.bind(('0.0.0.0',8888))
# #套接字监听
# s.listen(5)
# #设置非阻塞
# s.setblocking(False)

# #创建一个列表　里面放进需要关注的套接字
# rlist=[s]
# wlist=[]
# xlist=[]
# print('waiting')
# while True:
#     try:
#         rs,ws,xs=select(rlist,wlist,xlist)
#         if s == rs[0]:
#             c,addr=s.accept()
#             print('connect from',addr)
#             rlist.append(c)
#         elif c == rs[0]:
#             data=c.recv(4096)
#             if not data:
#                 rlist.remove(c)
#                 rs[0].close()
#             else:
#                 print(data.decode())
#                 rs[0].send('已收到消息'.encode())
#     except timeout:
#         print(ctime())
#         continue


from socket import *
from select import *

s=socket()

s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

s.bind(('0.0.0.0',9999))

s.listen(10)

s.setblocking(False)

rlist=[s]
wlist=[]
xlist=[]

while True:
    rs,ws,xs=select(rlist,wlist,xlist)
    for r in rs:
        if r == s:
            c,addr=r.accept()
            print('from {} 连接'.format(addr))
            rlist.append(c)
        elif r == c:
            data=r.recv(1024).decode()
            if not data:
                rlist.remove(r)
                r.close()
            else:
                print(data)
                r.send(b'666')
s.close()