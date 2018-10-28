import tkinter as tk 
#想写一个界面　要先有一个窗口　
#创建窗口　
win = tk.Tk()
#设置标题
win.title('qjy')
#设置大小和位置
win.geometry('600x600+200+20')


#进入消息循环

#标签控件
'''label :标签控件　，可以显示文本'''
'''label 窗体显示在什么根窗口下
text 显示的文本内容
bg 颜色
fg 字体颜色
font 元组　选择字体
width 宽度
height 高度
wraplength 制定text多宽之后换行
justify　　设置换行后的对齐方式　
anchor 位置 n 北　　s 南　　w 西　e 东  可以组合　东南　东北这样的'''
label = tk.Label(win,text='qjy is a good man',
                 bg='pink',fg='red',font=('黑体',20)
                 ,width = 10,height = 4,wraplength=100,
                 justify='left',anchor='e')

'''讲label挂在win上　固定'''
label.pack()












win.mainloop()