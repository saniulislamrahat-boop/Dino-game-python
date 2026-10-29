import pygame as pg

class Bird(pg.sprite.Sprite):
    def __init__(self,enemyG,speed):
        super(Bird,self).__init__()
        self.imageL=[pg.image.load("bird1.png").convert_alpha(),
                     pg.image.load("bird2.png").convert_alpha()]
        self.image=self.imageL[0]
        self.mask=pg.mask.from_surface(self.image)
        self.rect=pg.rect=pg.Rect(600,180,42,31)
        self.aniC=0
        self.enemyG=enemyG
        self.speed=speed
        self.imgswh=1


    def update(self,dt):
        if self.aniC==7:
            self.image=self.imageL[self.imgswh]
            if self.imgswh==0: self.imgswh=1
            else:self.imgswh=0
            self.aniC=0
        self.aniC+=1


        self.rect.x-=self.speed*dt
        if self.rect.right<=0:
            self.deletemyself()
            


    def setMovespeed(self,move_speed):
        self.speed=move_speed
    
    def deletemyself(self):
        self.kill()
        del self

