class player():
    
    def __init__(self):
        self.rect = None
        self.surface=None
        self.down=0
        self.up=0
        self.speed=1

    def set_surface(surface):
        self.surface=surface
        self.rect=surface.get_rect()
