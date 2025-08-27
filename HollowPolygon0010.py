import pygame

# Initialize Pygame
pygame.init()

# Set up the game window
window = pygame.display.set_mode((600, 600))
window.fill((255, 255, 255))
pygame.display.set_caption("Outlined Polygon")

# pygame to draw the outlined polygon
pygame.draw.polygon(window, (255, 0, 0), 
                    [[300, 300], [100, 400],
                     [100, 300]], 5)


pygame.display.update()


# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit Pygame
pygame.quit()
