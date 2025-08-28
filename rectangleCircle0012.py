import pygame

# Initialize Pygame
pygame.init()

# Set up the game window
window = pygame.display.set_mode((600, 600))
window.fill((255, 255, 255))
pygame.display.set_caption("Rectangle and Circle")

# pygame to draw the rectangle
pygame.draw.rect(window, (0, 0, 255),
                 [50, 200, 500, 200])

# Using draw.rect module of
# pygame to draw the circle inside the rectangle
pygame.draw.circle(window, (0, 255, 0),
                   [300, 300], 100)



pygame.display.update()


# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit Pygame
pygame.quit()


