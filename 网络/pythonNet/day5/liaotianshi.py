#! /usr/bin/env python3
# coding=utf-8
'''
name:qqq
email:
date:2018-9
class: AID
introduce: Chatroom server
env: python3.5 
'''


# 写一个聊天室　

# 功能　：类似qq群聊　
# １．进入聊天室需要输入姓名，姓名不能重复　

# ２．有人进入聊天室，会向其他人发送通知　新的连接套接字　

# ３．一个人发消息，其他人会受到消息， (addr)
# 　　　　xxx 说：　xxxxxxx
# print (f,'say',c.send(data.encode()))
# 4.某人退出聊天室，其他人也会收到通知　

# ５　管理员发消息　

# 功能模型　转发
# 技术　　套接字　udp 不需要连接　
# 用户存数　：　字典或列表　
# 消息收发的随意性：　多进程　收发单独　

# 代码设计　:　　１，封装　（每个功能封装为函数）
# 　　　　　　　　　　　２，接口测试（每实现一部就测试一步）
# 代码编写流程　
# 搭建网络连接　－－＞　创建多进程　－－＞　每个进程功能编写　
# －－＞　项目功模块实现
# 进入聊天室　
# 客户端：　输入姓名　讲信息发给服务端　　设定一个专门的标志　(L,name) L代表发信息　
# 　　　　　　　　等待服务端回复　　根据回复判断是否登录　


# 服务端：　接收请求信息，判断请求类型　
# 　　　　　　　　判断用户名是否存在　　如果存在回复不能登录　如果不存在　回复可以登录　并插入到数据结构　
# 　　　　　　　　发送通知给其他用户　
# 聊天　　
# 客户端　创建父子进程　发送聊天请求/接收聊天信息　
# 服务端　接收请求信息　将消息转发给其他用户


from socket import *
import os
import sys
# 登录判断


def do_login(s, user, name, addr):
    # 还有一个管理员消息
    if (name in user) or name == '管理员':
        s.sendto('该用户已存在'.encode(), addr)
        return

    s.sendto(b'ok', addr)
    # 通知其他人　
    mag = '\n欢迎 {} 进入聊天室'.format(name)
    for i in user:
        s.sendto(mag.encode(), user[i])
# 插入用户　
    user[name] = addr

# 发送聊天消息


def do_chat(s, user, name, text):
    msg = '\n{}　说:{}'.format(name, text)
    for i in user:
        if i != name:
            s.sendto(msg.encode(), user[i])


def do_quit(s, user, name):
    msg = '\n' + name + "退出聊天室"
    for i in user:
        if i == name:
            s.sendto(b'EXIT', user[i])
        else:
            s.sendto(msg.encode(), user[i])
# 从字典当中删除用户
    del user[name]


# 接收客户端请求 参数是套接字　
def do_parent(s):
    # 接收请求信息
    user = {}
    # 如果是一个可变的函数，传参会影响函数值
    # 不可变不行　
    while True:
        msg, addr = s.recvfrom(1024)
        msgList = msg.decode().split(' ')
        if msgList[0] == 'L':
            # 调用新的函数　进行是否是新用户　或者是旧的函数
            do_login(s, user, msgList[1], addr)
        elif msgList[0] == 'C':
            # 转发给所有人
            do_chat(s, user, msgList[1], ' '.join(msgList[2:]))
        elif msgList[0] == 'Q':
            do_quit(s, user, msgList[1])

# 做管理员喊话  子进程向父进程发消息 因为这是服务器端的ADDR


def do_child(s, ADDR):
    while True:
        msg = input('管理员消息')
        msg = 'C 管理员　' + msg
        s.sendto(msg.encode(), ADDR)

# 创建网络，创建进程，调用功能函数　


def main():
    # server address
    ADDR = ('0.0.0.0', 8888)
    # 创建套接字
    s = socket(AF_INET, SOCK_DGRAM)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(ADDR)

    # 创建一个单独的进程处理管理员喊话功能

    pid = os.fork()
    if pid < 0:
        sys.exit('创建进程失败')
    elif pid == 0:
        do_child(s, ADDR)
    else:
        do_parent(s)


if __name__ == '__main__':
    main()
