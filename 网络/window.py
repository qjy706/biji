

# windows = Tk()
# windows.title('我是最帅的')
# windows.geometry('600x600')


# windows.mainloop()

import tkinter as tk        #导入tkinter模块
import sys
import os

window = tk.Tk()            #主窗口
window.title('my window')   #窗口标题
window.geometry('400x400')  #窗口尺寸

### 这里是窗口的内容###




l = tk.Label(window, 
    text='OMG! this is TK!',    # 标签的文字
    bg='green',                 # 背景颜色
    font=('Arial', 12),         # 字体和字体大小
    width=15, height=2          # 标签长宽
    )
l.pack()    # 固定窗口位置


# 如果我们需要通过变量的形式控制Label的显示，那么需要用到var变量，如下：

var = tk.StringVar()    # 文字变量储存器
var.set('OMG! This is TK!')
l = tk.Label(window, 
    textvariable=var,   # 使用 textvariable 替换 text, 因为这个是可以变化的
    bg='green', font=('Arial', 12), width=15, height=2)
l.pack() 

# 上述的var变量值可以通过编写条件控制语句等进行更改，实现某种功能。

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



    b = tk.Label(windows,text='我最帅',bg='red')

    p=b.bind('<a>',myfun1)
    b.bind('<w>',myfun1)
    b.bind('<s>',myfun1)
    b.bind('<d>',myfun1)
    b.bind('<q>',myfun2)

    print(p)
    b.focus_set()#键盘事件绑定到键盘焦点

    b.pack()#用于自动调节尺寸 #将text标签添加到主窗口

    windows.mainloop()#主事件循环
# tk.Button 按钮
b = tk.Button(window, text='hit me',width=15, height=2,command=hit_me)     # 点击按钮执行的命令
b.pack()                # 按钮位置


window.mainloop()           #循环消息，让窗口活起来