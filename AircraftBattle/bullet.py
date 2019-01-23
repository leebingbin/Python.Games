# -*- coding: UTF-8 -*-

import pygame


class Bullet(object):
    def __init__(self, x, y, screen):
        self.x = x + 40
        self.y = y - 20
        self.screen = screen
        self.image = pygame.image.load("./img/bullet-3.gif").convert()

    def move(self):
        self.y -= 2

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def judge(self):
        if self.y < 0:
            return True
        else:
            return False


class EnemyBullet(object):
    def __init__(self, x, y, screen):
        self.x = x + 30
        self.y = y + 30
        self.screen = screen
        self.image = pygame.image.load("./img/bullet-1.gif").convert()

    def move(self):
        self.y += 2

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def judge(self):
        if self.y > 890:
            return True
        else:
            return False
