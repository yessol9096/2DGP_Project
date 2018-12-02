from pico2d import *
import random

# Airman Run Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 10.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# zombie Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 0

class Airman:

    def __init__(self, x, y):
        self.image = load_image('resource/boss/airman/airman.png')
        self.hit_image = load_image('resource/boss/hit.png')
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.w = self.image.w
        self.h = self.image.h
        self.speed = 0
        self.frame = 0
        self.x = x
        self.y = y
        self.dir = 1
        self.damage = False
        self.time = 0

    def get_bb(self):
        # fill here
        return self.x - 50, self.y - 50, self.x + 50, self.y + 50

    def update(self):
        pass

    def jump(self):
        pass


    def draw(self):
        self.image.clip_draw(int(self.frame) * 40, self.dir * 40, 40, 40, self.x, self.y, 120, 120)
        if(self.damage == True):
            self.hit_image.clip_draw(0, 0, 30, 30, self.x, self.y, 120, 120)
            self.time += 0.1
            if (self.time > 1.0):
                self.damage = False
                self.time = 0
        draw_rectangle(*self.get_bb())
