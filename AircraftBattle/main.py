# -*- coding: UTF-8 -*-

import pygame
from pygame.locals import *
from plane import *


def start():  # 开始游戏
    # 创建一个窗口，用来显示内容
    screen = pygame.display.set_mode((480, 890), 0, 32)
    # 创建一个和窗口大小的图片，用来充当背景
    image_file_path = "./img/background.png"
    background = pygame.image.load(image_file_path).convert()
    # 创建一个飞机对象
    hero_plane = HeroPlane(screen)
    # 把背景图片放到窗口中显示
    while True:
        screen.blit(background, (0, 0))
        hero_plane.display()
        # 判断是否是点击了退出按钮
        for event in pygame.event.get():
            if event.type == QUIT:
                print("exit")
                exit()
            elif event.type == KEYDOWN:
                if event.key == K_a or event.key == K_LEFT:
                    print("left")
                    # 控制飞机让其向左移动
                    hero_plane.move_left()
                elif event.key == K_d or event.key == K_RIGHT:
                    print("right")
                    # 控制飞机让其向右移动
                    hero_plane.move_right()
                elif event.key == K_SPACE:
                    print("space")
        pygame.display.update()


if __name__ == "__main__":
    start()
