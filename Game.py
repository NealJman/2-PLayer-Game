import pygame
pygame.init()
import os


WIDTH= 900
HEIGHT = 500


shipRed_dim = 100;
shipBlack_dim = 90;
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Pirate Ship Duel")

white = (255,255,255)
BLACK = (0,0,0)

FPS = 60
VELOCITY = 5
CBALLS_VELOCITY = 4
MAX_CBALLS = 15


RED_HIT = pygame.USEREVENT + 1
BLACK_HIT = pygame.USEREVENT + 2



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

def draw_window(red,black,IslandL1,IslandL2, IslandL3, IslandR1, IslandR2, IslandR3, Red_cannonballs, Black_cannonballs):


    WIN.fill(white)
    WIN.blit(Red_Ship, (red.x,red.y))
    WIN.blit(Black_Ship, (black.x,black.y))
    WIN.blit(Island_left1,(IslandL1.x,IslandL1.y))
    WIN.blit(Island_left2,(IslandL2.x,IslandL2.y))
    WIN.blit(Island_left3,(IslandL3.x,IslandL3.y))
    WIN.blit(Island_right1,(IslandR1.x, IslandR1.y))
    WIN.blit(Island_right2,(IslandR2.x,IslandR2.y))
    WIN.blit(Island_right3,(IslandR3.x,IslandR3.y))

    for Cball in Red_cannonballs:
        pygame.draw.rect(WIN, BLACK, Cball);
    for Cball in Black_cannonballs:
        pygame.draw.rect(WIN, BLACK, Cball);


    pygame.display.update()

def red_moves(keys_pressed, red):
        
        # Left
        if keys_pressed[pygame.K_a] and red.x - VELOCITY > 100: 
            red.x -= VELOCITY
        #Right
        if keys_pressed[pygame.K_d]and red.x + VELOCITY < 700: 
            red.x += VELOCITY
        #Up
        if keys_pressed[pygame.K_w]and red.y - VELOCITY > 0: 
            red.y -= VELOCITY
        #Down
        if keys_pressed[pygame.K_s]and red.y + VELOCITY < 400: 
            red.y += VELOCITY


def black_moves(keys_pressed, black):
        
         #Left
        if keys_pressed[pygame.K_LEFT] and black.x - VELOCITY > 100: 
            black.x -= VELOCITY
        #Right
        if keys_pressed[pygame.K_RIGHT] and black.x + VELOCITY < 700: 
            black.x += VELOCITY
        #Up
        if keys_pressed[pygame.K_UP] and black.y - VELOCITY > 0: 
            black.y -= VELOCITY
        #Down
        if keys_pressed[pygame.K_DOWN] and black.y + VELOCITY < 400: 
            black.y += VELOCITY


def handle_Cballs(Black_cannonballs, Red_cannonballs, IslandL1,IslandL2,IslandL3, IslandR1, IslandR2,IslandR3):
    #[(4, 6, 10,10), (7, 6, 10,10)]
    for cannonballs in Red_cannonballs:
        cannonballs.x += CBALLS_VELOCITY
        if IslandR1.colliderect(cannonballs):
            pygame.event.post(pygame.event.Event(RED_HIT))
            Red_cannonballs.remove(cannonballs)

    for cannonballs in Black_cannonballs:
        cannonballs.x -= CBALLS_VELOCITY
        if IslandL1.colliderect(cannonballs):
            pygame.event.post(pygame.event.Event(BLACK_HIT))
            Black_cannonballs.remove(cannonballs)

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

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(Red_cannonballs) < MAX_CBALLS:
                    CannonBall = pygame.Rect(red.x + red.width, red.y + red.height//2 -2, 10,10)
                    Red_cannonballs.append(CannonBall)

                if event.key == pygame.K_RCTRL and len(Black_cannonballs) < MAX_CBALLS:
                    CannonBall = pygame.Rect(black.x, black.y + black.height//2 -2, 10,10)
                    Black_cannonballs.append(CannonBall)

        keys_pressed = pygame.key.get_pressed()

        red_moves(keys_pressed, red)
        black_moves(keys_pressed, black)

        handle_Cballs(Black_cannonballs, Red_cannonballs,IslandL1,IslandL2,IslandL3, IslandR1, IslandR2,IslandR3)


        draw_window(red,black,IslandL1,IslandL2,IslandL3, IslandR1, IslandR2,IslandR3, Red_cannonballs,Black_cannonballs)
        
    
    pygame.quit()

if __name__ == "__main__":
    main()