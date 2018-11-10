from flask import  Flask,render_template,url_for,request

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form['username']
        password=   request.form['password']
        source_url= request.form['source_url']
        return '用户名:{},密码:{}'.format(username,password)

if __name__ == '__main__':
    app.run(debug=True,port='8888')