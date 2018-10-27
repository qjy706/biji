class A:
    def go(self):
        print('A')

class B(A):
    def go(self):
        print('B')
        super(B,self).go()
class C(A):
    def go(self):
        print('C')
        super(C,self).go()
class D(B,C):
    def go(self):
        print('D')
        super(D,self).go()
d=D()
print(D.__mro__,end='\n')
d.go()

class MyList():
    '''这是一个自定义的列表类型，
    此类型的对象用data属性绑定的列表来存储数据'''
    def __init__(self,iterable=()):
        self.data=[x for x in iterable]


    def __repr__(self):
        return 'MyList(%s)' % self.data

    # def __str__(self):
    #     return 'MyList(%s)' % self.data

    def __len__(self):
        return len(self.data)

    # def __bool__(self):
    #     print('__bool__方法被调用')
    #     for x in self.data:
    #         if x:
    #             return True
    #         return False
    #         return any(self.data)

load data infile '/var/lib/mysql-files/'
into table t1 
fields terminated by ','
lines terminated by '\n';


 create table t1(id int primary key auto_increment,
 name varchar(15),
 score float(5,2),
 phnumber char(11),
 class char(7));

show variables like 'secure_file_priv';



create table passwd(用户名 char(50),密码 varchar(50),UID int,
GID int,
描述 varchar(50),
主目录 varchar(50),
登录权限 varchar(50));


alter table passwd add id int(3) zerofill primary key auto_increment



select * from passwd
into outfile '/var/lib/mysql-files/xxx'
fields terminated by ':'
lines terminated by '\n';




a=sum(map(lambda x: x,range(101)))
print(a)

def mysum(n):
    return n

a=sum(map(mysum,range(101)))
print(a)


def mysum(x):
    if x == 0:
        return 0
    return x+mysum(x-1)
print(mysum(100))


def myfac(n):
    s=1
    for x in range(1,n+1):
        s *= x 
    return s 
print(myfac(5))


def myfac(n):
    for x in range(1,n+1):
        x += x**x
    return x
print(myfac(5))

