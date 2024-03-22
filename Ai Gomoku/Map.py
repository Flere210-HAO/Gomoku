import pygame
from enum import IntEnum
from pygame.locals import *  #导入pygame的locals模块
'''
Pygame Locals模块是一个常量模块，其中包含了大量的常量定义，这些常量定义主要用于以下几个方面：
    事件像键盘鼠标等的名称、值等。
    Pygame中定义的颜色、特效等值。
    Pygame中所支持的字体的名称和样式。
    屏幕的尺寸和特效。
'''
Game_ver =  'V0.1'

Squa_size = 40      #棋子格子大小
Chess_Radius = Squa_size/2 -2   #棋子的半径
Chess_Len= 15   #棋盘是15*15的
Map_Width = Chess_Len*Squa_size     #确定整个棋盘的大小
Map_Height = Chess_Len*Squa_size

Button_Width = 150
Button_Height = 60

Screen_Width = Map_Width + Button_Width
Screen_Height = Map_Height

#确定各个组件的大小先

class Map_input_type(IntEnum):
    Map_Empty=0
    Map_PlayerOne = 1
    Map_PlayerTwo = 2
    Map_out = 3         #不在界面内的选项

