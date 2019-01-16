import pygame


def start():  # 开始游戏
    # 创建一个窗口，用来显示内容
    screen = pygame.display.set_mode((480, 890), 0, 32)
    # 创建一个和窗口大小的图片，用来充当背景
    image_file_path = "./img/background.png"
    background = pygame.image.load(image_file_path).convert()
    # 把背景图片放到窗口中显示
    while True:
        screen.blit(background, (0, 0))
        pygame.display.update()


if __name__ == "__main__":
    start()
