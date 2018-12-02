from pico2d import *
import random
import game_framework
from tornado import Tornado
import game_world
import math

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

TORNAMDO_FRAMES_PER_ACTION = 3


class Airman:

    def __init__(self, x, y):
        self.image = load_image('resource/boss/airman/airman.png')
        self.hit_image = load_image('resource/boss/hit.png')
        self.tornado_image = load_image('resource/boss/airman/tornado.png')
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.w = self.image.w
        self.h = self.image.h
        self.speed = 0
        self.frame = 0
        self.x = x
        self.y = y
        self.dir = 0
        self.damage = False
        self.time = 0
        self.cur_state = 'attack'

    def get_bb(self):
        # fill here
        return self.x - 50, self.y - 50, self.x + 50, self.y + 50

    def update(self):
        self.frame = (self.frame + 3 * ACTION_PER_TIME * game_framework.frame_time) % 3

    def jump(self):
        pass

    def attack(self):
        r = math.pi / 180
        tornado_leftpos=[(self.x + math.cos(150*r)*200 , self.y + math.sin(150*r)*200),
                     (self.x + math.cos(120*r)*200 ,  self.y + math.sin(120*r)*200),
                     (self.x + math.cos(180*r) * 200, self.y + math.sin(180*r) * 200),
                     (self.x + math.cos(120 * r) * 450, self.y + math.sin(120 * r) * 450),
                     (self.x + (math.cos(150 * r) * 450), self.y + (math.sin(150 * r) * 450)),
                     (self.x + (math.cos(170 * r) * 450), self.y + (math.sin(170 * r) * 450))
                     ]
        tornado_rightpos = [(self.x + math.cos(50 * r) * 200, self.y + math.sin(50 * r) * 200),
                           (self.x + math.cos(20 * r) * 200, self.y + math.sin(20 * r) * 200),
                           (self.x + math.cos(80 * r) * 200, self.y + math.sin(80 * r) * 200),
                           (self.x + math.cos(20 * r) * 450, self.y + math.sin(20 * r) * 450),
                           (self.x + (math.cos(50 * r) * 450), self.y + (math.sin(50 * r) * 450)),
                           (self.x + (math.cos(70 * r) * 450), self.y + (math.sin(70 * r) * 450))
                           ]
        if(self.dir == 1):
            tornadoes = [Tornado(tornado_leftpos[i], self.dir) for i in range(6)]
        else:
            tornadoes = [Tornado(tornado_rightpos[i], self.dir) for i in range(6)]
        game_world.add_objects(tornadoes, 4)

    def draw(self):
        if(self.cur_state == 'idle'):
            self.image.clip_draw(0, self.dir * 40, 40, 40, self.x, self.y, 120, 120)
        elif(self.cur_state == 'attack'):
            self.image.clip_draw(160, self.dir * 40, 40, 40, self.x, self.y, 120, 120)
        if(self.damage == True):
            self.hit_image.clip_draw(0, 0, 30, 30, self.x, self.y, 120, 120)
            self.time += 0.1
            if (self.time > 1.0):
                self.damage = False
                self.time = 0
        draw_rectangle(*self.get_bb())
