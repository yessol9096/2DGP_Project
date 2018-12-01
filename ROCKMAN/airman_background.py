from pico2d import *

import game_framework
# Backgound Animation Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 2

class Airman_background:
    def __init__(self):
        self.image = load_image('resource/stage/AirManMapBG3.png')
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.w = self.image.w
        self.h = self.image.h
        self.speed = 0
        self.window_left = 0
        self.window_bottom = 0
        self.frame = 0
    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION
        self.window_left = clamp(0, int(self.set_center_object.x) - self.canvas_width // 2, self.w - self.canvas_width)

    def draw(self):
        self.image.clip_draw_to_origin(self.window_left,int(self.frame) * 700 ,self.canvas_width,self.canvas_width,0,0)


    def set_center_object(self, player):
        self.set_center_object = player






