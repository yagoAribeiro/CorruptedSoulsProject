import random
import enemy
import timer
import entity

class Spawner():
    def __init__(self, cooldown_per_enemy, min_enemy_per_wave, max_enemy_per_wave, minion_id):
       self.clock = timer.Timer()
       self.wave_clock = timer.Timer()
       self.cdOn = False
       self.minions_in_wave = 0
       self.finished = False
       self.minionid = minion_id
       self.cooldown_seconds = cooldown_per_enemy
       self.rng_wave_count = random.randint(min_enemy_per_wave, max_enemy_per_wave)

    def spawner_spawn(self, ticks, display_w, display_h): 
        self.cdOn = self.clock.countdown(self.cdOn, ticks, self.cooldown_seconds)
        # print(self.clock.ticks)

        if self.minions_in_wave>= self.rng_wave_count:
           self.finished = True

        if self.cdOn == False:
            if self.minionid == 1:
               entity.Entity.enemies.append(enemy.Harpy(display_w, display_h))
            if self.minionid == 2:
               entity.Entity.enemies.append(enemy.Big_Harpy(display_w, display_h))
            self.minions_in_wave += 1
            self.cdOn = True


