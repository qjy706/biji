'''此模块用于定义一个学生类，此类用于生成学生对象，来存储
学生相关信息'''
from s import Student
class Student:
    def __init__(self,n,a,s=0):
        self.name=n
        self.age=a
        self.score=s
    def get_info(self):
        '''此方法用来返回学生信息对象'''
        return (self.name,self.age,self.score)
        
    def get_score(self):
        return self.score

    def get_age(self):
        return self.age