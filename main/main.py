import pygame
import display
import balls_simulation

#init
width = 800
height = 600

screen = display.create_window(width, height) 
background_colour = (55,55,55)
running = True
ball_1 = balls_simulation.ball(100,0,30,0)
clock = pygame.time.Clock()
t = 0.
fps = 60.
dt = 1/(fps/10)

#main loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False
    screen.fill(background_colour)


    ball_1.actu_pos(dt, height, width)
    display.place_ball(screen, ball_1.pos_x, ball_1.pos_y)
    pygame.display.flip() 
    


    clock.tick(fps) #set the fps