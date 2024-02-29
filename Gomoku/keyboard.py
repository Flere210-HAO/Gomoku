#调用pygame库来进行棋盘的设置
import pygame
import sys

#内部各功能模块进行初始化以及变量设置，默认调用
pygame.init()
#获取对显示的访问，并创建一个窗口screen
#设置窗口大小
screen = pygame.display.set_mode((670,670))
#设置窗口颜色
screen_color = [255,255,255] #白色
while True:
    for event in pygame.event.get():
        if event.type in pygame.QUIT:
            sys.exit()
        screen.fill(screen_color)
        pygame.display.update()
