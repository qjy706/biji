import tkinter as tk        #导入tkinter模块
import sys
import os

window = tk.Tk()
window.title('Tanks')
window.geometry('400x400')

l = tk.Label(window, 
    text='坦克大战页面',
    bg='green',
    font=('Arial', 12),
    width=15, height=2
    )
l.pack()

def myfun1(event):
    print('捕捉到',event.char)
def myfun2(event):
    os._exit(0)

on_hit = False  # 默认初始状态为 False
def hit_me():
    import sys
    import os
    windows = tk.Tk()#主窗口
    windows.title('坦克大战')#窗口标题
    windows.geometry('600x600')#窗口尺寸



    b = tk.Label(windows,text='玩耍',bg='red')

    p=b.bind('<a>',myfun1)
    b.bind('<w>',myfun1)
    b.bind('<s>',myfun1)
    b.bind('<d>',myfun1)
    b.bind('<q>',myfun2)
    print(p)
    b.focus_set()#键盘事件绑定到键盘焦点
    b.pack()
    windows.mainloop()

    
# tk.Button 按钮
b = tk.Button(window, 
    text='登录',      # 显示按钮上的文字
    width=15, height=2, 
    command=hit_me)     # 点击按钮执行的命令
b.pack()                # 按钮位置

c = tk.Button(window, 
    text='注册',
    width=15, height=2, 
    command=hit_me)
c.pack()

d = tk.Button(window, 
    text='选择',
    width=15, height=2, 
    command=hit_me)
d.pack()

window.mainloop()