import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self,direction=0,posX=0,posY=0,hurt=100):
        #子弹发射的方向，子弹的位置，子弹的速度，子弹的生命,子弹的伤害量
        self.direction = direction
        self.posX = posX
        self.posY = posY
        self.hurt = hurt
        self.runTime = 2
        self.bullet_up = pygame.image.load('./image/bullet_up.png')
        self.bullet_down = pygame.image.load('./image/bullet_down.png')
        self.bullet_left = pygame.image.load('./image/bullet_left.png')
        self.bullet_right = pygame.image.load('./image/bullet_right.png')
        self.arrImage = [self.bullet_up,self.bullet_down,self.bullet_left,self.bullet_right]

        self.bulletShow = self.arrImage[direction]

        if self.direction == 0:
            self.detailX = posX*24 + 24
            self.detailY = posY*24
        elif self.direction == 1:
            self.detailX = posX*24 + 24
            self.detailY = posY*24 + 48
        elif self.direction == 2:
            self.detailX = posX*24
            self.detailY = posY*24 + 24
        elif self.direction == 3:
            self.detailX = posX*24 + 48
            self.detailY = posY*24 + 24

        pass

    def move(self):
        if self.runTime == 0:
            self.runTime = 2
            if self.direction == 0:
                    self.posY -= 1
            elif self.direction == 1:
                    self.posY += 1
            elif self.direction == 2:
                    self.posX -= 1
            else:
                    self.posX += 1

            if self.direction == 0:
                self.detailX = self.posX * 24 + 24 - 6
                self.detailY = self.posY * 24
            elif self.direction == 1:
                self.detailX = self.posX * 24 + 24 - 6
                self.detailY = self.posY * 24 + 48
            elif self.direction == 2:
                self.detailX = self.posX * 24
                self.detailY = self.posY * 24 + 24 - 6
            elif self.direction == 3:
                self.detailX = self.posX * 24 + 48
                self.detailY = self.posY * 24 + 24 - 6
        else:
            self.runTime -= 1
        pass


