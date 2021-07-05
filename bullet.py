import pygame
import math


class Bullet(pygame.sprite.Sprite):
    def __init__(self, StartposX, StartposY):
        self.pos_x = StartposX
        self.pos_y = StartposY
        self.startPosX = StartposX
        self.startPosY = StartposY
        self.range = 1000
        self.radius = 6
        self.hitbox = 0
        self.speed = 10
        self.damage = 1
        self.out_range = False
        self.typebox = "Circle"

    def bullet_action(self):
        pass

    def bullet_verify(self):
        pass
    

class Soul_Bullet(Bullet):

    def __init__(self, StartposX, StartposY, polarity):
        Bullet.__init__(self, StartposX, StartposY)
        self.polarity = polarity
        self.speed = 18
        self.damage = 20

    def bullet_action(self):
        if self.polarity == "BottomTop":
            self.pos_y -= self.speed
        if (self.polarity == "TopBottom"):
            self.pos_y += self.speed 
        if (self.polarity == "LeftRight"):
            self.pos_x += self.speed
        if (self.polarity == "RightLeft"):
            self.pos_x -= self.speed


    def bullet_verify(self):
        if (self.pos_y)-(self.startPosY) > self.range or (-self.pos_y)-(-self.startPosY) > self.range:
            self.out_range = True

        if (self.pos_x)-(self.startPosX) > self.range or (-self.pos_x)-(-self.startPosX) > self.range:
            self.out_range = True

    def update_frame(self, display):
        pass


class Normal_Bullet(Bullet):
    def __init__(self, StartposX, StartposY, targetx, targety):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('./images/normal_bullet/sprite_normal_bullet0.png'))
        self.sprites.append(pygame.image.load('./images/normal_bullet/sprite_normal_bullet1.png'))
        self.sprites.append(pygame.image.load('./images/normal_bullet/sprite_normal_bullet2.png'))
        self.sprites.append(pygame.image.load('./images/normal_bullet/sprite_normal_bullet3.png'))
        self.sprites.append(pygame.image.load('./images/normal_bullet/sprite_normal_bullet4.png'))
        self.sprites.append(pygame.image.load('./images/normal_bullet/sprite_normal_bullet5.png'))
        self.sprites.append(pygame.image.load('./images/normal_bullet/sprite_normal_bullet6.png'))
        self.sprites.append(pygame.image.load('./images/normal_bullet/sprite_normal_bullet7.png'))
        self.sprites.append(pygame.image.load('./images/normal_bullet/sprite_normal_bullet8.png'))
        self.this_frame = 0
        self.image = self.sprites[self.this_frame]

        all_sprites = pygame.sprite.Group()
        all_sprites.add(self)

        Bullet.__init__(self, StartposX, StartposY)
        self.image = pygame.transform.scale(self.image, (int(self.radius/8), int(self.radius/8)))
        self.speed = 10
        self.range = 1700
        angle = math.atan2(targety-self.startPosY, targetx-self.startPosX)
        self.movex = math.cos(angle)*self.speed
        self.movey = math.sin(angle)*self.speed

    def bullet_action(self):

        self.pos_x+= self.movex
        self.pos_y+= self.movey

    def bullet_verify(self):
        if (self.pos_y)-(self.startPosY) > self.range or (-self.pos_y)-(-self.startPosY) > self.range:
            self.out_range = True

        if (self.pos_x)-(self.startPosX) > self.range or (-self.pos_x)-(-self.startPosX) > self.range:
            self.out_range = True
    
    def update_frame(self, display):
        self.this_frame+=0.05
        if int(self.this_frame)>=self.sprites.__len__():
            self.this_frame = 0
        self.image = self.sprites[int(self.this_frame)]
        self.image.set_alpha(100)
        display.blit(self.image, (self.pos_x-(self.radius*self.radius), self.pos_y-(self.radius*self.radius)))



      
