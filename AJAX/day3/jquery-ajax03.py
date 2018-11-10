from flask import Flask,render_template,request,make_response
from flask_sqlalchemy import SQLAlchemy
import pymysql
import json

app = Flask(__name__)



@app.route('/02-server')
def server02():
    return '帅'
@app.route('/07-crossdomain')
def cross():
    return "alert('这是/07-crossdomain的访问路径')"


if __name__ == '__main__':
    app.run(debug=True)