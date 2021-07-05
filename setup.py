import pygame as client, sys, os, player, time
import collider
import timer
import entity
import item
import spawn
import enemy
import text_builder
import math
import bullet

class Game:

    def __init__(self) -> None:
        pass

    client.init()
    
    drawer = entity.Drawer()
    spawner1 = spawn.Spawner(0.5, 40, 63, 1)
    spawner2 = spawn.Spawner(0.5, 2, 2, 2)
    border_collision = collider.Collider()
    time = client.time.Clock() 
    info = client.display.Info()
    global_width = info.current_w
    global_height = info.current_h
    display = client.display.set_mode((info.current_w, info.current_h))
   
    spawners = entity.Entity.spawners
    enemies = entity.Entity.enemies
    entities = []
    text = entity.Entity().global_words
    items = entity.Entity().items
    bullets = entity.Entity().player_bullets
    enemy_bullets = entity.Entity().enemy_bullets
    player = player.Player(global_width, global_height)

    test_square = item.TestSquare(200,200,60,60)
    timerText = text_builder.clock("comicsansms", "",1000,0,22, (0,0,221))
    #test = enemy.energy_sphere(global_width, global_height) 
    #entity.Entity().enemies.append(test)

    #entity.Entity().spawners.append(spawner1)
    entity.Entity().spawners.append(spawner2)
    entity.Entity().items.append(test_square)
    entity.Entity().global_words.append(timerText)

    #print(client.font.get_fonts())
    run = True
    while(run):
        ticks = time.tick_busy_loop(60)
        display.fill((0,0,0))
        player.alives(client, display, ticks)
        #print(enemy_bullets.__len__())
       
        drawer.draw_spawner(spawners, ticks, global_width, global_height)
        drawer.draw_enemy(enemies, display, client, player.pos_x, player.pos_y, ticks)
        drawer.draw_bullets(bullets, display, client)
        drawer.draw_bullets(enemy_bullets, display, client)
        drawer.draw_items(items, display, client)
        drawer.draw_text(text, display, client)
        border_collision.player_collider(player, enemy_bullets)
        border_collision.limiter(player, global_width, global_height)
        border_collision.item_collider(player, items)
        #print(bullets.__len__())

        for event in client.event.get():
            if event.type== client.QUIT:
                run=False
                client.quit() 
                sys.exit()
        client.display.flip()  


    
   
