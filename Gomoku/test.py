"""
import pygame
from pygame.locals import *

# 初始化PyGame引擎
pygame.init()

# 设置窗口尺寸
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Button Example")

# 设置按钮的属性
x, y = 350, 250
width, height = 100, 50
button_rect = pygame.Rect(x, y, width, height)
button_color = (255, 255, 255)
text_color = (0, 0, 0)
button_font = pygame.font.Font()
button_text = button_font.render("Button", True, text_color)

# 游戏主循环
running = True
while running:
    screen.fill((0, 0, 0))  # 清空屏幕

    # 绘制按钮
    pygame.draw.rect(screen, button_color, button_rect)
    screen.blit(button_text, (button_rect.centerx - button_text.get_width() / 2, button_rect.centery - button_text.get_height() / 2))

    # 监听事件
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                # 在这里执行按钮点击后的操作
                print("Button clicked!")

    pygame.display.flip()  # 更新屏幕显示

# 退出游戏
pygame.quit()
"""

"""
#开始界面的测试  完成√
import pygame
import sys
#内部各功能模块进行初始化以及变量设置，默认调用
pygame.init()
#获取对显示的访问，并创建一个窗口screen
#设置窗口大小

screen = pygame.display.set_mode((800,800))  #调整宽度来给调整类型按钮留下空间
start_screen = pygame.Surface(screen.get_size())
game_screen=pygame.Surface(screen.get_size())
start_screen = start_screen.convert()
game_screen = game_screen.convert()
start_screen.fill((255,255,255))
game_screen.fill((0,255,0))
#设置窗口颜色
screen_color = [238,155,65] #白色(换成像棋盘一样的颜色
black_color = [0,0,0] #设置线条颜色，黑色(从line_color变成了black_color,收缩一下定义)
white_color = [255,255,255] #白色
clock = pygame.time.Clock()



s1 = pygame.image.load("./image/S1.png")
s1.convert()
s2 = pygame.image.load("./image/S2.png")
s2.convert()
e1 = pygame.image.load("./image/E1.png")
e1.convert()
e2 = pygame.image.load("./image/E2.png")
e2.convert()
n1=True
while n1:
    clock.tick(30)
    for event in pygame.event.get():  #获取事件，如果点击窗口右上角的关闭案件即关闭
        if event.type in (pygame.QUIT,pygame.KEYDOWN):
            sys.exit()
    buttons=pygame.mouse.get_pressed()
    x1,y1=pygame.mouse.get_pos()
    if x1>=227 and x1<=555 and y1>=261 and y1<=327:
        start_screen.blit(s2,(200,240))
        if buttons[0]:
            n1 = False

    elif x1 >= 227 and x1 <= 555 and y1>=381 and y1<=447:
        start_screen.blit(e2,(200,360))
        if buttons[0]:
            pygame.quit()
            exit()

    else:
        start_screen.blit(s1,(200,240))
        start_screen.blit(e1,(200,360))

    screen.blit(start_screen,(0,0))
    pygame.display.update()

n2 = True
while n2:
    for event in pygame.event.get():  #获取事件，如果点击窗口右上角的关闭案件即关闭
        if event.type in (pygame.QUIT,pygame.KEYDOWN):
            sys.exit()
    screen.blit(game_screen,(0,0))
    pygame.display.update()
    
"""

def AlphaBeta(depth,alpha,beta):
    if depth==0:
        return False
