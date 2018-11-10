from flask import render_template
#导入蓝图程序main 用于构建路由
from . import main


#导入dv以及models们
from .. import db
from ..models import *






#首页的访问路由
@main.route('/')
def index_views():
    categories = Category.query.all()
    print(categories)
    return 'hellp world'


@main.route('/01')
def htmL():
    return render_template('index.html')
