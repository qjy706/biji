import tkinter as tk
from tkinter import messagebox
#想写一个界面　要先有一个窗口　
#创建窗口　
win = tk.Tk()
#设置标题
win.title('qjy')
#设置大小和位置
win.geometry('600x600+200+20')

def func():
    tk.messagebox.showinfo(title='Python tkinter',
        message='登录成功！')

#创建按钮
button = tk.Button(win,text = '按钮',command = func,width=5,
    height=2)
#固定按钮
button.pack()
#添加匿名函数
button2 = tk.Button(win,text = '按钮',command = lambda:print
    ('qjy is good man'),width=5,height=2)

button2.pack()

button3 = tk.Button(win,text = '退出',command = win.quit,width=5,height=2)

button3.pack()

windows.destroy()






win.mainloop()