import pygame,sys
from pygame.locals import *
from player import player
from ball import ball


class game():

    def __init__(self):

        
        self.phase=0
        
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
        
        self.choice1_rect=None
        self.choice2_rect=None
        
        self.playerwin=None
        self.playerwin_rect=None

        self.arrow_left=pygame.image.load("images/left_arrow.bmp")
        self.arrow_right=pygame.image.load("images/right_arrow.bmp")
        self.A=pygame.image.load("images/A.bmp")
        self.D=pygame.image.load("images/D.bmp")


        self.arrow_left.set_colorkey((0,255,0))
        self.arrow_right.set_colorkey((0,255,0))
        self.A.set_colorkey((0,255,0))
        self.D.set_colorkey((0,255,0))

        self.arrow_left_rect=self.arrow_left.get_rect()
        self.arrow_right_rect=self.arrow_right.get_rect()
        self.A_rect=self.A.get_rect()
        self.D_rect=self.D.get_rect()


        self.arrow_left_rect = self.arrow_left_rect.move(350,250)
        self.arrow_right_rect = self.arrow_right_rect.move(500,250)
        self.A_rect=self.A_rect.move(50,250)
        self.D_rect=self.D_rect.move(200,250)

        self.score1color = (255,255,255)
        self.score2color = (255,255,255)
       

        self.player_opts=["player","CPU"]
        self.player1_opt=0
        self.player2_opt=1


    def set_scores(self):
        self.set_score1()
        self.set_score2()
    
    def set_opts(self):


        self.choice1=self.font.render(self.player_opts[self.player1_opt],True,(255,255,255),(0,0,0))
        
        self.choice2=self.font.render(self.player_opts[self.player2_opt],True,(255,255,255),(0,0,0))

        
        
        
        

    def set_opt_rects(self):

        self.choice1rect=self.choice1.get_rect()
        self.choice2rect=self.choice2.get_rect()           
        
        self.choice1rect=self.choice1rect.move(400,190)        
        self.choice2rect=self.choice2rect.move(100,190)        

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
        self.set_opts()
        self.set_opt_rects()

        while 1:
            self.handle_events() 
            self.move()
            self.draw()
            if self.score1value>9:
                self.phase=3
            elif self.score2value>9:
                self.phase=2
            

    def draw(self):
       
        self.screen.fill(self.screen_color)
        if self.phase==0:
            self.screen.blit(self.A,self.A_rect) 
            self.screen.blit(self.D,self.D_rect)
            self.screen.blit(self.arrow_left,self.arrow_left_rect)
            self.screen.blit(self.arrow_right,self.arrow_right_rect)

            self.screen.blit(self.choice1,self.choice1rect)
            self.screen.blit(self.choice2,self.choice2rect) 
        
        elif self.phase==1:
            self.player1.draw(self.screen)
            self.player2.draw(self.screen)
            self.ball.draw(self.screen)
            self.set_scores()
            self.screen.blit(self.score1,self.score1rect)
            self.screen.blit(self.score2,self.score2rect)
        
        elif self.phase==2:
            self.playerwin=self.font.render("Left "+self.player_opts[self.player2_opt]+" Wins!",True,(255,255,255),(0,0,0))
            self.playerwin_rect=self.playerwin.get_rect()
            self.playerwin_rect=self.playerwin_rect.move(220,220)
            self.screen.blit(self.playerwin,self.playerwin_rect)
        
        elif self.phase==3:
            self.playerwin=self.font.render("Right "+self.player_opts[self.player1_opt]+" Wins!",True,(255,255,255),(0,0,0))
            self.playerwin_rect=self.playerwin.get_rect()
            self.playerwin_rect=self.playerwin_rect.move(200,220)
            self.screen.blit(self.playerwin,self.playerwin_rect)
        
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
            if self.phase==1:
                
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

            elif self.phase==0:
                if(event.type==pygame.QUIT):
                    sys.exit()
                elif event.type== pygame.KEYDOWN:
                    if event.key==K_LEFT or event.key==K_RIGHT:
                        if self.player1_opt==1:
                            self.player1_opt=0
                        else:
                            self.player1_opt=1
                        self.set_opts()
                    elif event.key==K_a or event.key==K_d:
                        if self.player2_opt==1:
                            self.player2_opt=0
                        else:
                            self.player2_opt=1
                        self.set_opts()
                    elif event.key==K_ESCAPE:
                        sys.exit()
                    elif event.key==K_RETURN or event.key==K_SPACE:
                        self.phase=1
                        self.reset()
            elif self.phase>1:
                if(event.type==pygame.QUIT):
                    sys.exit
                elif event.type==pygame.KEYDOWN:
                    if event.key==K_RETURN or event.key==K_SPACE:
                        self.phase=0
                        self.reset()
                    elif event.key==K_ESCAPE:
                        sys.exit()


    def reset_players(self):
        self.player1.reset_paddle()
        self.player2.reset_paddle()

    def reset(self):
        self.score1value=0
        self.score2value=0
        self.reset_players()
        self.ball.reset_ball()
