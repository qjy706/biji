from flask import Flask

app = Flask(__name__)

@app.route('/'):

@app.route('/url')
def url():
    url_index = url_for('index')
    print('index():'+url_index)
    # 通过shouw(name)解析出对应的访问路径
    url_show = url_for('show',name='wangwc')
    print('show(name):'+url_show)
    return '反向地址生成成功'



if __name__  == '__main__':
    app.run(debug=True)