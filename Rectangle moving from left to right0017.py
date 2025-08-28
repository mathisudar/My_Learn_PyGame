import pygame
pygame.init() 

w, h = 600, 200  # size
surface = pygame.display.set_mode((w, h)) 

c_white, c_blue = (255,255,255), (0,0,255)  # colors
x, y, rw, rh, posIncr = 0, 50, 60, 40, 5  # rect params

clk = pygame.time.Clock()  # clock


run = True  
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False 

    surface.fill(c_white) 

    pygame.draw.rect(surface, c_blue, (x, y, rw, rh)) 

    x = (x + posIncr) % (w + rw) - rw 

    pygame.display.flip()  
    clk.tick(30)  

pygame.quit() 



""" Explanation:

while loop keeps the program active until the window is closed, 
handling events and updating the screen by clearing it and drawing 
the moving blue rectangle that wraps around horizontally.

pygame.display.flip() refreshes the display each frame, 
while clk.tick(30) limits the frame rate to 30 FPS for smooth animation. """

