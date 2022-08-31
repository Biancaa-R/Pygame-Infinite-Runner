import pygame
import random
from sys import exit
pygame.init()
screen=pygame.display.set_mode((800,480))#pygame.RESIZABLE)#creating a display surface
screen.fill("Green")
pygame.display.set_caption("Infinite runner")#name to be displayed on top of window

clock=pygame.time.Clock()#creating the clock object

icon=pygame.image.load("graphics/lemon.png")
pygame.display.set_icon(icon)

#objects
bg_surface=pygame.Surface((800,300))
bg_surface=pygame.image.load("graphics/Sky.png")

ground_surface=pygame.Surface((800,200))
ground_surface=pygame.image.load("graphics/ground.png")

#characters
player_surface=pygame.image.load("graphics/player_stand.png")
player_rect=player_surface.get_rect(bottomleft=(10,300))

snail_surface=pygame.image.load("graphics/snail1.png")
snail_rect=snail_surface.get_rect(midbottom=(770,300))

#constants
gravity=0
player_rect.y=300

while True:
    for event in pygame.event.get():#to all the possible events
        if event.type==pygame.QUIT:# constant irrespective of the type of window
            pygame.quit()#opposite of pygame.init()
            exit()
        if event.type==pygame.KEYDOWN: #and player_rect.colliderect(snail_rect)==False:
            if event.key==pygame.K_UP and player_rect.bottom>=100:
                gravity = -15
            elif event.key==pygame.K_DOWN:
                gravity =10
            
    screen.blit(bg_surface,(0,0))
    screen.blit(ground_surface,(0,300))

    screen.blit(player_surface,player_rect)
    screen.blit(snail_surface,snail_rect)

    #gravity mechanism:
    gravity+=1
    player_rect.y+=gravity

    if player_rect.bottom>=300:
        player_rect.bottom=300
        gravity=0

    #opponent motion:
    snail_rect.left-=2
    if snail_rect.left<=0:
        snail_rect.right=800
        #snail_rect.left=random.randint(200,800)

    pygame.display.update()#for updating the initial display surface
    clock.tick(60)#The while true loop should not run faster than 60 times a sec

       
