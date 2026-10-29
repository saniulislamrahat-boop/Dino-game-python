import pygame as pg
import random

class Tree(pg.sprite.Sprite):
    def __init__(self,enemyG,speed):
        super(Tree,self).__init__()
        self.imageL=[]
        for i in range(1,6):
            self.imageL.append(pg.image.load(f"trees/tree{i}.png").convert_alpha())

        self.image=self.imageL[random.randint(0,4)]
        self.mask=pg.mask.from_surface(self.image)
        self.rect=pg.Rect(600,202,50,50)
        self.enemyG=enemyG
        self.speed=speed

    def update(self,dt):

        self.rect.x-=self.speed*dt
        if self.rect.right<=0:
           self.deletemyself()
    
    def setMovespeed(self,move_speed):
        self.speed=move_speed
    def deletemyself(self):
        self.kill()
