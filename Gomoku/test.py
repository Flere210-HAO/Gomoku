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