import bullet
import timer
import pygame
import entity

class Player(pygame.sprite.Sprite):

    def __init__(self, gamew, gameh):
        self.buffs = []
        self.debuffs = []
        self.inventory = []
        self.clock = timer.Timer()
        self.last_ticks = 0
        self.ticks = 0
        self.attack_speed = 0.15 #seconds
        self.cdOn = False
        self.pos_x = gamew/2
        self.pos_y = gameh - gameh*0.05
        self.color = (0,255,0)
        self.radius = 12
        self.speed = 8
        self.hp = 6
        self.hitbox = 0
        self.mp = 15
        self.alive = True
        self.left = True
        self.right = True
        self.top = True
        self.invencible = False
        self.bottom = True
        self.freezed = False
        self.attack_side = "Top"
        self.bullet_direction = "BottomTop"
        self.direction_vector = [self.pos_x,self.pos_y]

    def draw(self, pygame, display):
        self.hitbox = pygame.draw.circle(display, self.color, (self.pos_x, self.pos_y), self.radius)

    def move(self, pygame):
        key = pygame.key.get_pressed()

        if self.freezed == False:
            if self.left:
                if key[pygame.K_a]:
                    self.pos_x -= self.speed
                   
             
            if self.right:
                if key[pygame.K_d]:
                    self.pos_x += self.speed
                    
         
            if self.top:
                if key[pygame.K_w]:
                    self.pos_y -= self.speed
                   
            
            if self.bottom:
                if key[pygame.K_s]:
                    self.pos_y += self.speed

            if key[pygame.K_LSHIFT]:
                self.speed = 3
            else:
                self.speed = 8
                    

    def direction(self, pygame):
        key = pygame.key.get_pressed()
        if self.freezed == False:
            if key[pygame.K_LEFT]:
                self.attack_side="Left"
            if key[pygame.K_RIGHT]:
                self.attack_side="Right"
            if key[pygame.K_UP]:
                self.attack_side="Top"
            if key[pygame.K_DOWN]:
                self.attack_side="Bot"


    def alives(self, pygame, display, ticks):
        if self.alive:
            #redraw
            #print(self.hp)
            self.draw(pygame, display)

            #verificar cooldowns

            #attack speed
            self.cdOn = self.clock.countdown(self.cdOn, ticks, self.attack_speed)

            #verificar movimento
            self.move(pygame)

            #verificar para onde está olhando
            self.direction(pygame)

            #verificar ataque
            self.attack(pygame)    



        else:
            return -1

    def attack(self, pygame):
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
              if self.cdOn == False:
                    self.check_attack_side()
                    pygame.mixer.Sound('./sounds/default_bullet.mp3').play()
                    bullet_object = bullet.Soul_Bullet(self.direction_vector[0], self.direction_vector[1],self.bullet_direction)
                    entity.Entity().player_bullets.append(bullet_object)
                   

    def check_attack_side(self):
        if self.attack_side == "Left":
            self.direction_vector[0] = self.pos_x-self.radius-(self.radius/2)
            self.direction_vector[1] = self.pos_y
            self.bullet_direction = "RightLeft"

        if self.attack_side  == "Right":
            self.direction_vector[0] = self.pos_x+self.radius+(self.radius/2)
            self.direction_vector[1] = self.pos_y
            self.bullet_direction = "LeftRight"

        if self.attack_side  == "Top":
            self.direction_vector[0] = self.pos_x
            self.direction_vector[1] = self.pos_y-self.radius-(self.radius/2)
            self.bullet_direction = "BottomTop"

        if self.attack_side  == "Bot":
            self.direction_vector[0] = self.pos_x
            self.direction_vector[1] = self.pos_y+self.radius+(self.radius/2)
            self.bullet_direction = "TopBottom"
        
    def dies(self):
        self.color = (255,0,0)
        self.hp-=1
        






            
            





        
        



