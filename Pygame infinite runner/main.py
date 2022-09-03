import pygame
import random
from sys import exit

def display_time():
    current_time=pygame.time.get_ticks()//1000-starting_time//1000
    time_font=pygame.font.Font(None,20)
    time_surface=time_font.render("Time elapsed : "+ str(current_time),True,"Black")
    time_rect=time_surface.get_rect(midleft=(30,20))
    screen.blit(time_surface,time_rect)
    
pygame.init()
screen=pygame.display.set_mode((800,480))#pygame.RESIZABLE)#creating a display surface
screen.fill("Green")
pygame.display.set_caption("Infinite runner")#name to be displayed on top of window

clock=pygame.time.Clock()#creating the clock object

icon=pygame.image.load("graphics/lemon.png")
pygame.display.set_icon(icon)

#constants
starting_time=0
score=0
gravity=0
game_running=True


#objects
bg_surface=pygame.Surface((800,300))
bg_surface=pygame.image.load("graphics/Sky.png")

ground_surface=pygame.Surface((800,200))
ground_surface=pygame.image.load("graphics/ground.png")

score_surface = pygame.image.load("graphics/board1.png")
score_rect = score_surface.get_rect(midtop=(750,0))

#coins
coin_surface=pygame.image.load("graphics/coin1.png")
coin_rect=coin_surface.get_rect(bottomleft=(300,300))

#characters
player_surface=pygame.image.load("graphics/player_walk_1.png")
player_rect=player_surface.get_rect(bottomleft=(30,300))

snail_surface=pygame.image.load("graphics/snail1.png")
snail_rect=snail_surface.get_rect(midbottom=(770,300))

player_stand=pygame.image.load("graphics/player_stand.png")
player_stand=pygame.transform.scale2x(player_stand) #Transforming the player_surf
playerstand_rect=player_stand.get_rect(center=(360,260))

#Game over
#game_font=pygame.font.Font(None,50)
#game_font_surface=game_font.render("GAME OVER",False,"black")
score_font= pygame.font.Font (None,20)
#constants
player_rect.y=300

while True:
    for event in pygame.event.get():#to all the possible events
        if event.type==pygame.QUIT:# constant irrespective of the type of window
            pygame.quit()#opposite of pygame.init()
            exit()
            
        if game_running == True:
            if event.type==pygame.KEYDOWN and player_rect.colliderect(snail_rect)==False:
                if event.key==pygame.K_UP and player_rect.bottom>=100:
                    gravity = -15
                elif event.key==pygame.K_DOWN:
                    gravity =10
                if event.key==pygame.K_SPACE:
                    game_running=True
                    
        if game_running == False:
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    game_running=True
                    snail_rect.right=800
                    score=0
                    starting_time=pygame.time.get_ticks()//1000
                    
    if game_running==True:
        #Text
        text=("Score :"+ str(score))
        
        score_text_surface=score_font.render((text),False,"white")
            
        screen.blit(bg_surface,(0,0))
        screen.blit(ground_surface,(0,300))
        screen.blit(coin_surface,coin_rect)
        screen.blit(score_surface,score_rect)
        screen.blit(score_text_surface,(720,10))

        screen.blit(player_surface,player_rect)
        screen.blit(snail_surface,snail_rect)

        display_time()

        #gravity mechanism:
        gravity+=1
        player_rect.y+=gravity

        if player_rect.bottom>=300:
            player_rect.bottom=300
            gravity=0
        
        #collision:
        if player_rect.colliderect(snail_rect):
            game_running=False

        if coin_rect.colliderect(player_rect):
            score+=1
            coin_rect.left=random.randint(97,800)
            #97,275
        
        #opponent motion:
        snail_rect.left-=4
        if snail_rect.left<=0:
            snail_rect.right=800
            #snail_rect.left=random.randint(200,800)

        coin_rect.left-=3
        if coin_rect.left<=0:
            coin_rect.right=800


    if game_running==False:
        pygame.time.wait(360)
        screen.fill("cornflowerblue")
        screen.blit(player_stand,playerstand_rect)
        
        game_font=pygame.font.Font(None,50)
        game_font_surface=game_font.render("Press space to replay",False,"Powderblue")
        screen.blit(game_font_surface,(200,370))

        final_score_surface=game_font.render("Infinite runner score :"+ str(score),False,"Powderblue")
        screen.blit(final_score_surface,(200,70))

    
    pygame.display.update()#for updating the initial display surface
    clock.tick(60)#The while true loop should not run faster than 60 times a sec


'''
    To figure out point
    mousepos=pygame.mouse.get_pos()
    if player_rect.collidepoint(mousepos):
        print(mousepos)
'''
