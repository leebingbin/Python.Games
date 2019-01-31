# -*- coding: UTF-8 -*-

'''
【项目介绍】
    飞机大战是一款飞行射击类游戏，它采用的涂鸦风格简单但不是趣味。在这款游戏中，玩家将操作飞机在空中战斗。飞机大战的玩法非常简单，玩家点击并移动自己的飞机，在躲避迎面而来的其他的飞机时，
通过发射炮弹打掉小飞机来赢取分数。一旦撞上其他飞机，游戏就会结束。
【具体游戏规则】
    1、游戏中的飞机分为大、中、小型三种型号；
    2、游戏中飞机的飞行速度分为高、中、低三种型号；
    3、游戏中，消灭小型飞机需要 1 发子弹，消灭中型飞机需要 5 发子弹，消灭大型飞机需要 12 发子弹；
    4、子弹的最长射程是屏幕长度的 8/10 ；
    5、消灭不同型号的飞机，所得成绩不同。每消灭一个小型飞机得 1000 分，每消灭一个中型飞机得 6000 分，每消灭一个大型飞机得 30000 分。
【分析显示过程】
    分析下游戏的界面，敌人飞机位于屏幕顶部发射子弹（随机的），玩家飞机通过左右移动躲避子弹的攻击，并且发射子弹以攻击敌人飞机。游戏的整个界面是一张背景图片，其他游戏中用到的角色同样都对应
着图片，这些图片需要借助 pygame 模块搭载窗口显示。
    在窗口中，对象显示的位置是通过坐标标注的。其中，窗口的左上角为（0，0）坐标，x 轴向右延伸数值增大，y 轴向下延伸数值增大。所有的游戏元素都参考的这个坐标系，对象在窗口的移动就是坐标位置
的变化。在窗口中完成设定的游戏场景，具体步骤如下：
    1、设置游戏背景图片；
    2、在窗口中显示玩家飞机，其具备左右移动和发射子弹的功能；
    3、在窗口中显示玩家飞机，敌人飞机保持一定的速度左右移动，并且发射随机数量的子弹。
【基本操作】
    1、玩家操作飞机，可以通过左右移动来躲避子弹；
    2、玩家飞机可以发射子弹；
    3、敌机位于屏幕顶部左右匀速运动，并且随机向玩家飞机发射子弹。
'''

import pygame
import time
import random
from pygame.locals import *

class HeroPlane(object):

    def __init__(self,screen):
        #设置飞机默认的位置
        self.x = 160
        self.y = 500
        #设置要显示内容的窗口
        self.screen = screen
        #用来保存英雄飞机需要的图片名字
        self.imageName = "./img/hero.gif"
        #根据名字生成飞机图片
        self.image = pygame.image.load(self.imageName).convert()
        # 用来存储英雄飞机发射的所有子弹
        self.bulletList = []

    def display(self):
        # 更新飞机的位置
        self.screen.blit(self.image, (self.x, self.y))
        # 用来存放需要删除的对象信息
        needDelItemList = []
        # 保存需要删除的对象
        for i in self.bulletList:
            if i.judge():
                needDelItemList.append(i)
        # 删除self.bulletList中需要删除的对象
        for i in needDelItemList:
            self.bulletList.remove(i)

        for bullet in self.bulletList:
            bullet.display()
            bullet.move()

    def sheBullet(self):
        newBullet = Bullet(self.x, self.y, self.screen)
        self.bulletList.append(newBullet)

    def moveLeft(self):
        self.x -= 10

    def moveRight(self):
        self.x += 10


class EnemyPlane(object):
    def __init__(self,screen):
        #设置飞机默认的位置
        self.x = 0
        self.y = 0
        #设置要显示内容的窗口
        self.screen = screen
        self.imageName = "./img/enemy-1.gif"
        self.image = pygame.image.load(self.imageName).convert()
        #用来存储敌人飞机发射的所有子弹
        self.bulletList = []
        self.direction = "right"

    def move(self):
        # 如果碰到了右边的边界，那么就往左走，如果碰到了左边的边界，那么就往右走
        if self.direction == "right":
            self.x += 2
        elif self.direction == "left":
            self.x -= 2
        if self.x > 430 - 50:
            self.direction = "left"
        elif self.x < 0:
            self.direction = "right"

    def display(self):
        # 更新飞机的位置
        self.screen.blit(self.image, (self.x, self.y))

        # 存放需要删除的对象信息
        needDelItemList = []

        for i in self.bulletList:
            if i.judge():
                needDelItemList.append(i)

        for i in needDelItemList:
            self.bulletList.remove(i)

        # 更新及这架飞机发射出的所有子弹的位置
        for bullet in self.bulletList:
            bullet.display()
            bullet.move()

    def sheBullet(self):
        num = random.randint(1, 100)
        if num == 88:
            newBullet = EnemyBullet(self.x, self.y, self.screen)
            self.bulletList.append(newBullet)

class Bullet(object):
    def __init__(self,x,y,screen):
        self.x = x+40
        self.y = y-20
        self.screen = screen
        self.image = pygame.image.load("./img/bullet-3.gif").convert()

    def display(self):
        self.screen.blit(self.image,(self.x,self.y))

    def move(self):
        self.y -= 2

    def judge(self):
        if self.y < 0:
            return True
        else:
            return False

class EnemyBullet(object):
    def __init__(self,x,y,screen):
        self.x = x+22
        self.y = y+30
        self.screen = screen
        self.image = pygame.image.load("./img/bullet-1.gif").convert()

    def display(self):
        self.screen.blit(self.image,(self.x,self.y))

    def move(self):
        self.y += 20

    def judge(self):
        if self.y>750:
            return True
        else:
            return False

if __name__ == "__main__":
    #1. 创建一个窗口，用来显示内容
    screen = pygame.display.set_mode((430,750),0,32)

    #2. 创建一个和窗口大小的图片，用来充当背景
    background = pygame.image.load("./img/background.png").convert()

    #3. 创建一个飞机对象
    heroPlane = HeroPlane(screen)

    # 4. 创建一个敌人飞机
    enemyPlane = EnemyPlane(screen)

    #4. 把背景图片放到窗口中显示
    while True:
        screen.blit(background,(0,0))
        heroPlane.display()
        enemyPlane.display()
        enemyPlane.move()
        enemyPlane.sheBullet()

        #判断是否是点击了退出按钮
        for event in pygame.event.get():
            # print(event.type)
            if event.type == QUIT:
                print("exit")
                exit()
            elif event.type == KEYDOWN:

                if event.key == K_a or event.key == K_LEFT:
                    # print('left')
                    #控制飞机让其向左移动
                    heroPlane.moveLeft()
                elif event.key == K_d or event.key == K_RIGHT:
                    # print('right')
                    heroPlane.moveRight()
                elif event.key == K_SPACE:
                    heroPlane.sheBullet()

        # 通过延时的方式，来降低这个while循环的循环速度，从而降低了cpu占用率
        time.sleep(0.05)
        pygame.display.update()