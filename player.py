###
# Class for the players
###

class player():
    
    def __init__(self):
        self.rect = None
        self.surface=None
        self.direction=0
        self.speed=1
        self.color=(255,255,255)

    def set_surface(self,surface):
        self.surface=surface
        self.rect=self.surface.get_rect()

    def set_pos(self,x,y):
        self.rect.topleft=[x,y]

    def set_color(self,r,g,b):
        self.color=(r,g,b)

    def draw(self,surface):
        self.surface.fill(self.color)
        surface.blit(self.surface,self.rect)

    def move(self):
        if self.rect[1]>0 and self.direction==-1:
            self.rect = self.rect.move(0,self.direction*self.speed)
        elif self.rect[1]<380 and self.direction==1:
            self.rect = self.rect.move(0,self.direction*self.speed)

    def ai_move(self,ball):
        if ball[1]<self.rect.centery:
            self.direction=-1
        elif ball[1]>self.rect.centery:
            self.direction=1
        else:
            self.direction=0
