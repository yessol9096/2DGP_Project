from pico2d import *


class Brick:

    def __init__(self, pos, size):
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.off_set_x = 0
        self.x,self.y = pos[0],pos[1]
        self.sizex,self.sizey = size[0],size[1]
        self.collide_check = False
    def get_bb(self):
        self.sx = self.x - (self.bg.window_left)
        return self.sx - self.sizex, self.y - self.sizey, self.sx + self.sizex, self.y + self.sizey

    def update(self):
        pass

    def set_background(self, bg):
        self.temp = bg.window_left
        self.bg = bg


    def set_center_object(self, player):
        self.set_center_object = player

    def draw(self):
        self.sx = self.x - (self.bg.window_left)
        draw_rectangle(*self.get_bb())






