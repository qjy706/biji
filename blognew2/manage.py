#启动程序
from app import create_app
#init.py系统会自动寻找里面的程序

app = create_app()









if __name__ == '__main__':
    app.run()