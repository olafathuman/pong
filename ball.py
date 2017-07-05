###
# Class for the ball
###

class ball():

    def __init__(self):
        self.rect = None
        self.surface = None
        self.current_speed=1
        self.base_speed=1
        self.direction=(0,0)
        self.reset_position=[310,230]

    def set_surface(self,surface):
        self.surface=surface
        self.rect=self.surface.get_rect()

    def set_pos(self,x,y)
        self.rect.topLeft=[x,y]
    
    def vertical_bounce(self):
        self.direction[y]=self.direction[y]*-1
        self.current_speed+=0.1

    def player_bounce(self,y):
        self.direction[0]=self.direction[0]*-1
        self.direction[1]=y

    def reset_ball(self):
        if self.direction[0]==0:
            self.direction[0]=1
        else:
            self.direction=(self.direction[0]*-1,0)
        self.rect.topLeft(self.reset_position)

    def draw(self,surface):
        self.surface.fill((255,255,255))
        surface.blit(self.surface,self.rect)
