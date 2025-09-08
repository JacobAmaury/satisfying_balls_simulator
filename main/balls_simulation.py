import pygame
import random as rd

class ball:
    def __init__(self, pos_x, pos_y, v_x, v_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.v_x = v_x
        self.v_y = v_y


    def actu_pos(self, dt, height, width):
        #init
        g = 9.81
        alpha = 0.9
        smallest_v = 0.1 
        change_sign = -1.0

        #for y
        self.v_y += g*dt*0.5 
        self.pos_y += self.v_y*dt
        self.v_y += g*dt*0.5 

        if(self.pos_y >= height):
            self.v_y = self.v_y * change_sign
            self.pos_y = height
            self.v_y = self.v_y * alpha


        #for x
        self.pos_x += self.v_x*dt

        if(self.pos_x >= width):
            self.v_x = self.v_x * change_sign
            self.pos_x = width
            self.v_x = self.v_x * alpha
        
        if(self.pos_x <= 0):
            self.v_x = self.v_x * change_sign
            self.pos_x = 0
            self.v_x = self.v_x * alpha





def balls_init(v_max_init, width, height, number_balls):

    balls = [] 
    for i in range(number_balls):
        balls.append(ball(rd.randint(0, width), rd.randint(0, height), rd.randint(0, v_max_init), rd.randint(0, v_max_init)))
    
    return balls
