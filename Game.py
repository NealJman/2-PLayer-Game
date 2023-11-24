import pygame
import os


WIDTH= 900
HEIGHT = 500

shipRed_dim = 100;
shipBlack_dim = 90;
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Pirate Ship Duel")

white = (255,255,255)
FPS = 60
VELOCITY = 5
CBALLS_VELOCITY = 7
MAX_CBALLS = 3

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

def draw_window(red,black):


    WIN.fill(white)
    WIN.blit(Red_Ship, (red.x,red.y))
    WIN.blit(Black_Ship, (black.x,black.y))
    WIN.blit(Island_left1,(50,50))
    WIN.blit(Island_left2,(50,200))
    WIN.blit(Island_left3,(50,350))
    WIN.blit(Island_right1,(800,50))
    WIN.blit(Island_right2,(800,200))
    WIN.blit(Island_right3,(800,350))
    pygame.display.update()

def red_moves(keys_pressed, red):
        
         #Left
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





def main():

    red = pygame.Rect(100,300,shipRed_dim, shipRed_dim)
    black = pygame.Rect(700,300,shipRed_dim, shipRed_dim)

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
                    CannonBall = (red.x + red.width, red.y + red.height/2 -2, 10,10)
                    Red_cannonballs.append(CannonBall)

                if event.key == pygame.K_RCTRL and len(Black_cannonballs) < MAX_CBALLS:
                    CannonBall = (black.x, black.y + black.height/2 -2, 10,10)
                    Black_cannonballs.append(CannonBall)

        keys_pressed = pygame.key.get_pressed()

        red_moves(keys_pressed, red)
        black_moves(keys_pressed, black)

        draw_window(red,black)
        
    
    pygame.quit()

if __name__ == "__main__":
    main()