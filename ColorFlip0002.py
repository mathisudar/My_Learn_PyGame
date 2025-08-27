import pygame

# Initialize Pygame
pygame.init()

# Set up the game window
window = pygame.display.set_mode((600, 600))

pygame.display.set_caption("Color Flip")




# Game loop
running = True
color = "red"

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    window.fill(color)
    pygame.display.flip()  
    



    pygame.display.update()
    if (color == "red"):
        color = "green"
        
    else:
        color = "red"

# Quit Pygame
pygame.quit()



 