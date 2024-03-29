#调用pygame库来进行棋盘的设置
import queue

import pygame
import sys
import numpy as np

#内部各功能模块进行初始化以及变量设置，默认调用
pygame.init()
#获取对显示的访问，并创建一个窗口screen
#设置窗口大小
start_screen = pygame.display.set_mode(670,670)
screen = pygame.display.set_mode((850,670))  #调整宽度来给调整类型按钮留下空间
#设置窗口颜色
screen_color = [238,155,65] #白色(换成像棋盘一样的颜色
black_color = [0,0,0] #设置线条颜色，黑色(从line_color变成了black_color,收缩一下定义)
white_color = [255,255,255] #白色

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

def check_pos(x,y,pos):
    for val in pos:
        if val[0][0]==x and val[0][1]==y:
            return False
    return True #表示没有落子


tim=0 #给鼠标左键建立延迟时间
board = np.zeros((15,15)) #存作棋盘的棋子位置(用一个全局变量存下来可以减少运算)
#over_pos = queue.Queue()  本来想着队列先进先出好弄悔棋，但是遍历队列需要迭代器不如列表
over_pos=[]
flag=False
direction=[(1,0),(0,1),(1,1),(1,-1)]

def check_win(pos):
    if len(pos)==0:
        return False
    val = pos[len(pos)-1]
    x = int((val[0][0] - 27) / 44)
    y = int((val[0][1] - 27) / 44)
    if val[1]==black_color:
        board[x][y]=1
    else:
        board[x][y]=2
    for os in direction:
        if check_direction_win(x,y,board[x][y],os[0],os[1]):
            return True

def check_direction_win(point_x,point_y,chest,x_offset,y_offset):
    count = 1
    for step in range(-4,4):
        x=point_x+step*x_offset
        y=point_y+step*y_offset
        if step==0:
            break
        if 0<=x<15 and 0<=y<15 and board[x][y]==chest:
            count=count+1
        elif count<5 and board[x][y]!=chest:
            count=1
        else:
            break
    return count>=5



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
    buttons=pygame.mouse.get_pressed()
    x1,y1=pygame.mouse.get_pos()





while True: #刷新画布（pygame就像一个画布不断刷新
    for event in pygame.event.get():  #获取事件，如果点击窗口右上角的关闭案件即关闭
        if event.type in (pygame.QUIT,pygame.KEYDOWN):
            sys.exit()
    screen.fill(screen_color)  #清屏，刷成了screen_color 的颜色


    #pygame.draw.line(screen,black_color,[0,0],[670,670],2)
    for i in range(27,670,44):
        #先画竖线
        if i==27 or i==670-27:
            pygame.draw.line(screen,black_color,[i,27],[i,670-27],4)
        else:
            pygame.draw.line(screen,black_color,[i,27],[i,670-27],2)
        #再画横线
        if i==27 or i==670-27:
            pygame.draw.line(screen,black_color,[27,i],[670-27,i],4)
        else:
            pygame.draw.line(screen,black_color,[27,i],[670-27,i],2)

    pygame.draw.circle(screen,black_color,[27,27],8,0)

    x,y = pygame.mouse.get_pos()
    x,y = find_pos(x,y)
    if x<=670 and y<=670:
        if check_pos(x,y,over_pos):
        # 把下棋的方格限制再棋盘内,并判断是否能落子
            pygame.draw.rect(screen,[0,229,238],[x-22,y-22,44,44],2,1)
        mouse_press = pygame.mouse.get_pressed()
        #在pygame中对按键的连续检测是默认失能的，调用上述函数便可以使能按键的连续检测。
        #按键的连续检测使能后，当按键按下时，将会以delay的延时去触发第一次的KEYDOWN事件，之后则会以interval的延时去触发接下来的KEYDOWN事件。
        #通俗的讲，第一个参数影响着按键的灵敏度，第二个参数影响着按键的移动时间间隔，不调整参数的话你会发现按了一下左键会触发很多次
        if mouse_press[0]==True and tim==0:
            #print('按下了鼠标左键')
            flag=True
            if check_pos(x,y,over_pos):
                if len(over_pos)%2==0:  #黑棋
                    over_pos.append([[x,y],black_color])
                else:
                    over_pos.append([[x,y],white_color])

    if flag: #做出200Ms的延迟
        tim=tim+1
    if tim%200==0:
        flag=False
        tim=0

    for val in over_pos: #画下棋子
        pygame.draw.circle(screen,val[1],val[0],15,0)
        print(val[0])
    if check_win(over_pos):
        val = over_pos[len(over_pos) - 1]
        if val[1]==black_color:
            print('Black Win!')
        else:
            print('White Win!')
    pygame.display.update()  #更新pygame这个画布
