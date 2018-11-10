#main目录 包含主要业务逻辑的路由和视图
from flask import Blueprint
users = Blueprint('users',__name__)

#关联操作  可以用views里面的方法了
from . import views