# -*- coding: UTF-8 -*-

import pygame


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

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move_left(self):
        self.x -= 10

    def move_right(self):
        self.x += 10
