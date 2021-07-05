class Item():

    def __init__(self) -> None:
        pass

    def apply(self):
        pass

class TestSquare(Item):

    def __init__(self, startposX, startposY, startWidth, startHeight):
        self.name = "6666666666"
        self.desc = "No"
        self.hitbox = None
        self.width = startWidth
        self.height = startHeight
        self.sprites = []
        self.pos_x = startposX
        self.pos_y = startposY
        self.dropped = True
    