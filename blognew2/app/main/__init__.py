#main目录 包含主要业务逻辑的路由和视图
from flask import Blueprint
main = Blueprint('main',__name__)


#当前目录views
from . import views