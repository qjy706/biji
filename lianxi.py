class Mylist(object):
    def __init__(self,iterable=()):
        self.data = [x for x in iterable]

    def __repr__(self):
        return '%s'%self.data

    def __iter__(self):
        return iter(self.data)

    def __next__(self):
        for x in self.data:
            return x

a=Mylist([1,2,3,4,5])

it=iter(a)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))


class MyList():
    '''这是一个自定义的列表类型，
    此类型的对象用data属性绑定的列表来存储数据'''
    def __init__(self,iterable=()):
        self.data=[x for x in iterable]


    def __repr__(self):
        return 'MyList(%s)' % self.data
    def __iter__(self):
        print('__iter__被调用')
        return MyListIterator(self.data)

class MyListIterator():
    def __init__(self,lst):
        self.data_list = lst
        self.cur_index = 0
    def __next__(self):
        print('__next__方法被调用')
        if self.cur_index >= len(self.data_list):
            raise StopIteration
        r=self.data_list[self.cur_index]
        self.cur_index += 1
        return r
myl=MyList([2,3,5,7])
it=iter(myl)
print(next(it))
print(next(it))
print(next(it))


for x in myl:
    print(x)
