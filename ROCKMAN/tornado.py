from pico2d import *
import random
import game_framework
import game_world

# Airman Run Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 10.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# zombie Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
TORNAMDO_FRAMES_PER_ACTION = 3


class Tornado:

    def __init__(self, pos, dir):
        self.tornado_image = load_image('resource/boss/airman/tornado.png')
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.speed = 0
        self.frame = 0
        self.x = pos[0]
        self.y = pos[1]
        self.dir = dir
        self.damage = False
        self.time = 0
        self.cur_state = 'attack'

    def get_bb(self):
        # fill here
        return self.x - 30, self.y - 30, self.x + 30, self.y + 30

    def update(self):
        self.frame = (self.frame + 3 * ACTION_PER_TIME * game_framework.frame_time) % 3
        self.time += game_framework.frame_time
        if(self.time > 2):
            if(self.dir == 1):
                self.x -= 1
            else:
                self.x += 1

        if self.x < 25 or self.x > 800 - 25 :
            game_world.remove_object(self)

    def draw(self):
        self.tornado_image.clip_draw(int(self.frame) * 20, self.dir * 24, 20, 24, self.x , self.y, 90, 90)
