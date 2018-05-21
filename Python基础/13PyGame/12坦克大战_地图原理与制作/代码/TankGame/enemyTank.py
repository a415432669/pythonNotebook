import pygame
import random
import bullet

class EnemyTank(pygame.sprite.Sprite):
    def __init__(self):
        #运动的方向、运动和静止的状态
        #坦克的是否还活着
        #坦克的血量

        self.blood = 1000
        self.isLife = True
        self.enemy_red_imgage = pygame.image.load('./image/enemy_1_3.png')
        self.enemyShow = self.enemy_red_imgage.subsurface((0,48),(48,48))
        self.rect = self.enemyShow.get_rect()
        self.rect.topleft = 51,51
        pass

    def display(self):
        pass

