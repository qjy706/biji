# from tkinter import *
# import sys
# windows = Tk()#主窗口
# windows.title('坦克大战')#窗口标题
# windows.geometry('600x600+200+20')#窗口尺寸

# def myfun1(event):
#     print('捕捉到',event.char)
# def myfun2(event):
#     sys,exit('退出')


# b = Label(windows,text='我最帅',bg='red')

# p=b.bind('<a>',myfun1)
# b.bind('<w>',myfun1)
# b.bind('<s>',myfun1)
# b.bind('<d>',myfun1)
# b.bind('<q>',myfun2)

# print(p)
# b.focus_set()

# b.pack()#用于自动调节尺寸 #将text标签添加到主窗口

# windows.mainloop()#主事件循环

# 发
# 　　　def 登录信息　def 注册信息　def 坦克选择信息　
# 　　键盘绑定信息　＊

# 收　　服务器命令　八个套接字　
# 　　　　def 接收图片


#! /usr/bin/env python#! encoding:utf-8
# Filename:test.py
# from tkinter import *
# root = Tk()
# root.title("Entry Test")
# v1 = StringVar()
# v2 = StringVar()
# v3 = StringVar()
# #设置entry为只读属性
# Entry(root, width=30,textvariable=v1, stat="readonly").pack()
# v1.set("readonly")
# #默认情况下下Entry的状态为normal
# Entry(root, width=30,textvariable=v2).pack()
# v2.set("normal")
# #将输入的内容用密文的形式显示
# entry = Entry(root, width=30,textvariable=v3)
# v3.set("password")
# entry.pack()
# entry["show"] = "*"
# root.mainloop()

# from tkinter import *

# top=Tk()
# top.wm_title('python test')
# top.geometry('500x600+0+0')
# name=StringVar()
# Entry(top,textvariable=name,show='.').pack()
# print(name.get()) 


# from tkinter import *


# def main():
#     # 这个函数要写在前面
#     # 如果要是写在所有代码的后面，找不到的
#     def _change_content():
#         var.set('甘薯')

#     root = Tk()

#     # 两个框架
#     frame1 = Frame(root)
#     frame2 = Frame(root)

#     # Label显示的文字要是会变化的话，只接受这种类型的变量
#     var = StringVar()
#     var.set("紫菜")

#     text_label = Label(frame1,
#                        textvariable=var,
#                        justify=LEFT
#                        )
#     text_label.pack()

#     the_button = Button(frame2,
#                         text='下一句',
#                         command=_change_content  # 点击时调用的函数
#                         )
#     the_button.pack()

#     # 可以把这两个调换一下位置，2先1后。
#     frame1.pack(padx=20, pady=20)
#     frame2.pack(padx=40, pady=40)

#     mainloop()


# if __name__ == '__main__':
#     main()


# import tkinter
# import tkinter.messagebox

# #创建应用程序窗口
# root = tkinter.Tk()
# varName = tkinter.StringVar()
# varName.set('')
# varPwd = tkinter.StringVar()
# varPwd.set('')
# #创建标签
# labelName = tkinter.Label(root, text='用户名:', justify=tkinter.RIGHT, width=80)
# #将标签放到窗口上
# labelName.place(x=10, y=5, width=80, height=20)
# #创建文本框，同时设置关联的变量
# entryName = tkinter.Entry(root, width=80,textvariable=varName)
# entryName.place(x=100, y=5, width=80, height=20)

# labelPwd = tkinter.Label(root, text='密  码:', justify=tkinter.RIGHT, width=80)
# labelPwd.place(x=10, y=30, width=80, height=20)
# #创建密码文本框
# entryPwd = tkinter.Entry(root, show='*',width=80, textvariable=varPwd)
# entryPwd.place(x=100, y=30, width=80, height=20)
# #登录按钮事件处理函数
# def login():
# #获取用户名和密码
#     name = entryName.get()
#     pwd = entryPwd.get()
#     if name == 'admin'and pwd == '123456':
#         tkinter.messagebox.showinfo(title='Python tkinter',message='登录成功！')
#     else:
#         tkinter.messagebox.showerror('Python tkinter', message='登录失败')
# #创建按钮组件，同时设置按钮事件处理函数
# buttonOk = tkinter.Button(root, text='登录', command=login)
# buttonOk.place(x=30, y=70, width=50, height=20)
#     #取消按钮的事件处理函数
# def cancel():
# #清空用户输入的用户名和密码
#     varName.set('')
#     varPwd.set('')
# buttonCancel = tkinter.Button(root, text='取消', command=cancel)
# buttonCancel.place(x=90, y=70, width=50, height=20)

# #启动消息循环
# root.mainloop()


# -*- coding: utf-8 -*-
"""
Created on Sun Aug  5 10:34:10 2018

@author: Administrator
"""
import tkinter as tk
import tkinter.messagebox

#窗口
window=tk.Tk()
window.title('坦克大战登录界面')
window.geometry('450x300')
#画布放置图片

#标签 用户名密码
tk.Label(window,text='用户名:').place(x=100,y=150)
tk.Label(window,text='密码:').place(x=100,y=190)
#用户名输入框
name=tk.StringVar()
entry_usr_name=tk.Entry(window,textvariable=name)
entry_usr_name.place(x=160,y=150)
#密码输入框
pwd=tk.StringVar()
password=tk.Entry(window,textvariable=pwd,show='*')
password.place(x=160,y=190)

#登录函数
def login():
    #输入框获取用户名密码
    username=name.get()
    userpassword=pwd.get()
    global s
    user = 'L '
    user = user + username + ' ' + userpassword
    s.send(user.encode())
    data = s.recv(1024).decode()
    if data == 'ok':
        tk.messagebox.showinfo(title='welcome',message='欢迎您：'+username)
    if data == 'Flase':
        is_signup=tk.messagebox.askyesno('欢迎','您还没有注册，是否现在注册')
        if is_signup:
            rigister()

#注册函数
def rigister():
    #确认注册时的相应函数
    global s
    def fun1():
        #获取输入框内的内容
        newname=new_name.get()
        np=new_pwd.get()
        npf=new_pwd2.get()
        if np != npf:
            tk.messagebox.showerror('错误','密码前后不一致')
        elif np =='' or newname=='':
            tk.messagebox.showerror('错误','用户名或密码为空')
        newinfo = 'R '
        newinfo = newinfo + newname + ' ' + np
        s.send(newinfo.encode())
        data = s.recv(1024).decode()
        if data == 'ok':
            tk.messagebox.showinfo('欢迎','注册成功')
            window2.destroy()
        else:
            tk.messagebox.showinfo('注册失败')
    #新建注册界面
    window2=tk.Toplevel(window)
    window2.geometry('350x200')
    window2.title('注册')
    #用户名变量及标签、输入框
    new_name=tk.StringVar()
    tk.Label(window2,text='用户名：').place(x=10,y=10)
    tk.Entry(window2,textvariable=new_name).place(x=150,y=10)
    #密码变量及标签、输入框
    new_pwd=tk.StringVar()
    tk.Label(window2,text='请输入密码：').place(x=10,y=50)
    tk.Entry(window2,textvariable=new_pwd,show='*').place(x=150,y=50)    
    #重复密码变量及标签、输入框
    new_pwd2=tk.StringVar()
    tk.Label(window2,text='请再次输入密码：').place(x=10,y=90)
    tk.Entry(window2,textvariable=new_pwd2,show='*').place(x=150,y=90)    
    #确认注册按钮及位置
    bt_confirm_sign_up=tk.Button(window2,text='确认注册',
                                 command=fun1)
    bt_confirm_sign_up.place(x=150,y=130)
#退出的函数
def quit():
    window.destroy()
#登录 注册按钮
bt_login=tk.Button(window,text='登录',command=login)
bt_login.place(x=140,y=230)
bt_logup=tk.Button(window,text='注册',command=rigister)
bt_logup.place(x=210,y=230)
bt_logquit=tk.Button(window,text='退出',command=quit)
bt_logquit.place(x=280,y=230)
#主循环
window.mainloop()