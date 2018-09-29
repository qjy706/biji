import pygame,sys,time
from random import randint
from pygame.locals import *

#主界面对象的显示
class TankMain(object):
    """坦克大战的主窗口"""
    width=800
    height=700
    my_tank_missile_list = []
    my_tank =None
    wall=None
    enemy_list =pygame.sprite.Group()#敌方坦克组
    explode_lsit=[]
    enemy_missile_list=pygame.sprite.Group()
          #开始游戏的方法
    def startGame(self):
        pygame.init()#pygame模块初始化，加载系统资源
        screem=pygame.display.set_mode((TankMain.width,TankMain.height),0,32)
          #给窗口设置一个标题
        pygame.display.set_caption("坦克大战")
        #创建墙
        TankMain.wall=Wall(screem,80,150,50,200)
        TankMain.my_tank = My_Tank(screem)
        if len(TankMain.enemy_list)==0:
            for i in range(1,6):#游戏开始的时候，初始化5个敌方坦克
                TankMain.enemy_list.add(Enemy_Tank(screem))#把敌方坦克放到组里面

        while True:
            if len(TankMain.enemy_list) < 5:
                TankMain.enemy_list.add(Enemy_Tank(screem))
        #color RGB(0,100,200),(0,0,0)黑色 (255.255.255)白色
        #设置窗口的背景色为黑色。
            screem.fill((0,0,0))
            #显示左上角的文字
            for i,text in enumerate(self.write_text(),0):
                screem.blit(text,(0,5+(15*i)))
            #显示游戏中的墙,并且对其他对象进行检测
            TankMain.wall.display()

            self.get_event(TankMain.my_tank,screem)#获取事件，根据或许的事件去处理。
            if TankMain.my_tank:
                TankMain.my_tank.hit_enemy_missile()
            if TankMain.my_tank and TankMain.my_tank.live:
                TankMain.my_tank.display()#屏幕上显示我方坦克
                TankMain.my_tank.move()#我方坦克移动
            else:
                TankMain.my_tank=None



            for enemy in TankMain.enemy_list:
                enemy.display()#显示敌方坦克。
                enemy.random_move()#敌方坦克移动
                enemy.random_fire()
            #显示所有的我方炮弹
            for m in TankMain.my_tank_missile_list:
                if m.live:
                    m.display()
                    m.hit_tank()#炮弹是否击中敌方坦克
                    m.move()
                else:
                    TankMain.my_tank_missile_list.remove(m)

            #显示敌方所有炮弹
            for m in TankMain.enemy_missile_list:
                if m.live:
                    m.display()
                    m.move()
                else:
                    TankMain.enemy_missile_list.remove(m)
            #显示爆炸效果
            for explode in TankMain.explode_lsit:
                explode.display()


            # 显示重置.
            time.sleep(0.01)
            pygame.display.update()
    #获取所有的事件，（敲击键盘）
    def get_event(self,my_tank,screem):
        for event in pygame.event.get():

            if event.type == QUIT:
                self.stopGame()#程序退出
            if event.type == KEYDOWN and not my_tank and event.key==K_F1:
                TankMain.my_tank = My_Tank(screem)
            if event.type == KEYDOWN and my_tank:
                if event.key ==K_LEFT or event.key==K_a:
                    my_tank.direction="L"
                    my_tank.stop=False
                    #my_tank.move()
                if event.key ==K_RIGHT:
                    my_tank.direction="R"
                    my_tank.stop = False
                    #my_tank.move()
                if event.key ==K_UP:
                    my_tank.direction = "U"
                    my_tank.stop = False
                    #my_tank.move()
                if event.key ==K_DOWN:
                    my_tank.direction = "D"
                    my_tank.stop = False
                    #my_tank.move()
                if event.key ==K_ESCAPE:#敲击键盘esc件，程序退出
                    self.stopGame()
                if event.key == K_x:
                    m= my_tank.fire()
                    m.good=True#我方坦克发射的炮弹
                    TankMain.my_tank_missile_list.append(m)
            if event.type ==KEYUP and my_tank:
                if event.key==K_LEFT or event.key==K_RIGHT or event.key==K_UP or event.key==K_DOWN:
                    my_tank.stop=True
    #关闭游戏的方法
    def stopGame(self):
        sys.exit()

    def write_text(self):

        font = pygame.font.SysFont("simsunnsimsun",12)#定义一个字体
        text_sf1=font.render("敌方坦克数量为:%d"%len(TankMain.enemy_list),True,(255,0,0))#根>据字体创建一个文字的图像。
        text_sf2=font.render("我方炮弹的数量:%d"%len(TankMain.my_tank_missile_list),True,(255, 0, 0))

        return text_sf1,text_sf2
    #坦克大战游戏中所有对象的类。

class BaseTtem(pygame.sprite.Sprite):
    def __init__(self,screem):
        pygame.sprite.Sprite.__init__(self)
        #所有对象共享的属性
        self.screem=screem
    #在游戏中显示当前对象。
    def display(self):
        if self.live:
            self.image = self.images[self.direction]
            self.screem.blit(self.image,self.rect)

#坦克的公共父类
class Tank(BaseTtem):
    #定义类属性，所有坦克的高和宽是一样的
    width=50
    height=50
    def __init__(self,screem,left,top):
        super().__init__(screem)
        self.screem=screem
        self.direction="U"#坦克的默认方向向下
        self.speed=5#坦克移动的速度
        self.stop=False
        self.images={}#坦克的所有图片，key为方向，value为图片
        self.images["L"]=pygame.image.load("images/tankL.jpg")
        self.images["R"]=pygame.image.load("images/tankR.jpg")
        self.images["U"]=pygame.image.load("images/tankU.jpg")
        self.images["D"]=pygame.image.load("images/tankD.jpg")
        self.image=self.images[self.direction]#坦克的图片由方向决定
        self.rect=self.image.get_rect()
        self.rect.left=left
        self.rect.top=top
        self.live=True#决定坦克是否死亡

    # 坦克移动方法
    def move (self):
        if not self.stop:#如果坦克不是停止状态
            if self.direction=="L":
                if self.rect.left>0:#判断坦克是否还能移动
                    self.rect.left-=self.speed
                else:
                    self.rect.left=0
            elif self.direction=="R":
                if self.rect.right < TankMain.width:
                    self.rect.right+=self.speed
                else:
                    self.rect.right=TankMain.width


            elif self.direction=="D":
                if self.rect.bottom < TankMain.height:
                    self.rect.top+=self.speed
                else:
                    self.rect.bottom=TankMain.height
            elif self.direction=="U":
                if self.rect.top > 0:
                    self.rect.top-=self.speed
                else:
                    self.rect.top = 0

    def fire(self):
        m = Missile(self.screem,self)
        return m

#我方坦克
class My_Tank(Tank):
    def __init__(self,screem):
        super().__init__(screem,280,450)#创建一个我方坦克
        self.stop=True
        self.live=True
    def hit_enemy_missile(self):
        hit_list=pygame.sprite.spritecollide(self,TankMain.enemy_missile_list,False)
        for m in hit_list:#我方坦克被击中
            m.live=False
            TankMain.enemy_missile_list.remove(m)
            self.live=False
            exploed =Explode(self.screem,self.rect)
            TankMain.explode_lsit.append(exploed)

#敌方坦克
class Enemy_Tank(Tank):

    def __init__(self,screem):
        super().__init__(screem,randint(1,5)*100,200)
        self.speed=2
        self.step=10  # 坦克按照某个方向连续移动的步数
        self.get_random_direction()


    def get_random_direction(self):
        r = randint(0,4)  # 得到一个坦克移动方向和停止的随机数
        if r == 4 :
            self.stop=True
        elif r ==1:
            self.direction="L"
            self.stop=False
        elif r ==2:
            self.direction="R"
            self.stop = False
        elif r ==0:
            self.direction="D"
            self.stop = False
        elif r ==3:
            self.direction="U"
            self.stop = False

    #敌方坦克，按照一个随机的方向，连续移动6步，然后再次改变方向。
    def random_move(self):
        if self.live:
            if self.step==0:
                self.get_random_direction()
                self.step=6
            else:
                self.move()
                self.step-=1

    def random_fire(self):
        r =randint(0,50)
        if r==20: #or r == 20 or r==30 or r==40:
            m=self.fire()
            TankMain.enemy_missile_list.add(m)
        else:
            return
#我方炮弹
class Missile(BaseTtem):
    width = 12
    height = 12
    def __init__(self,screem,tank):
        super().__init__(screem)
        self.tank=tank
        self.direction = tank.direction #炮弹的方向有所发射的坦克决定
        self.speed = 12 #炮弹的速度
        self.images = {}  # 炮弹的所有图片，key为方向，value为图片
        self.images["L"] = pygame.image.load("images/tankL.jpg")
        self.images["R"] = pygame.image.load("images/tankR.jpg")
        self.images["U"] = pygame.image.load("images/tankU.jpg")
        self.images["D"] = pygame.image.load("images/tankD.jpg")
        self.image = self.images[self.direction]  # 炮弹的图片由方向决定
        self.rect = self.image.get_rect()
        self.rect.left = tank.rect.left + (tank.width - self.width) /2
        self.rect.top = tank.rect.top + (tank.height - self.height) /2
        self.live = True #炮弹是否消灭了
        self.good=False

    def move(self):
        if self.live:#如果炮弹还存在
            if self.direction=="L":
                if self.rect.left>0:#判断坦克是否还能移动
                    self.rect.left-=self.speed
                else:
                    self.live=False
            elif self.direction=="R":
                if self.rect.right < TankMain.width:
                    self.rect.right+=self.speed
                else:
                    self.live = False


            elif self.direction=="D":
                if self.rect.bottom < TankMain.height:
                    self.rect.top+=self.speed
                else:
                    self.live = False
            elif self.direction=="U":
                if self.rect.top > 0:
                    self.rect.top-=self.speed
                else:
                    self.live = False
    #炮弹击中坦克,第一种我方炮弹击中敌方坦克，敌方炮弹击中我方坦克
    def hit_tank(self):
        if self.good:#如果炮弹是我方的炮弹
            hit_list=pygame.sprite.spritecollide(self,TankMain.enemy_list,False)
            for e in hit_list:
                e.live=False
                TankMain.enemy_list.remove(e)#如果敌方坦克被击中，则从列表中删除敌方坦克
                self.live=False
                explode= Explode(self.screem,e.rect)#产生一个爆炸对象
                TankMain.explode_lsit.append(explode)

#爆炸类
class Explode(BaseTtem):

    def __init__(self,screen,rect):
        super().__init__(screen)
        self.live=True
        self.images=[pygame.image.load("images/explode.jpg"),\
                     pygame.image.load("images/explode.jpg"), \
                     pygame.image.load("images/explode.jpg"), \
                     pygame.image.load("images/explode.jpg"), \
                     pygame.image.load("images/explode.jpg"),\
                     pygame.image.load("images/explode.jpg")]

        self.step=0
        self.rect=rect#爆炸的位置和发生爆炸前，炮弹碰到的坦克位置一样。在构建爆炸的时候，把坦克的rect作为参数传进来
    #display方法在整个游戏运行过程中，循环调用，每次一定时间调用一次
    def display(self):
        if self.live:
            if self.step==len(self.images):#最后一张爆炸图片已经显示
                self.live=False
            else:
                self.image=self.images[self.step]
                self.screem.blit(self.image,self.rect)
                self.step+=1
        else:
            pass #删除该对象

#游戏中的墙
class Wall(BaseTtem):
    def __init__(self,screem,left,top,width,heigth):
        super().__init__(screem)
        self.rect=Rect(left,top,width,heigth)
        self.color=(255,0,0)
    def display(self):
        self.screem.fill(self.color,self.rect)
    #针对墙和坦克和炮弹的碰撞检测
    def hit_other(self):
        if TankMain.my_tank:
            is_hit =pygame.sprite.collide_rect(self,TankMain.my_tank)
            if is_hit:
                TankMain.my_tank.stop=True
game=TankMain()
game.startGame()