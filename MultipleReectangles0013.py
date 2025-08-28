import pygame

# Initialize Pygame
pygame.init()

# Set up the game window
window = pygame.display.set_mode((600, 600))
window.fill((255, 255, 255))
pygame.display.set_caption("MultipleRectangles")

# Creating a list of different rects
rectangle_list = [pygame.Rect(50, 100, 500, 200),
                  pygame.Rect(70, 120, 460, 160),
                  pygame.Rect(90, 140, 420, 120),
                  pygame.Rect(110, 160, 380, 80),
                  pygame.Rect(130, 180, 340, 40)
                  ]

# Creating list of different colors
color_list = [(0,   0,   0),
              (255, 255, 255),
              (0,   0, 255),
              (0, 255,   0),
              (255,   0,   0)
              ]

# Creating a variable which we will use
# to iterate over the color_list
color_var = 0

# Iterating over the rectangle_list using
# for loop
for rectangle in rectangle_list:

    # Drawing the rectangle 
    # using the draw.rect() method
    pygame.draw.rect(window, color_list[color_var],
                     rectangle)

    # Increasing the value of color_var
    # by 1 after every iteration
    color_var += 1

pygame.display.update()


# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit Pygame
pygame.quit()


