import pygame,sys
from pygame.locals import *
from player import player
from ball import ball


class game():

    def __init__(self):

        self.player1=player()
        self.player2=player()
        self.game_ball = ball()
        self.screen= None    
        self.screen_color=(0,0,0)

        self.player1.set_surface(pygame.Surface((20,100)))
        self.player2.set_surface(pygame.Surface((20,100)))
        self.ball.set_surface(pygame.Surface((20,20)))

        self.player1.set_pos(620,190)
        self.player2.set_pos(0,190)
        self.ball.reset_ball()

        self.font = pygame.font.Font(None,50)

        self.score1value=0
        self.score2value=0

        self.score1= None
        self.score2= None

        self.score1rect = None
        self.score2rect = None

        self.set_scores()
        self.set_score_rects()


        self.player_opts=["player","CPU"]
        self.player1_opt=0
        self.player2_opt=0


    def set_scores(self):
        self.set_score1()
        self.set_score2()

    def set_score_rects(self):
        self.score1rect=self.score1.get_rect()
        self.score2rect=self.score2.get_rect()

        self.score1rect.move(480,0)
        self.score2rect.move(160,0)

    def set_score1(self):
        
        self.score1=font.render(str(self.score1value),True,self.score1color,(0,0,0))

    def set_score2(self):
        self.score2=font.render(str(self.score2value),True,self.score2color,(0,0,0))

    def play(self):
        pygame.init()
        self.screen = pygame.displaye.set_mode((640,480))

        while 1:

            self.draw()

    def draw(self):
        
        self.screen.fill(self.screen_color)
        self.player1.draw(self.screen)
        self.player2.draw(self.screen)
        self.ball.draw(self.screen)
        self.set_scores()
        self.screen.blit(self.score1,self.score1pos)
        self.screen.blit(self.score2,self.score2pos)
        
        pygame.display.flip()

    def self.move(self):
        
        self.player1.move()
        self.player2.move()
        self.ball.move()
        if self.ball.rect.colliderect(self.player1.rect):
            if self.player1.direction==1:
                self.ball.player_bounce(1)
            else: 
                self.ball.player_bounce(-1)
        elif self.ball.rect.colliderect(self.player2.rect)
            if self.player2.direction==1:
                self.ball.player_bounce(1)
            else:
                self.ball.player_bounce(-1)
        elif self.ball.rect[1]==0 or self.ball.rect[1]==460:
            self.ball.vertical_bounce()
        elif self.ball.rect[0]==0:
            self.score1value+=1
            self.ball.reset_ball()
        elif self.ball.rect[0]==620:
            self.score2value+=1
            self.ball.reset_ball()
