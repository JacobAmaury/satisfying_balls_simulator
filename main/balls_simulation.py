import pygame
import random as rd

class ball:
    def __init__(self, pos_x, pos_y, v_x, v_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.v_x = v_x
        self.v_y = v_y


    def actu_pos(self, dt, height, width, wall_coord):
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
            

        for i in range(len(wall_coord)):
            a,b = get_affine_coef(wall_coord[i])
            norm_1, norm_2 = get_normal(wall_coord[i])

            if(wall_coord[i][4] == "up"):
                if(self.pos_y>(self.pos_x*a+b)):
                    reflect_vector_x, reflect_vector_y = reflection_vector(self.v_x, self.v_y, norm_1[0], norm_1[1])
                    self.v_x = reflect_vector_x
                    self.v_y = reflect_vector_y
            elif(wall_coord[i][4] == "down"):

                if(self.pos_y<(self.pos_x*a+b)):
                    reflect_vector_x, reflect_vector_y = reflection_vector(self.v_x, self.v_y, norm_1[0], norm_1[1])
                    self.v_x = reflect_vector_x
                    self.v_y = reflect_vector_y


            



def balls_init(v_max_init, width, height, number_balls):

    balls = [] 
    for i in range(number_balls):
        balls.append(ball(width/2, height/2, rd.randint(-v_max_init, v_max_init), rd.randint(-v_max_init, v_max_init)))
    
    return balls


def reflection_vector(vx, vy, normal_x, normal_y):
    # normalization of the normal
    normal_length = (normal_x**2 + normal_y**2) ** 0.5
    normalized_normal_x = normal_x / normal_length
    normalized_normal_y = normal_y / normal_length
    # dot product
    dot = vx * normalized_normal_x + vy * normalized_normal_y
    # reflection formula
    reflect_vector_x = vx - 2 * dot * normalized_normal_x
    reflect_vector_y = vy - 2 * dot * normalized_normal_y
    
    return reflect_vector_x, reflect_vector_y



def get_normal(wall_coord):
    x1 = wall_coord[0]
    x2 = wall_coord[1]
    y1 = wall_coord[2]
    y2 = wall_coord[3]
    dx = x2 - x1
    dy = y2 - y1
    normal_1 = (-dy, dx)
    normal_2 = (dy, -dx)
    return normal_1, normal_2
    
    
def get_affine_coef(wall_coord):
    x1 = wall_coord[0]
    x2 = wall_coord[1]
    y1 = wall_coord[2]
    y2 = wall_coord[3]
    a = (y2-y1)/(x2-x1)
    b = y1-a*x1
    return a, b