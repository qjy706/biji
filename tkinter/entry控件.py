import tkinter
win = tkinter.Tk()
win.title('qjy')
win.geometry('400x400')

'''输入框架
用于显示简单的文本内容
输入密码可以用 show = '*'　匿文显示
如果想把输入的值拿出来　需要设定一个变量
'''
#创建变量
e = tkinter.Variable()
def func():
    print(e.get())
#e就代表输入的输入的对象
entry = tkinter.Entry(win,show='*',textvariable=e)
entry.pack()

#设置值
e.set('qjy is a good man')
#取值　
print(e.get())
print(entry.get())
#使用按钮输出输入框架内的内容 
def func():
    print(e.get())
button = tkinter.Button(win,text='按钮',command=func)
button.pack()


win.mainloop()