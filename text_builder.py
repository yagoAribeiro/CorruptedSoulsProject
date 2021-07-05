class Text():

    def __init__(self) -> None:
        pass
       
    def animation(self) -> None:
        pass


class item_text(Text):

    def __init__(self, font, text, posx, posy, size, color):
        self.font = font
        self.size = size
        self.text_object = text
        self.pos_x = posx
        self.pos_y = posy
        self.nextPosX = 0
        self.nextPosY = 0
        self.prevPosX = posx
        self.prevPosY = posy
        self.exists = True
        self.color = color
        self.type = "text_item"
    
    def animation(self):
        self.nextPosY = self.prevPosY-100

        if (self.pos_y>=self.nextPosY):
            self.pos_y-=1.75
        else:
            self.exists = False

class clock(Text):

    def __init__(self, font, text, posx, posy, size, color):
        self.font = font
        self.size = size
        self.text_object = text
        self.text_color = None
        self.pos_x = posx
        self.pos_y = posy
        self.exists = True
        self.color = color
        self.type = "text_clock"

        