from pico2d import *
import game_world
import game_framework
class Bullet:
    image = None

    def __init__(self, x = 400, y = 300, velocity = 10):
        if Bullet.image == None:
            Bullet.image = load_image('resource/rockman/bullet.png')
        self.x, self.y, self.velocity = x + (50 * velocity), y + 10, velocity*5
        self.time = 0
    def get_bb(self):
        return self.x - 5, self.y -5, self.x + 5, self.y + 5

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.x += self.velocity
        self.time += game_framework.frame_time
        if self.x < 25 or self.x > 800 - 25 or self.time > 0.5:
            game_world.remove_object(self)
