import pygame



def place_ball(screen, pos_x, pos_y):
    pygame.draw.circle(screen, (255,255,255), (pos_x, pos_y), 15, 1)

def create_window(width, height):
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('balls simulation')
    return screen

def draw_line(screen, rgb_code ,wall_coord):
    for i in range(len(wall_coord)):
        pygame.draw.line(screen, (255, 255, 255), (wall_coord[i][0], wall_coord[i][2]), (wall_coord[i][1], wall_coord[i][3]), 3)






