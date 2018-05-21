import pygame,sys,traceback
import myTank
import enemyTank

class TankGame():
    def __init__(self):#初始化
        pygame.init()#pygame初始化
        pygame.mixer.init()#音频初始化

        self.resolution = 630,630 #定义屏幕大小
        self.screen = pygame.display.set_mode(self.resolution)
        pygame.display.set_caption('TankWar') #设置窗口标题

        #加载图片、音乐、音效
        self.background_image = pygame.image.load('./image/background.png')
        self.home_image = pygame.image.load('./image/home.png')
        self.home_image_destoryed = pygame.image.load('./image/home_destroyed.png')

        self.bang_sound = pygame.mixer.Sound('./music/bang.wav')
        self.bang_sound.set_volume(1)

        self.fire_sound = pygame.mixer.Sound('./music/Gunfire.wav')
        self.start_sound = pygame.mixer.Sound('./music/start.wav')
        self.start_sound.play()
        self.clock = pygame.time.Clock()

        # 游戏的进程，是否处于游戏中或者是游戏结束的状态
        self.isGameover = False


        #创建坦克：我方坦克、敌方坦克、敌方子弹、我方子弹
        self.myTank1 = myTank.myTank(1)
        self.myBullets = []
        self.enemys = []
        self.enemys.append(enemyTank.EnemyTank())

        #创建地图


    def Gaming(self):
        # 监听事件,操控我们坦克，发射子弹
        self.myTank1.display()
        self.screen.blit(self.myTank1.tankShow,(self.myTank1.posX*24+3,self.myTank1.posY*24+3))
        for eachBullet in self.myBullets:
            self.screen.blit(eachBullet.bulletShow,(eachBullet.detailX+3,eachBullet.detailY+3))
            eachBullet.move()
            for eachEnemy in self.enemys:
                if pygame.sprite.collide_rect(eachBullet,eachEnemy):
                    print("碰撞了")
                    eachEnemy.blood -= eachBullet.hurt
                    self.myBullets.remove(eachBullet)
                    if eachEnemy.blood <= 0:
                        self.enemys.remove(eachEnemy)

        for eachEnemy in self.enemys:
            self.screen.blit(eachEnemy.enemyShow,(48,48))
        pass

    def GameOver(self):
        #得分情况、重新游戏提示
        pass

    def display(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            key_pressed = pygame.key.get_pressed()
            self.screen.blit(self.background_image,(0,0))
            if key_pressed[pygame.K_w]:
                self.myTank1.direction = 0
                self.myTank1.move()
            elif key_pressed[pygame.K_s]:
                self.myTank1.direction = 1
                self.myTank1.move()
            elif key_pressed[pygame.K_a]:
                self.myTank1.direction = 2
                self.myTank1.move()
                #print('a')
            elif key_pressed[pygame.K_d]:
                self.myTank1.direction = 3
                self.myTank1.move()
            elif key_pressed[pygame.K_j]:
                newBullet = self.myTank1.sendBullet()
                self.myBullets.append(newBullet)


            if self.isGameover:
                self.GameOver()
            else:
                self.Gaming()

            pygame.display.flip()
            self.clock.tick(60)
        #最终呈现出的画面
        pass


if __name__ == '__main__':
    tankWar = TankGame()
    tankWar.display()




