from text_builder import clock
import timer

class Entity:
     player_bullets = []
     enemy_bullets = []
     global_words = []
     enemies = []
     items = []
     spawners = []

     def __init__(self):
        pass


class Drawer:

    def __init__(self):
        self.timer_object = timer.Timer()

    def draw_enemy(self, enemy_array, display, pygame, player_x, player_y, ticks):
        if enemy_array.__len__()>0:
            for enemy in enemy_array:
                if enemy.alive:
                    if enemy.typebox == "Square":
                        enemy.alives(player_x, player_y, ticks)
                        enemy.hitbox = pygame.draw.rect(display, (255,0,0), (enemy.pos_x, enemy.pos_y, enemy.width, enemy.height))
                else: 
                    enemy_array.remove(enemy)

    def draw_bullets(self, bullet_array, display, pygame):
        if bullet_array.__len__()>0:
            self.verify_dies(bullet_array)
            for bullet in bullet_array:
                #print(bullet_array.__len__())
                if bullet.typebox == "Circle":
                    bullet.bullet_action()
                    surf = pygame.Surface((bullet.radius*2, bullet.radius*2))
                    bullet.hitbox = pygame.draw.circle(surf, (100, 128, 255, 0), (bullet.pos_x, bullet.pos_y), bullet.radius)
                    bullet.update_frame(display)

    def draw_items(self, item_array, display, pygame):
        if item_array.__len__()>0:
                for item in item_array:
                    if item.dropped:
                            item.hitbox = pygame.draw.rect(display, (0,255,0), (item.pos_x, item.pos_y, item.width, item.height))
                    else:
                        item_array.remove(item)

    def draw_text(self, text_array, display, pygame):
         if text_array.__len__()>0:
             for text in text_array:
                 if text.exists:
                     if text.type=="text_item":
                        text.animation()
                        font = pygame.font.SysFont(text.font, text.size)
                        final_text = font.render(text.text_object, 1, text.color)
                        #print(str(text.pos_x)+","+str(text.pos_y))
                        display.blit(final_text, (text.pos_x, text.pos_y))

                     elif text.type=="text_clock": 
                        text.text_object = self.timer_object.clock(pygame.time.get_ticks(),False, text.text_object)
                        font = pygame.font.SysFont(text.font, text.size)
                        final_text = font.render(text.text_object, 1, text.color)
                        display.blit(final_text, (text.pos_x, text.pos_y))
                 else:
                     text_array.remove(text)

    def draw_spawner(self, spawn_array, ticks, globalw, globalh):
        if spawn_array.__len__()>0:
            for spawn in spawn_array:
                if spawn.finished!=True:
                    spawn.spawner_spawn(ticks, globalw, globalh)
                else:
                    spawn_array.remove(spawn)


    def verify_dies(self, bullet_array):
        for bullet in bullet_array:
            bullet.bullet_verify()
            if bullet.out_range:
                bullet_array.remove(bullet)

        


    



