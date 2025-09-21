import pygame
import display
import balls_simulation
import random as rd

#init
width = 1920
height = 1080
v_max_init = 60*3
number_of_balls = 10

walls = [[0, 800, 0, 2000, "up"], [1500, 2200, 0, 2000, "down"], [0, 1920, 400, 450, "down"], [0, 1920, 940, 900, "up"]]
walls_simu = balls_simulation.walls_for_simu(walls)




balls = balls_simulation.balls_init(v_max_init, width, height, number_of_balls)


screen = display.create_window(width, height) 
background_colour = (55,55,55)
running = True
clock = pygame.time.Clock()
t = 0.
fps = 60*2.
dt = 1/(fps/10)

#main loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False
    screen.fill(background_colour)
    display.draw_line(screen, (255, 255, 255), walls)

    for i in range(number_of_balls):
        balls[i].actu_pos(dt, height, width, walls_simu)
        display.place_ball(screen, balls[i].pos_x, balls[i].pos_y)

    pygame.display.flip() 
    


    clock.tick(fps) #set the fps