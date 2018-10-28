import tkinter
win = tkinter.Tk()
win.title('qjy')
win.geometry('400x400')

check1 = tkinter.Checkbutton(win,text = 'money')
check1.pack()
check2 = tkinter.Checkbutton(win,text = 'power')
check2.pack()
check3 = tkinter.Checkbutton(win,text = 'women')
check3.pack()

win.mainloop()