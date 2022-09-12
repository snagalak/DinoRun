import pygame, sys, random

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
pygame.display.set_caption("Dino Run")

#Classes
class Dino(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        super().__init__()

        self.running_sprites = []

        self.running_sprites.append(pygame.image.load("assets/Dino1.png"))
        self.running_sprites.append(pygame.image.load("assets/Dino2.png"))

        self.x = x_pos 
        self.y= y_pos

        self.current_image = 0
        self.image = self.running_sprites[self.current_image]
        self.rect = self.image.get_rect(center = (self.x,self.y))
        self.velocity = 50

    def animate(self):
        self.current_image+=1
        if self.current_image>1:
            self.current_image=0
        
        self.image = self.running_sprites[self.current_image]
    
    def update(self):
        self.animate()


#Variables
game_speed = 5


# Surface for the game
ground = pygame.image.load("assets/ground.png")
ground = pygame.transform.scale(ground, (1280,20))
ground_x = 0

ground_rect=ground.get_rect(center=(640, 400))

# Groups

dino_group = pygame.sprite.GroupSingle()

# Objects

dinosaur = Dino (50,360)
dino_group.add(dinosaur)

while True:
    for event in pygame.event.get():
        if event .type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill("white")

    dino_group.update()
    dino_group.draw(screen)

    game_speed = game_speed + 0.0025
    ground_x=ground_x-1

    screen.blit(ground, (ground_x, 360))
    screen.blit(ground, (ground_x +1280, 360))

    if ground_x<= -1280:
        ground_x=0

    pygame.display.update()
    clock.tick(120)
