from pico2d import *
import game_framework
import game_world
import random
import math

TIME_PER_ACTION = 3   # 한번 액션하는데 0.5 걸린다
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION    # 시간당 몇번 액션 할 것인가
FRAMES_PER_ACTION = 15


class Tikky:

    def __init__(self):
        self.image = load_image('resource/enemy/Tikky.png')
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.w = self.image.w
        self.h = self.image.h
        self.speed = 0
        self.frame = random.randint(0,15)
        self.left = 0
        self.x = 0
        self.y = 0
        self.off_set_x = 0

    def set_xy(self,x,y):
        self.x, self.y = x, y
    def update(self):
        self.frame = (self.frame + 15 * ACTION_PER_TIME * game_framework.frame_time) % 15
        #self.off_set()

    def set_background(self, bg):
        self.temp = bg.left
        self.bg = bg


    def set_center_object(self, player):
        self.set_center_object = player

    def draw(self):
        sx = self.x - (self.bg.left*3)
        self.image.clip_draw(0, int(self.frame) * 104, 80, 104, sx, self.y, 200, 250)


class Lightning_lord:

    def __init__(self):
        self.image = load_image('resource/enemy/cloud.png')
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.w = self.image.w
        self.h = self.image.h
        self.speed = 0
        self.frame = random.randint(0,1)
        self.left = 0
        self.x = 0
        self.y = 0
        self.off_set_x = 0
        self.r = 0
        self.velocity = 1
        self.temp_y = 0
        self.temp_x = 0

        self.TIME_PER_CIRCLE = 5.0
        self.CIRCLE_PER_TIME = 1.0 / self.TIME_PER_CIRCLE
        self.FRAMES_PER_DEGREE = 360
        self.PIXEL_PER_METER = (10.0 / 0.3)

    def set_xy(self, x, y, r, speed):
        self.x, self.y = x, y
        self.r,  self.CIRCLE_PER_TIME = r, speed
        self.temp_x, self.temp_y = self.x, self.y


    def update(self):
        self.frame = (self.frame + 2 * 0.5 * game_framework.frame_time) % 2

        #self.off_set()

    def set_background(self, bg):
        self.bg = bg

    def circle(self):
        self.velocity = (self.velocity +  self.FRAMES_PER_DEGREE *  self.CIRCLE_PER_TIME * game_framework.frame_time) % 360
        r = (self.velocity) * math.pi / 180
        self.x = self.temp_x + self.r * self.PIXEL_PER_METER * math.cos(r)
        self.y = self.temp_y + self.r * self.PIXEL_PER_METER * math.sin(r)

    def set_center_object(self, player):
        self.set_center_object = player

    def draw(self):
        self.circle()
        sx = self.x - (self.bg.left*3)
        self.image.clip_draw( int(self.frame) *40, 0, 40, 32, self.x - (self.bg.left*3), self.y, 100, 100)

class Fan_fined:

    def __init__(self):
        self.image = load_image('resource/enemy/Fan_Fined.png')
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.w = self.image.w
        self.h = self.image.h
        self.speed = 0
        self.frame = random.randint(0,8)
        self.left = 0
        self.x = 0
        self.y = 0
        self.off_set_x = 0

    def set_xy(self,x,y):
        self.x, self.y = x, y

    def update(self):
        self.frame = (self.frame + 8* ACTION_PER_TIME * game_framework.frame_time) % 8

    def set_background(self, bg):
        self.bg = bg


    def set_center_object(self, player):
        self.set_center_object = player

    def draw(self):
        sx = self.x - (self.bg.left*3)
        self.image.clip_draw(int(self.frame) * 40, 0, 40, 31, sx, self.y, 100, 90)


