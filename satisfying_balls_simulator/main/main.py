import pygame
import display
import balls_simulation

#init
screen = display.create_window(800, 600) 
background_colour = (55,55,55)
running = True
ball_1 = balls_simulation.ball(0,0,1,1)
clock = pygame.time.Clock()


#main loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False


    screen.fill(background_colour)

    ball_1.actu_pos()
    
    display.place_ball(screen, ball_1.pos_x, ball_1.pos_y)
    pygame.display.flip() 

    clock.tick(60) #set 60 fps