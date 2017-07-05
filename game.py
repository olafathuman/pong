import pygame,sys
from pygame.locals import *
from player import player
from ball import ball


class game():

    def __init__(self):

        self.player1=player()
        self.player2=player()
        self.ball = ball()
        self.screen= None    
        self.screen_color=(0,0,0)

        self.player1.set_surface(pygame.Surface((20,100)))
        self.player2.set_surface(pygame.Surface((20,100)))
        self.ball.set_surface(pygame.Surface((20,20)))

        self.player1.set_pos(620,190)
        self.player2.set_pos(0,190)
        self.ball.reset_ball()

        self.font=None
        self.score1value=0
        self.score2value=0

        self.score1= None
        self.score2= None

        self.score1rect = None
        self.score2rect = None
        
        self.choice1=None
        self.choice2=None
        
        self.choice1rect=None
        self.choice2rect=None

        self.score1color = (255,255,255)
        self.score2color = (255,255,255)
       

        self.player_opts=["player","CPU"]
        self.player1_opt=0
        self.player2_opt=1


    def set_scores(self):
        self.set_score1()
        self.set_score2()

    def set_score_rects(self):
        self.score1rect=self.score1.get_rect()
        self.score2rect=self.score2.get_rect()

        self.score1rect=self.score1rect.move(480,0)
        self.score2rect=self.score2rect.move(160,0)

    def set_score1(self):
        
        self.score1=self.font.render(str(self.score1value),True,self.score1color,(0,0,0))

    def set_score2(self):
        self.score2=self.font.render(str(self.score2value),True,self.score2color,(0,0,0))

    def play(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640,480))
        
        self.font = pygame.font.Font(None,50)
        self.set_scores()
        self.set_score_rects()

        while 1:
            self.handle_events() 
            self.move()
            self.draw()
            

    def draw(self):
        
        self.screen.fill(self.screen_color)
        self.player1.draw(self.screen)
        self.player2.draw(self.screen)
        self.ball.draw(self.screen)
        self.set_scores()
        self.screen.blit(self.score1,self.score1rect)
        self.screen.blit(self.score2,self.score2rect)
        
        pygame.display.flip()

    def move(self):
        if self.player1_opt==1:
            self.player1.ai_move(self.ball.rect)
        if self.player2_opt==1:
            self.player2.ai_move(self.ball.rect)
        self.player1.move()
        self.player2.move()
        self.ball.move()
        if self.ball.rect.colliderect(self.player1.rect):
            if self.player1.direction==1:
                self.ball.player_bounce(1)
            else: 
                self.ball.player_bounce(-1)
        elif self.ball.rect.colliderect(self.player2.rect):
            if self.player2.direction==1:
                self.ball.player_bounce(1)
            else:
                self.ball.player_bounce(-1)
        elif self.ball.rect[1]<=0:
            self.ball.rect[1]=1
            self.ball.vertical_bounce()
        elif self.ball.rect[1]>=460:
            self.ball.rect[1]=459
            self.ball.vertical_bounce()
        elif self.ball.rect[0]<=0:
            self.score1value+=1
            self.ball.reset_ball()
            self.reset_players()
        elif self.ball.rect[0]>=620:
            self.score2value+=1
            self.ball.reset_ball()
            self.reset_players()

    def handle_events(self):

        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
               sys.exit()
            elif event.type == pygame.KEYDOWN:
                if self.player1_opt==0:
                    if event.key==K_UP:
                        self.player1.direction=-1
                    elif event.key == K_DOWN:
                        self.player1.direction=1
                if self.player2_opt==0:
                    if event.key == K_w:
                        self.player2.direction=-1
                    if event.key == K_s:
                        self.player2.direction=1
            elif event.type == pygame.KEYUP:
                
                if self.player1_opt==0:
                    if event.key==K_UP:
                        self.player1.direction=0
                    elif event.key == K_DOWN:
                        self.player1.direction=0
                if self.player2_opt==0:
                    if event.key== K_w:
                        self.player2.direction=0
                    if event.key == K_s:
                        self.player2.direction=0
                if event.key == K_ESCAPE:
                    sys.exit()

    def reset_players(self):
        self.player1.reset_paddle()
        self.player2.reset_paddle()
