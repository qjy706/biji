from flask import Flask,url_for,render_template,request

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('test.html')
    else:
        print(request.path)
        print(request.form)
        uname = request.form['uname']
        upwd = request.form['upwd']
        return render_template('muban.html',params=locals())



if __name__ == '__main__':
    app.run(debug=True)