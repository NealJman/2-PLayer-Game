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

Red_Ship = pygame.image.load(os.path.join('Images&Sound','pirateShipleft.png'))
Red_Ship = pygame.transform.scale(Red_Ship,(shipRed_dim,shipRed_dim))
Black_Ship = pygame.image.load(os.path.join('Images&Sound','pirateShipright.png'))
Black_Ship = pygame.transform.scale(Black_Ship,(shipBlack_dim,shipBlack_dim))

def draw_window(red,black):


    WIN.fill(white)
    WIN.blit(Red_Ship, (red.x,red.y))
    WIN.blit(Black_Ship, (black.x,black.y))
    pygame.display.update()




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

        

        draw_window(red,black)
        
    
    pygame.quit()

if __name__ == "__main__":
    main()