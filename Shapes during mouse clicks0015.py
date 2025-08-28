import pygame



# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()



# Set up the game window
window = pygame.display.set_mode((600, 600))
window.fill((255, 255, 255))
pygame.display.set_caption("Shapes during mouse clicks")


# creating list in which we will store
# the position of the circle
circle_positions = []

# Color of the circle
color = (0, 0, 255)

# radius of the circle
circle_radius = 60




# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if the type of the event is MOUSEBUTTONDOWN
        # then storing the current position
        elif event.type == pygame.MOUSEBUTTONDOWN:
            position = event.pos
            circle_positions.append(position)

    # Using for loop to iterate
    # over the circle_positions
    # list
    for position in circle_positions:

        # Drawing the circle
        pygame.draw.circle(window, color, position,
                           circle_radius)
        
    pygame.display.update()


# Quit Pygame
pygame.quit()


