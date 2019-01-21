# -*- coding: UTF-8 -*-

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
        new_bullet = Bullet(self.x,self.y,self.screen)
        self.bullet_list.append(new_bullet)
