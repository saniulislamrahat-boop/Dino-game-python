import pygame as pg
import sys
import time
from dino import Dino
from bird import Bird
import random
from tree import Tree


pg.init()

class Game:

    def __init__(self):
        self.width=600
        self.hight=300
        self.win=pg.display.set_mode((self.width,self.hight))
        self.clock=pg.time.Clock()

        self.ground=pg.image.load("ground.png").convert_alpha()
        self.ground_rect=self.ground.get_rect(center=(300,250))
        self.ground2=pg.image.load("ground.png").convert_alpha()
        self.ground_rect2=self.ground.get_rect(center=(900,250))

        self.font=pg.font.Font("font.ttf",20)

        self.lvlS=self.font.render("score:0",True,(0,0,0))
        self.lvlS_rect=self.lvlS.get_rect(center=(500,20))
        self.lvlRe=self.font.render("Restart",True,(0,0,0))
        self.lvlRe_rect=self.lvlRe.get_rect(center=(300,150))

        self.dino=Dino()
        self.game_lost=False
        self.speed=250
        self.eneSC=0
        self.eneSpawnT=80
        self.eneG=pg.sprite.Group()
        self.score=0
        
        self.deadS=pg.mixer.Sound("sfx/dead.mp3")
        self.jumpS=pg.mixer.Sound("sfx/jump.mp3")
        self.points=pg.mixer.Sound("sfx/points.mp3")


        
        self.gameloop()
    def chekCollision(self):
        if pg.sprite.spritecollide(self.dino,self.eneG,False,pg.sprite.collide_mask):
            self.stopGame()
    def stopGame(self):
        self.game_lost=True
        self.deadS.play()

    def restart(self):
        self.game_lost=False
        self.score=0
        self.eneSC=0
        self.speed=250
        self.lvlS=self.font.render("score:0",True,(0,0,0))
        self.dino.restdino()
        for enemy in self.eneG:
            enemy.deletemyself()

    def gameloop(self):
        last_time=time.time()
        while True:
            new_time=time.time()
            dt=new_time-last_time
            last_time=new_time
            for event in pg.event.get():
                if event.type==pg.QUIT:
                    pg.quit()
                    # sys.exit()
                    break
                if event.type==pg.KEYDOWN and event.key==pg.K_SPACE:
                    if not self.game_lost :
                        self.dino.jumpD(dt)
                        self.jumpS.play()
                    else:
                        self.restart()
            
            self.win.fill((255,255,255))
            if not self.game_lost:
                self.ground_rect.x-=int(self.speed*dt)
                self.ground_rect2.x-=int(self.speed*dt)

                if self.ground_rect.right<0:
                    self.ground_rect.x=600

                if self.ground_rect2.right<0:
                    self.ground_rect2.x=600

                self.score+=0.1
                self.lvlS=self.font.render(f"score:{int(self.score)}",True,(0,0,0))

            
                self.dino.update(dt)
                self.eneG.update(dt)
                if self.eneSC==self.eneSpawnT:
                    if random.randint(0,1)==0:
                        self.eneG.add(Bird(self.eneG, self.speed))
                    else:
                        self.eneG.add(Tree(self.eneG, self.speed))
                    self.eneSC=0
                self.eneSC+=1
                if int(self.score)%30==0:
                    self.speed+=1
                    for ene in self.eneG:
                        ene.setMovespeed(self.speed)
                if int(self.score+1)%100==0:
                    self.points.play()
                
                        
                self.win.blit(self.dino.image,self.dino.rect)
                
                for enemy in self.eneG:
                        self.win.blit(enemy.image, enemy.rect)
                self.chekCollision()
            else:
                self.win.blit(self.lvlRe,self.lvlRe_rect)
                
                

            self.win.blit(self.ground,self.ground_rect)
            self.win.blit(self.ground2,self.ground_rect2)
            self.win.blit(self.lvlS,self.lvlS_rect)

            pg.display.update()
            self.clock.tick(60)




game=Game()

