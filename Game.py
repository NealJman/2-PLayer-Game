import pygame
pygame.font.init()
pygame.mixer.init()
import os

# Screen dimensions
WIDTH= 900
HEIGHT = 500

HEALTH_FONT = pygame.font.SysFont('comicsans',30)
WINNER_FONT = pygame.font.SysFont('comicsans', 100 )
shipRed_dim = 100;
shipBlack_dim = 90;
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Pirate Ship Duel")

WHITE = (255,255,255)
BLACK = (0,0,0)

FPS = 60
VELOCITY = 5
CBALLS_VELOCITY = 7
MAX_CBALLS = 3


R1_HIT = pygame.USEREVENT + 1
L1_HIT = pygame.USEREVENT + 2
R2_HIT = pygame.USEREVENT + 3
R3_HIT = pygame.USEREVENT + 4
L2_HIT = pygame.USEREVENT + 5
L3_HIT = pygame.USEREVENT + 6

CBALL_HIT_SOUND = pygame.mixer.Sound(os.path.join('Images&Sound','cannon.mp3' ))
CBALL_FIRE_SOUND = pygame.mixer.Sound(os.path.join('Images&Sound','cannon-shot.wav' ))

Red_Ship = pygame.image.load(os.path.join('Images&Sound','pirateShipleft.png'))
Red_Ship = pygame.transform.scale(Red_Ship,(shipRed_dim,shipRed_dim))
Black_Ship = pygame.image.load(os.path.join('Images&Sound','pirateShipright.png'))
Black_Ship = pygame.transform.scale(Black_Ship,(shipBlack_dim,shipBlack_dim))

Island_left1 = pygame.image.load(os.path.join('Images&Sound','island.png'))
Island_left1 = pygame.transform.scale(Island_left1, (50,50))
Island_left2 = pygame.image.load(os.path.join('Images&Sound','island.png'))
Island_left2 = pygame.transform.scale(Island_left2, (50,50))
Island_left3 = pygame.image.load(os.path.join('Images&Sound','island.png'))
Island_left3 = pygame.transform.scale(Island_left3, (50,50))

Island_right1 = pygame.image.load(os.path.join('Images&Sound','island.png'))
Island_right1 = pygame.transform.scale(Island_right1, (50,50))
Island_right2 = pygame.image.load(os.path.join('Images&Sound','island.png'))
Island_right2 = pygame.transform.scale(Island_right2, (50,50))
Island_right3 = pygame.image.load(os.path.join('Images&Sound','island.png'))
Island_right3 = pygame.transform.scale(Island_right3, (50,50))

Sea = pygame.image.load(os.path.join('Images&Sound','sea.png'))
Sea = pygame.transform.scale(Sea, (WIDTH,HEIGHT))

def draw_window(red,black,IslandL1,IslandL2, IslandL3, IslandR1, IslandR2, IslandR3, 
                Red_cannonballs, Black_cannonballs, red_health, black_health,
                R1_health,R2_health,R3_health,L1_health,L2_health,L3_health):

    
    WIN.blit(Sea, (0,0))
    
    red_health_text = HEALTH_FONT.render("Health: " +str(red_health),1, WHITE)
    black_health_text = HEALTH_FONT.render("Health: " +str(black_health),1, WHITE)
    WIN.blit(red_health_text, (700, 10))
    WIN.blit(black_health_text, (10, 10))


    WIN.blit(Red_Ship, (red.x,red.y))
    WIN.blit(Black_Ship, (black.x,black.y))
    if L1_health >= 1:
        WIN.blit(Island_left1,(IslandL1.x,IslandL1.y))
    if L2_health >= 1:
        WIN.blit(Island_left2,(IslandL2.x,IslandL2.y))
    if L3_health >= 1:
        WIN.blit(Island_left3,(IslandL3.x,IslandL3.y))
    if R1_health >= 1:
        WIN.blit(Island_right1,(IslandR1.x, IslandR1.y))
    if R2_health >= 1:
        WIN.blit(Island_right2,(IslandR2.x,IslandR2.y))
    if R3_health >= 1:
        WIN.blit(Island_right3,(IslandR3.x,IslandR3.y))

    for Cball in Red_cannonballs:
        pygame.draw.rect(WIN, BLACK, Cball);
    for Cball in Black_cannonballs:
        pygame.draw.rect(WIN, BLACK, Cball);


    pygame.display.update()

def red_moves(keys_pressed, red):
        
        # Left
        if keys_pressed[pygame.K_a] and red.x - VELOCITY > 120: 
            red.x -= VELOCITY
        #Right
        if keys_pressed[pygame.K_d]and red.x + VELOCITY < 680: 
            red.x += VELOCITY
        #Up
        if keys_pressed[pygame.K_w]and red.y - VELOCITY > 0: 
            red.y -= VELOCITY
        #Down
        if keys_pressed[pygame.K_s]and red.y + VELOCITY < 400: 
            red.y += VELOCITY


def black_moves(keys_pressed, black):
        
        #Left
        if keys_pressed[pygame.K_LEFT] and black.x - VELOCITY > 120: 
            black.x -= VELOCITY
        #Right
        if keys_pressed[pygame.K_RIGHT] and black.x + VELOCITY < 680: 
            black.x += VELOCITY
        #Up
        if keys_pressed[pygame.K_UP] and black.y - VELOCITY > 0: 
            black.y -= VELOCITY
        #Down
        if keys_pressed[pygame.K_DOWN] and black.y + VELOCITY < 400: 
            black.y += VELOCITY


def handle_Cballs(Black_cannonballs, Red_cannonballs, IslandL1,IslandL2,IslandL3, IslandR1, IslandR2,IslandR3):

    for cannonball in Red_cannonballs:
        cannonball.x += CBALLS_VELOCITY
        if IslandR1.colliderect(cannonball):
            pygame.event.post(pygame.event.Event(R1_HIT))
            Red_cannonballs.remove(cannonball)


        if IslandR2.colliderect(cannonball):
            pygame.event.post(pygame.event.Event(R2_HIT))
            Red_cannonballs.remove(cannonball)



        if IslandR3.colliderect(cannonball):
            pygame.event.post(pygame.event.Event(R3_HIT))
            Red_cannonballs.remove(cannonball)
        elif cannonball.x > WIDTH:
            Red_cannonballs.remove(cannonball)
    



    for cannonball in Black_cannonballs:
        cannonball.x -= CBALLS_VELOCITY

        if IslandL1.colliderect(cannonball):
            pygame.event.post(pygame.event.Event(L1_HIT))
            Black_cannonballs.remove(cannonball)


        if IslandL2.colliderect(cannonball):
            pygame.event.post(pygame.event.Event(L2_HIT))
            Black_cannonballs.remove(cannonball)


        if IslandL3.colliderect(cannonball):
            pygame.event.post(pygame.event.Event(L3_HIT))
            Black_cannonballs.remove(cannonball)
        elif  cannonball.x < 0:
            Black_cannonballs.remove(cannonball)



def draw_winner(text):
    draw_text = WINNER_FONT.render(text,1,WHITE)
    WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width()/2,HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(4000)

def main():

    red = pygame.Rect(100,300,shipRed_dim, shipRed_dim)
    black = pygame.Rect(700,300,shipRed_dim, shipRed_dim)

    IslandL1 = pygame.Rect(50,50,50,50)
    IslandL2 = pygame.Rect(50,200,50,50)   
    IslandL3 = pygame.Rect(50,350,50,50)
    IslandR1 = pygame.Rect(800,50,50,50)
    IslandR2 = pygame.Rect(800,200,50,50)
    IslandR3 = pygame.Rect(800,350,50,50)


    Red_cannonballs = []
    Black_cannonballs = []

    red_health = 15
    black_health = 15

    L1_health = 5
    L2_health = 5
    L3_health=5
    R1_health=5
    R2_health=5
    R3_health=5

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(Red_cannonballs) < MAX_CBALLS:
                    CannonBall = pygame.Rect(red.x + red.width, red.y + red.height//2 -2, 10,10)
                    Red_cannonballs.append(CannonBall)
                    CBALL_FIRE_SOUND.play()

                if event.key == pygame.K_RCTRL and len(Black_cannonballs) < MAX_CBALLS:
                    CannonBall = pygame.Rect(black.x, black.y + black.height//2 -2, 10,10)
                    Black_cannonballs.append(CannonBall)
                    CBALL_FIRE_SOUND.play()

            if event.type == R1_HIT:
                
                R1_health -=1

                if R1_health >= 0:
                    red_health -= 1

                CBALL_HIT_SOUND.play()

            if event.type == R2_HIT:
                
                R2_health -=1

                if R2_health >= 0:
                    red_health -= 1
                CBALL_HIT_SOUND.play()

            if event.type == R3_HIT:
            
                R3_health -=1

                if R3_health >= 0:
                    red_health -= 1
                CBALL_HIT_SOUND.play()

            if event.type == L1_HIT:

                L1_health -=1
                if L1_health>=0:
                    black_health -= 1

                CBALL_HIT_SOUND.play()


            if event.type == L2_HIT:
                L2_health -=1
                if L2_health>=0:
                    black_health -= 1
                CBALL_HIT_SOUND.play()


            if event.type == L3_HIT:
                L3_health -=1
                if L3_health>=0:
                    black_health -= 1
                CBALL_HIT_SOUND.play()


            if L1_health == 0:
                IslandL1 = pygame.Rect(50,-1000,50,50)
            if L2_health == 0:
                IslandL2 = pygame.Rect(50,-1000,50,50)
            if L3_health == 0:
                IslandL3 = pygame.Rect(50,-1000,50,50)
            if R1_health == 0:
                IslandR1 = pygame.Rect(50,-1000,50,50)
            if R2_health == 0:
                IslandR2 = pygame.Rect(50,-1000,50,50)
            if R3_health == 0:
                IslandR3 = pygame.Rect(50,-1000,50,50)

        keys_pressed = pygame.key.get_pressed()

        red_moves(keys_pressed, red)
        black_moves(keys_pressed, black)

        handle_Cballs(Black_cannonballs, Red_cannonballs,IslandL1,IslandL2,IslandL3, IslandR1, IslandR2,IslandR3)


        draw_window(red,black,IslandL1,IslandL2,IslandL3, IslandR1, 
                    IslandR2,IslandR3, Red_cannonballs,Black_cannonballs, red_health,black_health,
                    R1_health,R2_health,R3_health,L1_health,L2_health,L3_health)
        
        winner_text = ""
        if red_health <=0:
            
            winner_text = "Red Ship Wins!"

        if black_health <=0:

            winner_text = "Black Ship Wins"

        if winner_text != "":
            draw_winner(winner_text)
            break

    
    main()

if __name__ == "__main__":
    main()