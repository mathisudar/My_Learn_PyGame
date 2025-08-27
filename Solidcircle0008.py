import pygame

# Initialize Pygame
pygame.init()

# Set up the game window
window = pygame.display.set_mode((600, 600))
window.fill((255, 255, 255))
pygame.display.set_caption("Solid Circle")

pygame.draw.circle(window, (0, 255, 0),
                   [300, 300], 170, 0)

pygame.display.update()


# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit Pygame
pygame.quit()
