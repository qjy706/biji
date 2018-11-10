from flask import Flask,render_template,request,make_response
from flask_sqlalchemy import SQLAlchemy
import pymysql
import json
pymysql.install_as_MySQLdb()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']="mysql://root:123456@localhost:3306/ajax"
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True

db=SQLAlchemy(app)


class Province(db.Model):
    __tablename__ = 'province'
    id = db.Column(db.Integer,primary_key=True)
    proName = db.Column(db.String(30),nullable=False)
    cities = db.relationship('City',backref='province',lazy='dynamic')

    def to_dict(self):
        dic={
            'id':self.id,
            'proName':self.proName
        }
        return dic


class City(db.Model):
    __tablename__ = 'city'
    id = db.Column(db.Integer,primary_key=True)
    cityName = db.Column(db.String(30))
    pid = db.Column(db.Integer,db.ForeignKey('province.id'))

    def to_dict(self):
        dic = {
            'id':self.id,
            'cityName':self.cityName,
            'pid':self.pid
        }
        return dic

db.create_all()


@app.route('/01-province')
def province():
    # 返回所有省份所组成的json串
    provinces = Province.query.all()
    print(provinces)
    list = []
    for pro in provinces:
        list.append(pro.to_dict())
    return json.dumps(list)


@app.route('/01-city')
def city():
    pid = request.args.get('pid')
    cities = City.query.filter_by(pid=pid).all()
    list =[]
    for c in cities:
        list.append(c.to_dict())
    return json.dumps(list)

# $.get
@app.route('/03-jq-get')
def jq_get():
    provinces = Province.query.all()
    list = []
    for pro in provinces:
        list.append(pro.to_dict())
    return json.dumps(list)







if __name__ == '__main__':
    app.run(debug=True)