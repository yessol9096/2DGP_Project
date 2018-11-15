from pico2d import *
import random
import game_framework

class Airman:

    def __init__(self, pos):
        self.image = load_image('resource/enemy/Fan_Fined.png')
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.w = self.image.w
        self.h = self.image.h
        self.speed = 0
        self.frame = random.randint(0,8)
        self.left = 0
        self.x = pos[0]
        self.y = pos[1]
        self.off_set_x = 0

    def update(self):
        pass
        #self.frame = (self.frame + 8* ACTION_PER_TIME * game_framework.frame_time) % 8

    def set_background(self, bg):
        self.bg = bg


    def set_center_object(self, player):
        self.set_center_object = player

    def draw(self):
        sx = self.x - (self.bg.left*3)
        self.image.clip_draw(int(self.frame) * 40, 0, 40, 31, sx, self.y, 100, 90)