#调用pygame库来进行棋盘的设置
import pygame
import sys
import numpy as np

#内部各功能模块进行初始化以及变量设置，默认调用
pygame.init()
#获取对显示的访问，并创建一个窗口screen
#设置窗口大小
screen = pygame.display.set_mode((850,670))  #调整宽度来给调整类型按钮留下空间
#设置窗口颜色
screen_color = [238,155,65] #白色(换成像棋盘一样的颜色
line_color = [0,0,0] #设置线条颜色，黑色

tim=0 #给鼠标左键建立延迟时间

board = np.zeros((15,15)) #存作棋盘的棋子位置

def find_pos(x,y):
    for i in range(27,670,44):
        for j in range(27,670,44):
            L1=i-22
            L2=i+22
            R1=j-22
            R2=j+22
            if x>=L1 and x<=L2 and y>=R1 and y<=R2:
                return i,j
    return x,y


while True: #刷新画布（pygame就像一个画布不断刷新
    for event in pygame.event.get():  #获取事件，如果点击窗口右上角的关闭案件即关闭
        if event.type in (pygame.QUIT,pygame.KEYDOWN):
            sys.exit()
    screen.fill(screen_color)  #清屏，刷成了screen_color 的颜色


    #pygame.draw.line(screen,line_color,[0,0],[670,670],2)
    for i in range(27,670,44):
        #先画竖线
        if i==27 or i==670-27:
            pygame.draw.line(screen,line_color,[i,27],[i,670-27],4)
        else:
            pygame.draw.line(screen,line_color,[i,27],[i,670-27],2)
        #
        if i==27 or i==670-27:
            pygame.draw.line(screen,line_color,[27,i],[670-27,i],4)
        else:
            pygame.draw.line(screen,line_color,[27,i],[670-27,i],2)

    pygame.draw.circle(screen,line_color,[27,27],8,0)

    x,y = pygame.mouse.get_pos()
    x,y = find_pos(x,y)
    if x<=670 and y<=670:
        # 把下棋的方格限制再棋盘内
        pygame.draw.rect(screen,[0,229,238],[x-22,y-22,44,44],2,1)
    mouse_press = pygame.mouse.get_pressed()
    #在pygame中对按键的连续检测是默认失能的，调用上述函数便可以使能按键的连续检测。
    #按键的连续检测使能后，当按键按下时，将会以delay的延时去触发第一次的KEYDOWN事件，之后则会以interval的延时去触发接下来的KEYDOWN事件。
    #通俗的讲，第一个参数影响着按键的灵敏度，第二个参数影响着按键的移动时间间隔，不调整参数的话你会发现按了一下左键会触发很多次
    if mouse_press[0]==True and tim==0:
        print('按下了鼠标左键')


    pygame.display.update()  #更新pygame这个画布
