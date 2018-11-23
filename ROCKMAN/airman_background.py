from pico2d import *

class Airman_background:
    def __init__(self):
        self.image = load_image('resource/stage/AirManMapBG2.png')
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.w = self.image.w
        self.h = self.image.h
        self.speed = 0
        self.window_left = 0
        self.window_bottom = 0

    def update(self):
        self.window_left = clamp(0, int(self.set_center_object.x) - self.canvas_width // 2, self.w - self.canvas_width)

    def draw(self):
        self.image.clip_draw_to_origin(self.window_left,self.window_bottom,self.canvas_width, self.canvas_height,0,0)


    def set_center_object(self, player):
        self.set_center_object = player




