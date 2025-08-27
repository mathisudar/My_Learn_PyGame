import pygame

# Initialize Pygame
pygame.init()

# Set up the game window
surface = pygame.display.set_mode((400, 300)) 
pygame.display.set_caption("Surface Color!") 


WHITE = (255,255,255) 
surface.fill(WHITE)


pygame.display.update()


# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit Pygame
pygame.quit()