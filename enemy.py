import pygame
import bullet
import entity
import timer
import random
import math

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        self.hp = 0
        self.cooldown = 0
        self.range = 0
        self.clock = timer.Timer()
        self.attack_rate = 0
        self.sprites = []
        self.freezed = False
        self.alive = True
        self.hitbox = 0
        self.typebox = "none"
        self.width = 0
        self.height = 0
        self.speed = 0
        self.pos_x = 0
        self.pos_y = 0

class Harpy(Enemy):
    def __init__(self, screen_w, screen_h):
        Enemy.__init__(self)
        self.name = "Harpia"
        self.id = 0
        self.side = None
        self.rng = random.randint(0,1)

        if self.rng == 0:
            self.side = "LEFT"

        elif self.rng == 1:
            self.side = "RIGHT"
        self.width = 30
        self.height = 30
        self.speed = 7

        if self.side =="LEFT":
            self.startx = -200
            self.pos_x = self.startx
        
        elif self.side == "RIGHT":
            self.startx = screen_w+200
            self.pos_x = self.startx

        self.starty = (screen_h*0.30)-random.randint(0, 150)
        self.pos_y = self.starty
        self.hp = 140
        self.typebox = "Square"
        self.range = 1800
        self.cooldown = False
        self.attack_rate = 0.4 #seconds
       

    def alives(self, player_x, player_y, ticks):
        if self.alive:
            self.move()
            self.cooldown = self.clock.countdown(self.cooldown, ticks, self.attack_rate)
            self.attack(player_x, player_y)
            #print(player_x, player_y)
            #print(self.startx)

    def move(self):
        if self.side == "LEFT":
            self.pos_x += self.speed

        if self.side == "RIGHT":
            self.pos_x -= self.speed

        if (self.pos_x)-(self.startx) >=self.range or (-self.pos_x)-(-self.startx)>=self.range:
            self.alive = False

    def attack(self, target_x, target_y):
        if self.cooldown == False:
            entity.Entity.enemy_bullets.append(bullet.Normal_Bullet(self.pos_x, self.pos_y, target_x, target_y))


class Big_Harpy(Enemy):
    def __init__(self, screen_w, screen_h):
        Enemy.__init__(self)
        self.name = "Grande Harpia"
        self.id = 2
        self.rng = random.randint(40, screen_w)
        self.startx = self.rng
        self.pos_x = self.startx
        self.starty = -100
        self.pos_y = self.starty
        self.hp = 300
        self.width = 60
        self.height = 60
        self.typebox = "Square"
        self.cooldown = False
        self.attack_rate = 2.5 #seconds
        self.speed = 4
        self.newx = 0
        self.newy = 0
        self.hasdestiny = False
        self.globalw = screen_w
        self.globalh = screen_h
        self.angle = 0 
        self.enraged = False
        self.attacks = 0
        self.second_attacks = 0
        self.second_angle = 0
    
    def move(self):
        if self.hasdestiny == False:
            randomposx = random.randint(100, self.globalw-100)
            randomposy = random.randint(100, self.globalh-100)
            distance = math.hypot(self.pos_x-randomposx, self.pos_y-randomposy)
            self.newx = randomposx
            self.newy = randomposy
            self.angle = math.atan2(self.newy - self.pos_y, self.newx - self.pos_x)
            self.hasdestiny = True
        else:
            distance = math.hypot(self.pos_x-self.newx, self.pos_y-self.newy)
            if distance>self.speed+1:
                self.pos_x += math.cos(self.angle)*self.speed
                self.pos_y += math.sin(self.angle)*self.speed
            else: 
                self.hasdestiny = False
            
    
    def alives(self, player_x, player_y, ticks):
        if self.alive:
            self.move()
            self.cooldown = self.clock.countdown(self.cooldown, ticks, self.attack_rate)
            self.attack(player_x, player_y)

    def attack(self, targetx, targety):
        if self.cooldown == False:     

            if self.attacks==4:
                self.attacks = 0
                self.enraged = True
                self.attack_rate = 0.35
                self.speed *= 2 

            if self.second_attacks == 7: 
                self.second_attacks = 0
                self.enraged = False
                self.speed = 4
                self.attack_rate = 2.5

           # i=0
           # while(i<15):
            #    if(i%3 == 0):
             #       entity.Entity.enemy_bullets.append(bullet.Normal_Bullet(self.pos_x, self.pos_y, targetx+(i*15), targety+(i*15)))
              #  i+= 1

            #while(self.second_angle<360):
                #self.second_angle+=7
             #   x = (math.cos(self.second_angle) * 50) + (self.pos_x+(self.width/2))
              #  y = (math.sin(self.second_angle) * 50) + (self.pos_y+(self.height/2))
               # 
                #entity.Entity.enemy_bullets.append(bullet.Normal_Bullet(x, y, (math.cos(self.second_angle) * 1000) + self.pos_x, (math.sin(self.second_angle) * 1000) + self.pos_y))
            entity.Entity.enemy_bullets.append(bullet.Normal_Bullet(self.pos_x, self.pos_y, targetx, targety))
            entity.Entity.enemy_bullets.append(bullet.Normal_Bullet(self.pos_x, self.pos_y, targetx+100, targety+50))
            entity.Entity.enemy_bullets.append(bullet.Normal_Bullet(self.pos_x, self.pos_y, targetx-100, targety+50))
            self.second_angle = 0
            if self.enraged:
                self.second_attacks+=1
            else: 
                self.attacks+=1



        



            
            
        
            

        



        
        





    
