from flask import Flask, render_template

app = Flask(__name__)

class Person(object):
    name = None
    def say(self):
        return 'qjy is a good man'

#将templates01.html文件渲染成字符串再响应给客户端　
@app.route('/t')
def template():
    # 将templates01.html渲染成字符串
    # a1 = input('歌名')
    # a2 = input('作词')
    # a3 = input('作曲')
    # a4 = input('演唱')
    # return render_template('templates01.html',name1=a1,name2=a2,name3=a3,name4=a4)


    # dic = {
    #     'music':'绿光',
    #     'author':'宝强',
    #     'qu':'乃亮',
    #     'singer':'羽凡'
    # }

    # locals(): 将当前函数内所有的局部变量封装成一个字典　

    music='绿光'
    author='宝强'
    qu='乃亮'
    singer='羽凡'

# locals()把局部变量用键值对的方式组合起来，这是一个拷贝，对其进行操作不会影响到内存空间内的值
    return render_template('templates01.html',params=locals())


#演示能够传递到模板中作为变量的数据类型都有哪些
@app.route('/var')
def var():
    bookName = '钢铁是怎样炼成的'
    author = '奥斯特洛夫斯基'
    price = 32.5
    list = ['罗琳','鸣人','卡卡西','自来也','佐助']
    tup = ('水浒传','三国演义','红楼梦','西游记')
    dic = {
        'WMZ':'老魏',
        'WWC':'隔壁老王',
        'LZ':'吕泽',
        'MM':'蒙蒙'
            }
    person = Person()
    person.name = '狮王.金毛'
    print((locals()))
    return  render_template('02var.html', params = locals())


if __name__ == '__main__':
    app.run(debug=True,port=8888)