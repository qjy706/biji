import tkinter
win = tkinter.Tk()
win.title('qjy')
win.geometry('400x400')

#单选框变量绑定一样的变量,用以区分
r=tkinter.Variable()
e=tkinter.IntVar()
def updata():
    print(r.get())
#一组单选框要绑定同一个变量，
radio1 = tkinter.Radiobutton(win,text='one',value='good'
    ,variable=r,command=updata)
radio1.pack()

radio2 = tkinter.Radiobutton(win,text='one',value=20
    ,variable=r,command=updata)
radio2.pack()

win.mainloop()