import pygame

class ball:
    def __init__(self, pos_x, pos_y, v_x, v_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.v_x = v_x
        self.v_y = v_y

    def actu_pos(self):
        self.pos_x += self.v_x
        self.pos_y += self.v_y


