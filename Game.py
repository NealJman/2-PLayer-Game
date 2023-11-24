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

Red_Ship = pygame.image.load(os.path.join('Images&Sound','pirateShipleft.png'))
Red_Ship = pygame.transform.scale(Red_Ship,(shipRed_dim,shipRed_dim))
Black_Ship = pygame.image.load(os.path.join('Images&Sound','pirateShipright.png'))
Black_Ship = pygame.transform.scale(Black_Ship,(shipBlack_dim,shipBlack_dim))

def draw_window(red,black):


    WIN.fill(white)
    WIN.blit(Red_Ship, (red.x,red.y))
    WIN.blit(Black_Ship, (black.x,black.y))
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


    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()

        red_moves(keys_pressed, red)
        black_moves(keys_pressed, black)

        draw_window(red,black)
        
    
    pygame.quit()

if __name__ == "__main__":
    main()