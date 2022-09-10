import pygame, sys, random

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
pygame.display.set_caption("Dino Run")

#Variables
game_speed = 5



# Surface for the game
ground = pygame.image.load("assets/ground.png")
ground = pygame.transform.scale(ground, (1280,20))
ground_x = 0

ground_rect=ground.get_rect(center=(640, 400))



while True:
    for event in pygame.event.get():
        if event .type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill("white")

    game_speed = game_speed + 0.005
    ground_x=ground_x-1

    screen.blit(ground, (ground_x, 360))
    screen.blit(ground, (ground_x +1280, 360))

    if ground_x<= -1280:
        ground_x=0

    pygame.display.update()
    clock.tick(120)