import tkinter
win = tkinter.Tk()
win.title('qjy')
win.geometry('400x400')
def func():
    print('qjy is a good man')

#text 是按钮里面的文字　command是绑定一个函数
button = tkinter.Button(win,text='按钮',command=func)
button.pack()
#添加匿名函数
button2 = tkinter.Button(win,text='按钮',
    command=lambda:print('666'),
    width=5,height=2)
button2.pack()
#直接退出
button3 = tkinter.Button(win,text='按钮',
    command=win.quit,
    width=5,height=2)
button3.pack()




win.mainloop()