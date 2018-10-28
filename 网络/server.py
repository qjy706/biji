import os
import sys
from socket import *
# 写一个聊天室　

# 功能　：类似qq群聊　
# １．进入聊天室需要输入姓名，姓名不能重复　

# ２．有人进入聊天室，会向其他人发送通知　新的连接套接字　

# ３．一个人发消息，其他人会受到消息， (addr)
# 　　　　xxx 说：　xxxxxxx
# print (f,'say',c.send(data.encode()))
# 4.某人退出聊天室，其他人也会收到通知　

# ５　管理员发消息　


# def main():
#     ADDR=('0.0.0.0',8000)
#     s=socket(AF_INET,SOCK_DGRAM)
#     s.bind(ADDR)

#     pid = os.fork()
#     if pid < 0:
#         sys.exit('服务器错误')
#     elif pid == 0:
#         do_child(s,addr)
#     else:
#         do_parents(s)

# def do_child(s,addr):
#     while True:
#         data = input('请输入管理员信息')
#         msg = 'C 管理员'+data
#         s.sendto(msg.encode(),addr)

# def do_parents(s):
#     user = {}
#     while True:
#         msg,addr= s.recvfrom(1024)
#         data = msg.decode().split(' ')
#         if data[0] == 'L':
#             do_login(user,s,addr,data[1])
#         elif data[0] == 'C':#用空格把列表索引２以后的全部连接起来　
#             do_chat(s, user, data[1], ' '.join(data[2:]))
#         elif data[0] == 'Q':
#             do_quit(s, user, data[1])

# def do_login(user,s,addr,name):
#     if name in user:
#         s.sendto('用户存在'.encode())

#     s.sendto(b'ok',addr)
#     mag = '\n欢迎 {} 进入聊天室'.format(name)
#     for i in user:
#         s.sendto(mag.encode(),user[i])

#     user[name]=addr


# def do_chat(s, user, name, text):
#     msg = '\n{}　说:{}'.format(name, text)
#     for i in user:
#         if i != name:
#             s.sendto(msg.encode(), user[i])


# def do_quit(s, user, name):
#     msg = '\n' + name + "退出聊天室"
#     for i in user:
#         if i == name:
#             s.sendto(b'EXIT', user[i])
#         else:
#             s.sendto(msg.encode(), user[i])
# # 从字典当中删除用户
#     del user[name]


