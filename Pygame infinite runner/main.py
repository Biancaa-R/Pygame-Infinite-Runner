import pygame
import random
from sys import exit

def display_time():
    
    current_time=pygame.time.get_ticks()//1000 -starting_time
    time_font=pygame.font.Font(None,20)
    time_surface=time_font.render("Time elapsed : "+ str(current_time),True,"Black")
    time_rect=time_surface.get_rect(midleft=(30,20))
    screen.blit(time_surface,time_rect)
    return current_time

def obstracle_movement(obstracle_rect_list):
    if (obstracle_rect_list):
        for obstracle_rect in obstracle_rect_list:
            obstracle_rect.left-=4
            if obstracle_rect.left in range((snail_rect.left)-60,(snail_rect.left)+60):
                obstracle_rect_list.remove(obstracle_rect)
            if obstracle_rect.bottom==300:
                screen.blit(snail_surface,obstracle_rect)
            if obstracle_rect.bottom==200:
                screen.blit(fly_surface,obstracle_rect)
                

            #if obstracle_rect.colliderect(player_rect):
                #game_running=False

        obsracle_rect_list=[obstracle for obstracle in obstracle_rect_list if obstracle.x>-100]
        return list(obstracle_rect_list)
    else:
        return []
            
def collision(player_rect,obstracle_rect_list):
    if obstracle_rect_list:
        for obstracle_rect in obstracle_rect_list:
            if player_rect.colliderect(obstracle_rect):
                settings=False
                return False
        return True
    else:
        return True

def player_animation():
    global player_surface,player_index
    if player_rect.bottom<300:
        player_surface=player_jump
    else:
        player_index+=0.1
        
        if player_index>=len(player_walk):
            player_index=0
        player_surface=player_walk[int(player_index)]

def coin_animation():
    global coin_surface,coin_index
    coin_index+=0.1
    if coin_index>=len(coin_spin):
        coin_index=0
    coin_surface=coin_spin[int(coin_index)]

def primary_snail_animation():
    global snail_surface,snail_index
    snail_index+=0.1
    if snail_index>=len(snail):
        snail_index=0
    snail_surface=snail[int(snail_index)]

        
pygame.init()
screen=pygame.display.set_mode((800,480))#pygame.RESIZABLE)#creating a display surface
screen.fill("Green")
pygame.display.set_caption("Infinite runner")#name to be displayed on top of window

clock=pygame.time.Clock()#creating the clock object

icon=pygame.image.load("graphics/lemon.png")
pygame.display.set_icon(icon)

#constants
obstracle_rect_list=[]
starting_time=0
time=0
score=0
gravity=0
game_running=False
global settings
settings=False
global game_level
game_level=0
global colour
colour="aqua"

#objects

sky1=pygame.image.load("graphics/Sky.png")
sky2=pygame.image.load("graphics/Sky1.jpg")
sky3=pygame.image.load("graphics/Sky2.png")
sky4=pygame.image.load("graphics/Sky3.jpg")
sky5=pygame.image.load("graphics/Sky4.jpg")
sky6=pygame.image.load("graphics/Sky5.png")
sky7=pygame.image.load("graphics/Sky6.jpg")
sky8=pygame.image.load("graphics/Sky7.jpg")
sky9=pygame.image.load("graphics/Sky8.jpg")
sky10=pygame.image.load("graphics/Sky9.png")
sky11=pygame.image.load("graphics/Sky11.jpg")
sky12=pygame.image.load("graphics/Sky12.jpg")
sky13=pygame.image.load("graphics/Sky13.jpg")
sky=[sky1,sky2,sky3,sky4,sky5,sky6,sky7,sky8,sky9,sky10,sky11,sky12,sky13]
if game_level>12:
    game_level=0
    
bg_surface=pygame.Surface((800,300))
bg_surface=sky[game_level]
ground_surface=pygame.Surface((800,200))
ground_surface=pygame.image.load("graphics/ground.png")

score_surface = pygame.image.load("graphics/board1.png")
score_rect = score_surface.get_rect(midtop=(750,0))

replay_surface=pygame.image.load("graphics/replay.png")
replay_rect=replay_surface.get_rect(midtop=(750,390))

settings_surface=pygame.image.load("graphics/settings.png")
settings_rect=settings_surface.get_rect(midtop=(710,390))

#coins
coin_index=0
coin1=pygame.image.load("graphics/coin1.png")
coin2=pygame.image.load("graphics/coin4.png")
coin3=pygame.image.load("graphics/coin3.png")
coin4=pygame.image.load("graphics/coin2.png")
coin5=pygame.image.load("graphics/coin6.png")
coin6=pygame.image.load("graphics/coin7.png")
coin_spin=[coin1,coin2,coin3,coin4,coin5,coin6,coin1]
coin_surface=coin_spin[coin_index]
coin_rect=coin_surface.get_rect(bottomleft=(300,300))

#characters
if colour in ["aqua",]:
    walk1="graphics/player_walk_1.png"
    walk2="graphics/player_walk_2.png"
    jump="graphics/jump.png"
    stand="graphics/player_stand.png"
if colour in ["blue",]:
    walk1="graphics/player_walk_1_b.png"
    walk2="graphics/player_walk_2_b.png"
    jump="graphics/jump_b.png"
    stand="graphics/player_stand_b.png"
if colour in ["red",]:
    walk1="graphics/player_walk_1_r.png"
    walk2="graphics/player_walk_2_r.png"
    jump="graphics/jump_r.png"
    stand="graphics/player_stand_r.png"
if colour in ["violet",]:
    walk1="graphics/player_walk_1_v.png"
    walk2="graphics/player_walk_2_v.png"
    jump="graphics/jump_v.png"
    stand="graphics/player_stand_v.png"
if colour in ["yellow",]:
    walk1="graphics/player_walk_1_y.png"
    walk2="graphics/player_walk_2_y.png"
    jump="graphics/jump_y.png"
    stand="graphics/player_stand_y.png"


player_index=0
player_walk_1=pygame.image.load(walk1).convert_alpha()
player_walk_2=pygame.image.load(walk2).convert_alpha()
player_jump=pygame.image.load(jump).convert_alpha()
player_walk=[player_walk_1,player_walk_2]
player_surface=player_walk[player_index]
player_rect=player_surface.get_rect(bottomleft=(50,300))

snail_index=0
snail1=pygame.image.load("graphics/snail1.png").convert_alpha()
snail2=pygame.image.load("graphics/snail2.png").convert_alpha()
snail=[snail1,snail2]
snail_surface=snail[snail_index]
snail_rect=snail_surface.get_rect(midbottom=(770,300))

fly_index=0
fly1=pygame.image.load("graphics/Fly1.png").convert_alpha()
fly2=pygame.image.load("graphics/Fly2.png").convert_alpha()
fly=[fly1,fly2]
fly_surface=fly[fly_index]

player_stand=pygame.image.load(stand)
player_stand=pygame.transform.scale2x(player_stand) #Transforming the player_surf
playerstand_rect=player_stand.get_rect(center=(360,260))

#Styles:
player_stand_a=pygame.image.load("graphics/player_stand.png")
player_stand_a=pygame.transform.scale2x(player_stand_a)
playerstand_rect_a=player_stand_a.get_rect(center=(230,260))

player_stand_r=pygame.image.load("graphics/player_stand_r.png")
player_stand_r=pygame.transform.scale2x(player_stand_r)
playerstand_rect_r=player_stand_r.get_rect(center=(360,260))

player_stand_b=pygame.image.load("graphics/player_stand_b.png")
player_stand_b=pygame.transform.scale2x(player_stand_b)
playerstand_rect_b=player_stand_b.get_rect(center=(490,260))

player_stand_v=pygame.image.load("graphics/player_stand_v.png")
player_stand_v=pygame.transform.scale2x(player_stand_v)
playerstand_rect_v=player_stand_v.get_rect(center=(620,260))

player_stand_y=pygame.image.load("graphics/player_stand_y.png")
player_stand_y=pygame.transform.scale2x(player_stand_y)
playerstand_rect_y=player_stand_y.get_rect(center=(100,260))



obstracle_timer=pygame.USEREVENT+1
pygame.time.set_timer(obstracle_timer,1800)

snail_animation_timer=pygame.USEREVENT+2
pygame.time.set_timer(snail_animation_timer,200)

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
            if event.type==obstracle_timer:
                choice=random.choice(("snail","fly"))
                position=random.randint(900,1100)
                if choice in ["snail",]:
                    obstracle_rect_list.append(snail_surface.get_rect(midbottom=(position,300)))
                if choice in ["fly",]:
                    obstracle_rect_list.append(fly_surface.get_rect(midbottom=(position,200)))

            if event.type==snail_animation_timer:
                for obstracle in obstracle_rect_list:
                    if obstracle.bottom==300:
                        snail_index+=0.3
                        if snail_index>=len(snail):
                            snail_index=0
                        snail_surface=snail[int(snail_index)]
                    else:
                        fly_index+=0.3
                        if fly_index>=len(fly):
                            fly_index=0
                        fly_surface=fly[int(fly_index)]
            if event.type==pygame.KEYDOWN and player_rect.colliderect(snail_rect)==False:
                if event.key==pygame.K_UP and player_rect.bottom>=100:
                    gravity = -15
                elif event.key==pygame.K_DOWN:
                    gravity =10
                if event.key==pygame.K_SPACE:
                    game_running=True
                    
        if game_running == False:
            if event.type==pygame.MOUSEMOTION:
                if settings_rect.collidepoint(event.pos):
                    book=pygame.mouse.get_pressed()
                    if book[0]==True:
                        settings=True
                        
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    game_running=True
                    settings=False
                    obstracle_rect_list=[]
                    snail_rect.right=800
                    if score>=3:
                        game_level+=1
                    score=0
                    starting_time=pygame.time.get_ticks()//1000
                    
            mousepos=pygame.mouse.get_pos()
            if replay_rect.collidepoint(mousepos):
                book=pygame.mouse.get_pressed()
                if book[0]==True:
                    game_running=True
                    settings=False
                    obstracle_rect_list=[]
                    snail_rect.right=800
                    if score>=3:
                        game_level+=1
                    score=0
                    starting_time=pygame.time.get_ticks()//1000
            mousepos=pygame.mouse.get_pos()
            if settings_rect.collidepoint(mousepos):
                book=pygame.mouse.get_pressed()
                if book[0]==True:
                    settings=True
                else:
                    pass
            
            if settings==True:
                mousepos=pygame.mouse.get_pos()
                if playerstand_rect_r.collidepoint(mousepos):
                    book=pygame.mouse.get_pressed()
                    if book[0]==True:
                        colour="red"
                if playerstand_rect_b.collidepoint(mousepos):
                    book=pygame.mouse.get_pressed()
                    if book[0]==True:
                        colour="blue"
                if playerstand_rect_v.collidepoint(mousepos):
                    book=pygame.mouse.get_pressed()
                    if book[0]==True:
                        colour="violet"
                if playerstand_rect_a.collidepoint(mousepos):
                    book=pygame.mouse.get_pressed()
                    if book[0]==True:
                        colour="aqua"
                if playerstand_rect_y.collidepoint(mousepos):
                    book=pygame.mouse.get_pressed()
                    if book[0]==True:
                        colour="yellow"
                
                
                
     
    if game_running==True:
        #Text
        text=("Score :"+ str(score))
        score_text_surface=score_font.render((text),False,"white")
            
        screen.blit(bg_surface,(0,0))
        screen.blit(ground_surface,(0,300))
        screen.blit(coin_surface,coin_rect)
        screen.blit(score_surface,score_rect)
        screen.blit(score_text_surface,(720,10))

        if colour in ["aqua",]:
            walk1="graphics/player_walk_1.png"
            walk2="graphics/player_walk_2.png"
            jump="graphics/jump.png"
            stand="graphics/player_stand.png"
        if colour in ["blue",]:
            walk1="graphics/player_walk_1_b.png"
            walk2="graphics/player_walk_2_b.png"
            jump="graphics/jump_b.png"
            stand="graphics/player_stand_b.png"
        if colour in ["red",]:
            walk1="graphics/player_walk_1_r.png"
            walk2="graphics/player_walk_2_r.png"
            jump="graphics/jump_r.png"
            stand="graphics/player_stand_r.png"
        if colour in ["violet",]:
            walk1="graphics/player_walk_1_v.png"
            walk2="graphics/player_walk_2_v.png"
            jump="graphics/jump_v.png"
            stand="graphics/player_stand_v.png"
        if colour in ["yellow",]:
            walk1="graphics/player_walk_1_y.png"
            walk2="graphics/player_walk_2_y.png"
            jump="graphics/jump_y.png"
            stand="graphics/player_stand_y.png"

        player_walk_1=pygame.image.load(walk1).convert_alpha()
        player_walk_2=pygame.image.load(walk2).convert_alpha()
        player_jump=pygame.image.load(jump).convert_alpha()
        player_walk=[player_walk_1,player_walk_2]
        player_surface=player_walk[int(player_index)]
        #player_rect=player_surface.get_rect(bottomleft=(50,300))


        screen.blit(player_surface,player_rect)
        screen.blit(snail_surface,snail_rect)

        display_time()
        player_animation()
        coin_animation()
        primary_snail_animation()

        if game_level>12:
            game_level=0
        bg_surface=sky[game_level]
        
        #gravity mechanism:
        gravity+=1
        player_rect.y+=gravity

        if player_rect.bottom>=300:
            player_rect.bottom=300
            gravity=0

        obstracle_rect_list=obstracle_movement(obstracle_rect_list)
        #collision:

        game_running=collision(player_rect,obstracle_rect_list)
        if player_rect.colliderect(snail_rect):
            game_running=False
            settings=False
            #starting_time=pygame.time.get_ticks()//1000

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

    #screen after game over

    if game_running==False and starting_time>0:
        pygame.time.wait(360)
        screen.fill("cornflowerblue")
        
        screen.blit(player_stand,playerstand_rect)

        screen.blit(replay_surface,replay_rect)
        
        game_font=pygame.font.Font(None,50)
        game_font_surface=game_font.render("Press space to replay",False,"Powderblue")
        screen.blit(game_font_surface,(200,370))

        final_score_surface=game_font.render("Infinite runner score :"+ str(score),False,"Powderblue")
        screen.blit(final_score_surface,(200,70))

        '''while True:
            value=pygame.mouse.get_pressed()
            if value[0]==True:
                game_running=True'''

        #screen before game begins:
    if game_running==False and starting_time in range(0,12) and score==0:
        #To account for the delay in game loading (rarely)
        
        screen.fill("salmon")
        bsurface=pygame.image.load("graphics/Sky10.jpg")
        bsurface=pygame.transform.scale(bsurface,(800,350))
        screen.blit(bsurface,(0,0))
        screen.blit(player_stand,playerstand_rect)

        screen.blit(replay_surface,replay_rect)
        screen.blit(settings_surface,settings_rect)
        
        game_font=pygame.font.Font(None,50)
        game_font_surface=game_font.render("Press space to play the game",False,"Crimson")
        screen.blit(game_font_surface,(170,390))

        game_name=game_font.render("Infinite Runner",False,"Crimson")
        screen.blit(game_name,(250,70))

        if settings==True and game_running==False:
            screen.fill("cornflowerblue")

            screen.blit(player_stand_y,playerstand_rect_y)
            screen.blit(player_stand_a,playerstand_rect_a)
            screen.blit(player_stand_r,playerstand_rect_r)
            screen.blit(player_stand_b,playerstand_rect_b)
            screen.blit(player_stand_v,playerstand_rect_v)

            screen.blit(replay_surface,replay_rect)
        
        
            game_font=pygame.font.Font(None,50)
            game_font_surface=game_font.render("Press space to replay",False,"Powderblue")
            screen.blit(game_font_surface,(180,370))

            select_surface=game_font.render("Click on the colour to select avatar",False,"Powderblue")
            screen.blit(select_surface,(120,70))

                    
               

    pygame.display.update()#for updating the initial display surface
    clock.tick(60)#The while true loop should not run faster than 60 times a sec


'''
    To figure out point
    mousepos=pygame.mouse.get_pos()
    if player_rect.collidepoint(mousepos):
        print(mousepos)
'''
