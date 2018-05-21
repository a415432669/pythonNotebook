import pygame

class Brick(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('./image/brick.png')
        self.rect = self.image.get_rect()

class Iron(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('./image/iron.png')
        self.rect = self.image.get_rect()

class Map():
    def __init__(self):
        self.brickGroup = pygame.sprite.Group()
        self.ironGroup = pygame.sprite.Group()
        #0-25左右上下坐标轴的上下限
        self.brickArr = [(10,10),(11,10),(12,10),(13,10),(14,10),(15,10)]
        self.ironArr = [(20, 10), (21, 10), (22, 10), (23, 10)]

        for brick in self.brickArr:
            self.brick = Brick()
            self.brick.rect.left,self.brick.rect.top = 24*brick[0],24*brick[1]
            self.brickGroup.add(self.brick)

        for iron in self.ironArr:
            self.iron = Iron()
            self.iron.rect.left,self.iron.rect.top = 24*iron[0],24*iron[1]
            self.ironGroup.add(self.iron)

