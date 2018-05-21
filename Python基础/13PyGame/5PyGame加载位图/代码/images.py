#要使用必先导入
import pygame
#导入pygame中的所有常量
from pygame.locals import *
import sys


#screen = pygame.display.set_mode()
#space = pygame.image.load("图片地址").convert_alpha() #适合JPG/PNG/GIF/BMP/PCX/TIF
#screen.blit(space,(0,0))


#初始化PyGame
pygame.init()
#创建一个600*500的窗口
screen = pygame.display.set_mode((600,500))

#打印文字到窗口
myfont = pygame.font.Font(None,60)
#RGB,R红色，G绿色，B蓝色
white = (255,255,255)
blue = (0,0,255)
textImage = myfont.render('Hello PyGame',True,white)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()


    logo = pygame.image.load('./images/home.png')
    # 清理屏幕，绘制，然后刷新
    #screen.fill(blue)
    logo = pygame.transform.smoothscale(logo,(200,200))
    screen.blit(logo,(0,0))
    pygame.display.update()
