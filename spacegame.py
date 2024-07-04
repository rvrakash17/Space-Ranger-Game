
import pygame
from pygame.locals import *
import random

size = width,height =(1200,600)
space_w = int(width/7)
startind = False

speed = 10
increase = 0
grade = 0
pygame.init()
run = True

screen = pygame.display.set_mode(size)

pygame.display.set_caption("Gameee")

spacebg = pygame.image.load('Space BG.png')
spacebg_loc = spacebg.get_rect()

title = pygame.image.load('Gametitle.png')
title_loc = title.get_rect()
title_loc.center = width/2,height/1.5

gamestart = pygame.image.load('Start Msg.png')
gamestart_loc = gamestart.get_rect()
gamestart_loc.center = width/2,height/2

spaceship = pygame.image.load('Spaceship.png')
spaceship_loc = spaceship.get_rect()
spaceship_loc.center = space_w,height*.8

metor = pygame.image.load('Meteor.png')
metor_loc = metor.get_rect()
metor_loc.center = space_w,height*.1

gameover = pygame.image.load('Game Over.png')
gameover_loc = gameover.get_rect()
gameover_loc.center = width/2,height/2

white = (255,255,255)
font = pygame.font.SysFont("Arial",36)
score = str(grade)
scoretxt = font.render("Score :",True,white)
scoretxt_loc = scoretxt.get_rect()
score = font.render(score,True,white)
score_loc = score.get_rect()
score_loc.center = width*.11,height*0.04
scoretxt_loc.center = width*.05,height*0.04


screen.blit(spacebg,spacebg_loc)
screen.blit(gamestart,gamestart_loc)
screen.blit(spaceship,spaceship_loc)
screen.blit(metor,metor_loc)
screen.blit(title,title_loc)
screen.blit(score,score_loc)
screen.blit(scoretxt,scoretxt_loc)

pygame.display.update()



while run:
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
        if event.type == KEYDOWN:
            if event.key == K_s:
                startind = True


        while startind:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key in [K_a,K_LEFT]:
                        spaceship_loc = spaceship_loc.move(-space_w,0)
                    if event.key in [K_d,K_RIGHT]:
                        spaceship_loc = spaceship_loc.move(space_w,0)
                if event.type == QUIT:
                    run = False
                    startind = False
            metor_loc[1] = metor_loc[1]+speed
        
            if metor_loc[1] > height:
                metor_loc.center = space_w * random.randint(1,6),-100
                increase = increase + 1
                grade = grade+1
                if increase == 10:
                    speed = speed + 10
                    increase = 0
            score = str(grade)
   
            scoretxt = font.render("Score :",True,white)
            scoretxt_loc = scoretxt.get_rect()
            score = font.render(score,True,white)
            score_loc = score.get_rect()
            score_loc.center = width*.11,height*0.04
            scoretxt_loc.center = width*.05,height*0.04    
            screen.blit(spacebg,spacebg_loc)
            screen.blit(spaceship,spaceship_loc)
            screen.blit(metor,metor_loc)
            screen.blit(title,title_loc)
            screen.blit(score,score_loc)
            screen.blit(scoretxt,scoretxt_loc)

            if spaceship_loc[0] == metor_loc[0] and spaceship_loc[1] < metor_loc[1]+175 and spaceship_loc[1] > metor_loc[1]-175:
                screen.blit(gameover,gameover_loc)
                pygame.display.update()
                startind = False
            pygame.display.update()    
    
        if event.type == KEYDOWN:
            if event.key == K_r:
                startind = True
                speed = 10
                increase = 0
                grade = 0
                spaceship_loc.center = space_w,height*.8
                metor_loc.center = space_w,height*.1
                screen.blit(spacebg,spacebg_loc)
                screen.blit(spaceship,spaceship_loc)
                screen.blit(metor,metor_loc)
                screen.blit(title,title_loc)
                pygame.display.update()


pygame.quit()
