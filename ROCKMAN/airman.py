from pico2d import *
import random

class Airman:

    def __init__(self, pos):
        self.image = load_image('resource/enemy/Tikky.png')
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.w = self.image.w
        self.h = self.image.h
        self.speed = 0
        self.frame = random.randint(0,15)
        self.left = 0
        self.x = pos[0]
        self.y = pos[1]
        self.off_set_x = 0

    def get_bb(self):
        # fill here
        return self.sx - 100, self.y - 100, self.sx + 100, self.y + 85

    def update(self):
        pass

    def set_background(self, bg):
        self.temp = bg.left
        self.bg = bg


    def set_center_object(self, player):
        self.set_center_object = player

    def draw(self):
        self.sx = self.x - (self.bg.left*3)
        self.image.clip_draw(0, int(self.frame) * 104, 80, 104, self.sx, self.y, 200, 250)
        draw_rectangle(*self.get_bb())
