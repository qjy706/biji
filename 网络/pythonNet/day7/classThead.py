from threading import Thread
from time import ctime,sleep


class MyThread(Thread):
    def __init__(self,target,name='tedu',args=(),kwargs={}):
        super(self.__class__,self).__init__()

        self.target=target
        self.name=name
        self.args=args
        self.kwargs=kwargs



    def run(self):
        self.target(*self.args,**self.kwargs)


def player(song,sec):
    for i in range(2):
        print('playing %s:%s'%(song,ctime()))
        sleep(2)

t=MyThread(target=player,args=('凉凉',2))
t.start()
t.join()