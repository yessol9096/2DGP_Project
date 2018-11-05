from pico2d import *

class Airman_background:
    def __init__(self):
        self.image = load_image('resource/stage/AirManMapBG.png')
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.w = self.image.w
        self.h = self.image.h
        self.speed = 0
        self.left = 0
        self.bottom = 483

    def update(self):
        self.left = clamp(0, int(self.set_center_object.x) - self.canvas_width // 2, self.w - self.canvas_width)
        if (self.left >= 2557 - 254 and self.bottom >= 0):
            self.left = 2557 - 254
            self.bottom -= 10
            if(self.bottom <= 0):
                self.bottom = 2
        if(self.bottom == 2):
            self.left = clamp(2303 ,int(self.set_center_object.x) - self.canvas_width // 2, self.w - self.canvas_width)

    def draw(self):
        self.image.clip_draw_to_origin(self.left,self.bottom,254,237,0,0,self.canvas_width,
                                       self.canvas_height)

    def set_center_object(self, player):
        self.set_center_object = player




