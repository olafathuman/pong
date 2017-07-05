import pygame,sys
from pygame.locals import *


pygame.init()
screen =pygame.display.set_mode((640,480))

player1 = pygame.Surface((20,100))
player1pos = player1.get_rect()
player1pos.topleft=[620,190]
                             
player2 = pygame.Surface((20,100))
player2pos = player2.get_rect()
player2pos.topleft=[0,190]

ball = pygame.Surface((20,20))
ballpos = ball.get_rect()
ballpos.topleft=[310,230]
ballSpeed = 1
baseSpeed = 1


up=0
down=0

up2=0
down2=0

ballmove=[-1*baseSpeed,0]

font = pygame.font.Font(None,50)

score1value=0
score1=font.render(str(score1value),True,(255,255,255),(0,0,0))
score1pos=score1.get_rect()
score1pos=score1pos.move(480,0)

score2value=0
score2=font.render(str(score2value),True,(255,255,255),(0,0,0))
score2pos=score2.get_rect()
score2pos=score2pos.move(160,0)


         
while 1:
    for event in pygame.event.get():
       if(event.type == pygame.QUIT):
           sys.exit()
       elif event.type == pygame.KEYDOWN:
               if event.key==K_UP:
                   up=1
               elif event.key == K_DOWN:
                   down=1
               elif event.key == K_w:
                   up2=1
               elif event.key == K_s:
                   down2=1
       elif event.type == pygame.KEYUP:
               if event.key==K_UP:
                   up=0
               elif event.key == K_DOWN:
                   down=0
               elif event.key== K_w:
                   up2=0
               elif event.key == K_s:
                   down2=0
               elif event.key == K_ESCAPE:
                   sys.exit()
                   

    if up==1:
        if player1pos[1]!=0:
            player1pos = player1pos.move((0,-1))
    if down==1:
        if player1pos[1]!=380:
            player1pos = player1pos.move((0,1))
    if up2==1:
        if player2pos[1]!=0:
            player2pos = player2pos.move((0,-1))
    if down2==1:
        if player2pos[1]!=380:
            player2pos = player2pos.move((0,1))

    if ballpos.colliderect(player1pos):
        ballSpeed=ballSpeed + 0.01
        if ballpos[1]<player1pos[1]+30:
            ballmove[1]=-1*ballSpeed
            ballpos.move(0,-1*ballSpeed)
        elif ballpos[1]>player1pos[1]+70:
            ballmove[1]=1*ballSpeed
            ballpos.move(0,1*ballSpeed)
        ballmove[0] = ballmove[0]*-1
    if ballpos.colliderect(player2pos):
        ballSpeed=ballSpeed+0.01
        if ballpos[1]<player2pos[1]+30:
            ballmove[1]=-1*ballSpeed
        elif ballpos[1]>player2pos[1]+70:
            ballmove[1]=1*ballSpeed
        ballmove[0] = ballmove[0]*-1    
    if ballpos[1]==0 or ballpos[1]==460:
        ballmove[1]*=-1*ballSpeed

    if ballpos[0]==0:
        score1value+=1
        ballpos.topleft=[310,230]
        player1pos.topleft=[620,190]
        player2pos.topleft=[0,190]
        ballSpeed = baseSpeed
        ballmove[0] = ballmove[0]*-1
        ballmove[1] = 0

    if ballpos[0]==620:
        ballSpeed = baseSpeed
        score2value+=1
        ballpos.topleft=[310,230]
        player1pos.topleft=[620,190]
        player2pos.topleft=[0,190]
        ballmove[0] = ballmove[0]*-1
        ballmove[1] = 0
        
    score1=font.render(str(score1value),True,(255,255,255),(0,0,0))
    score2=font.render(str(score2value),True,(255,255,255),(0,0,0))
    ballpos = ballpos.move(ballmove)
    screen.fill((0,0,0))
    player1.fill((255,255,255))
    player2.fill((255,255,255))
    ball.fill((255,255,255))
    screen.blit(player1,player1pos)
    screen.blit(player2,player2pos)
    screen.blit(ball,ballpos)
    screen.blit(score1,score1pos)
    screen.blit(score2,score2pos)
    pygame.display.flip()
    
