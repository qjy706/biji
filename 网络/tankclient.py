from socket import *
import os 
import sys
import tkinter as tk
import traceback
from threading import *
# 发
# 　　　登录信息　注册信息　坦克选择信息　
# 　　键盘绑定信息　＊

# 收　　服务器命令　八个套接字　
# 　　　　接收图片




def client():
    pass

def picture():
    pass



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
        choice()
    if data == 'Flase':
        is_signup=tk.messagebox.askyesno('欢迎','您还没有注册，是否现在注册')
        if is_signup:
            rigister()



def rigister():
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

def sendinfo():
    s.send('1'.encode())

def choice():
    window = tk.Tk()
    window.geometry('600x600')
    window.title('注册')

    b = tk.Button(window, text='坦克１',width=15, height=2,command=sendinfo)     # 点击按钮执行的命令
    b.pack()

    b = tk.Button(window, text='坦克２',width=15, height=2,command=sendinfo)     # 点击按钮执行的命令
    b.pack() 

    b = tk.Button(window, text='坦克３',width=15, height=2,command=sendinfo)     # 点击按钮执行的命令
    b.pack() 

    b = tk.Button(window, text='坦克４',width=15, height=2,command=sendinfo)     # 点击按钮执行的命令
    b.pack() 
    window.mainloop()

def quit():
    data = 'Q'
    s.send(data.encode())
    windows.destroy()

def myfun1(event):
    print('捕捉到',event.char)
def myfun2(event):
     windows.destroy()









def main():
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

    bt_login=tk.Button(window,text='登录',command=login)
    bt_login.place(x=140,y=230)
    bt_logup=tk.Button(window,text='注册',command=rigister)
    bt_logup.place(x=210,y=230)
    bt_logquit=tk.Button(window,text='退出',command=quit)
    bt_logquit.place(x=280,y=230)

    window.mainloop()



if __name__ == '__main__':
    # HOST = ''
    # PORT = 8000
    # ADDR = (HOST,PORT)
    # s = socket()
    # s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    # try:
    #     s.connect(ADDR)
    # except:
    #     print('连接服务器失败')
    # else:
    #     main()
    main()


# def hit_me():
#     import sys
#     import os
#     windows = tk.Tk()#主窗口
#     windows.title('坦克大战')#窗口标题
#     windows.geometry('600x600')#窗口尺寸

#     b = tk.Label(windows,text='玩耍',bg='red')

#     b.bind('<a>',myfun1)
#     b.bind('<w>',myfun1)
#     b.bind('<s>',myfun1)
#     b.bind('<d>',myfun1)
#     b.bind('<q>',myfun2)
#     b.focus_set()#键盘事件绑定到键盘焦点
#     b.pack()
#     windows.mainloop()


#     window = tk.Tk()
#     window.title('Tanks')
#     window.geometry('400x400')

#     l = tk.Label(window, 
#         text='坦克大战页面',
#         bg='green',
#         font=('Arial', 12),
#         width=15, height=2
#         )
#     l.pack()

#     on_hit = False  # 默认初始状态为 False