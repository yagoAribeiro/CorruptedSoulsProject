import math
import entity
import text_builder

class Collider:

    def __init__(self) -> None:
        pass

    

    def limiter(self, player, gw, gh):

        if player.pos_x-player.radius<=0:
            player.left = False
        else:
            player.left = True

        if player.pos_y-player.radius<=0:
            player.top = False
        else:
            player.top = True

        if player.pos_x+player.radius>=gw:
            player.right = False
        else:
            player.right = True
        
        if player.pos_y+player.radius>=gh:
            player.bottom = False
        else:
            player.bottom = True

    def item_collider(self, player, item_vector):

        if item_vector.__len__()>0:

            for item in item_vector:

                if (player.pos_x+player.radius)>=item.hitbox.left and (player.pos_x-player.radius)<=item.hitbox.right and (player.pos_y+player.radius)>=item.hitbox.top and (player.pos_y-player.radius)<=item.hitbox.bottom: 
                    player.inventory.append(item)
                    object_text = text_builder.item_text("monospace", "+ "+item.name, (item.hitbox.left+item.width/2), (item.hitbox.top+item.height*0.05),12, (170,170,170))
                    entity.Entity().global_words.append(object_text)
                    item.dropped = False
                else:
                    item.color = (0,255,0)

    def player_collider(self, player, bullet_vector):

        if bullet_vector.__len__()>0:
            for bullet in bullet_vector:
                distance = math.hypot(player.pos_x-bullet.pos_x, player.pos_y-bullet.pos_y)
                if (distance<=player.radius+bullet.radius):
                    player.dies()