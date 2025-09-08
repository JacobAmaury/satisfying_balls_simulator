import pygame



def create_window(width, height):
    screen = pygame.display.set_mode((width, height))
    background_colour = (55,55,55)
    screen.fill(background_colour)
    pygame.display.set_caption('Tutorial 1')
    pygame.display.flip()

    while True:
        pass



create_window(1920,1080)