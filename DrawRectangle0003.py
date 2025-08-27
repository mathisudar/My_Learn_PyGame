import pygame

# Initialize Pygame
pygame.init()

# Set up the game window
surface = pygame.display.set_mode((600, 600))
surface.fill((255, 255, 255)) # White
pygame.display.set_caption("Rectangle")

color = (255,255,0) # yellow
pygame.draw.rect(surface,color,[100,100,50,70],2)
pygame.display.update()  




# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit Pygame
pygame.quit()
