from pico2d import *
import game_world

class Bullet:
    image = None

    def __init__(self, x = 400, y = 300, velocity = 10):
        if Bullet.image == None:
            Bullet.image = load_image('resource/rockman/bullet.png')
        self.x, self.y, self.velocity = x + (50 * velocity), y + 10, velocity*5

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.x += self.velocity

        if self.x < 25 or self.x > 800 - 25:
            game_world.remove_object(self)
