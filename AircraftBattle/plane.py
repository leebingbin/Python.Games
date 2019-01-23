# -*- coding: UTF-8 -*-
import random
import pygame
from bullet import *


class HeroPlane(object):
    def __init__(self, screen):
        # 设置飞机默认的位置
        self.x = 230
        self.y = 600
        # 设置要显示内容的窗口
        self.screen = screen
        # 用来保存英雄飞机需要的图片名字
        self.image_name = "./img/hero.gif"
        # 根据图片的名称生成飞机图片
        self.image = pygame.image.load(self.image_name).convert()
        # 用来存储英雄飞机发射的所有子弹
        self.bullet_list = []

    def display(self):
        # 更新飞机的位置
        self.screen.blit(self.image, (self.x, self.y))
        # 用来存放需要删除的对象位置
        need_del_list = []
        # 保存需要删除的对象
        for item in self.bullet_list:
            if item.judge():
                need_del_list.append(item)
        # 删除 self.bullet_list 中需要删除的对象
        for del_item in need_del_list:
            self.bullet_list.remove(del_item)
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()

    def move_left(self):
        self.x -= 10

    def move_right(self):
        self.x += 10

    # 发射子弹的方法
    def launch_bullet(self):
        number = random.randint(1, 100)
        if number == 50:
            new_bullet = EnemyBullet(self.x, self.y, self.screen)
            self.bullet_list.append(new_bullet)


class EnemyPlane(object):
    def __init__(self, screen):
        # 设置飞机默认的位置
        self.x = 0
        self.y = 0
        # 设置要显示内容的窗口和图像
        self.screen = screen
        self.image_name = "./img/enemy-1.gif"
        self.image = pygame.image.load(self.image_name).convert()
        # 用来存储敌人飞机发射的所有子弹
        self.bullet_list = []
        # 记录飞机的初始运动方向
        self.direction = "right"

    def display(self):
        # 更新飞机的位置
        self.screen.blit(self.image, (self.x, self.y))
        # 存放需要删除的对象信息
        need_del_list = []
        for i in self.bullet_list:
            if i.judge():
                need_del_list.append(i)
        for i in need_del_list:
            self.bullet_list.remove(i)
        # 更新这架飞机发射出的所有子弹的位置
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()

    def move(self):
        # 如果碰到了右边的边界，那么就往左走；反之，同理
        if self.direction == "right":
            self.x += 2
        elif self.direction == "left":
            self.x -= 2
        if self.x > 480 - 50:
            self.direction = "left"
        elif self.x < 0:
            self.direction = "right"

    # 发射子弹的方法
    def launch_bullet(self):
        number = random.randint(1, 100)
        if number == 88:
            new_bullet = EnemyBullet(self.x, self.y, self.screen)
            self.bullet_list.append(new_bullet)
