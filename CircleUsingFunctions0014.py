import pygame


def drawingfunction(x, y, width, height):

    # Creating rectangle using the draw.rect() method
    pygame.draw.rect(window, (0, 0, 255), [x, y, width, height])

    # Calculation the center of the circle
    circle_x = width/2 + x
    circle_y = height/2 + y

    # Calculating the radius of the circle
    if height < width:
        radius = height/2
    else:
        radius = width/2

    # Drawing the circle
    pygame.draw.circle(window, (0, 255, 0), [circle_x, circle_y], radius)






# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()



# Set up the game window
window = pygame.display.set_mode((600, 600))
window.fill((255, 255, 255))
pygame.display.set_caption("Circle Using Functions")


# Calling the drawing function
drawingfunction(50, 200, 500, 200)


pygame.display.update()


# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit Pygame
pygame.quit()


