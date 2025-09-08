import pygame



def place_ball(screen, pos_x, pos_y):
    pygame.draw.circle(screen, (255,255,255), (pos_x, pos_y), 15, 1)

def create_window(width, height):
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('balls simulation')
    return screen





