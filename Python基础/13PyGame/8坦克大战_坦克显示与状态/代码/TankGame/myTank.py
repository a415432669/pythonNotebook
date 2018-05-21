import pygame

class myTank(pygame.sprite.Sprite):
    def __init__(self,playNumber):#设置创造哪一个玩家玩的坦克，有玩家1和玩家2
        #等级、运动的方向、运动和静止的状态
        #坦克的是否还活着
        #坦克的血量
        #坦克的命数
        #坦克的得分
        pygame.sprite.Sprite.__init__(self)
        self.life = True
        self.level = 0
        self.score = 0
        self.blood = 100
        self.lifeNum = 3
        self.direction = 1 #（1,2,3,4，上下左右）
        self.moveState = 1 #（0,1，静止，运动）
        self.playerNumber = playNumber
        self.count = 0


        pass

    #发射子弹、操控坦克、向左右上下移动、坦克显示
    def display(self):
        if self.playerNumber == 1:
            self.tank_L0_image = pygame.image.load('./image/tank_T1_0.png').convert_alpha()
            self.tank_L1_image = pygame.image.load('./image/tank_T1_1.png').convert_alpha()
            self.tank_L2_image = pygame.image.load('./image/tank_T1_2.png').convert_alpha()
        else:
            self.tank_L0_image = pygame.image.load('./image/tank_T2_0.png').convert_alpha()
            self.tank_L1_image = pygame.image.load('./image/tank_T2_1.png').convert_alpha()
            self.tank_L2_image = pygame.image.load('./image/tank_T2_2.png').convert_alpha()


        if self.level == 0:
            self.tank = self.tank_L0_image
        elif self.level == 1:
            self.tank = self.tank_L1_image
        else:
            self.tank = self.tank_L3_image

        if self.direction == 1:
            if self.moveState == 0:
                self.tankShow = self.tank.subsurface((0,0),(48,48))
            else:
                if self.count < 15:
                    self.tankShow = self.tank.subsurface((0,0),(48,48))
                    self.count += 1
                else:
                    self.tankShow = self.tank.subsurface((48, 0), (48, 48))
                    self.count += 1
                    print(self.count)
                    if self.count >= 30:
                        self.count = 0

