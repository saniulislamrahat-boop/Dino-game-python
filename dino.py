import pygame as pg

class Dino(pg.sprite.Sprite):
    def __init__(self):
        super(Dino,self).__init__()
        self.dino_run_lists=[pg.image.load("dino1.png").convert_alpha(),
                             pg.image.load("dino2.png").convert_alpha()
                             ]
        self.dino_runcruch_lists=[pg.image.load("dino_crouch1.png").convert_alpha(),
                                pg.image.load("dino_crouch2.png").convert_alpha()]
        
        self.image=self.dino_run_lists[0]
        self.mask=pg.mask.from_surface(self.image)
        self.rect=pg.Rect(200,200,43,51)
        self.restdino()
        # self.update()
        self.gravity=10
        self.speed=250

    def update(self,dt):
        keys=pg.key.get_pressed()
        if keys[pg.K_DOWN]: self.crouch=True
        else: self.crouch=False
        if  self.is_onG:

            if self.anim_count==5:
                if self.crouch:
                    self.image=self.dino_runcruch_lists[self.imageswh]
                    self.rect=pg.Rect(200,220,55,30)

                else:
                    self.image=self.dino_run_lists[self.imageswh]
                    self.rect=pg.Rect(200,200,43,51)
                self.mask=pg.mask.from_surface(self.image)
                # self.image=self.dino_run_lists[self.imageswh]
                # self.image=self.dino_run_lists[0]
                if self.imageswh==0: self.imageswh=1
                else:self.imageswh=0
                self.anim_count=0
            self.anim_count+=1
        else:
            self.vY+=self.gravity*dt
            self.rect.y+=self.vY
            if self.rect.y>=200:
                self.is_onG=True
                self.rect.y=200
    def jumpD(self,dt):
        if self.is_onG:

            self.vY = - self.speed * dt
            self.is_onG=False

                

        
    
    def restdino(self):

        self.rect=pg.Rect(200,200,43,51)
        self.imageswh=1
        self.anim_count=0
        self.crouch=False
        self.is_onG=True
        self.vY=0



