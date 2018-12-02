from pico2d import *
import game_world

class Player_hp:
    bar_image = None
    tic_image = None
    BAR_IMAGE_WIDTH = 8  # 바 원본이미지 크기
    BAR_IMAGE_HEIGHT = 56
    TIC_IMAGE_WIDTH = 6  # 틱 원본이미지 크기
    TIC_IMAGE_HEIGHT = 2

    BAR_WIDTH = BAR_IMAGE_WIDTH * 3  # 바 크기
    BAR_HEIGHT = BAR_IMAGE_HEIGHT * 3
    TIC_WIDTH = TIC_IMAGE_WIDTH * 3  # 틱 크기
    TIC_HEIGHT = TIC_IMAGE_HEIGHT * 3

    def __init__(self, hp):
        if Player_hp.bar_image == None:
            Player_hp.bar_image = load_image('resource/ui/hp_bar.png')
        if Player_hp.tic_image == None:
            Player_hp.tic_image = load_image('resource/ui/hp_tic.png')
        self.hp = hp
        self.x, self.y = 70,600

    def draw(self):
        self.bar_image.draw(self.x, self.y, self.BAR_WIDTH, self.BAR_HEIGHT)
        for i in range(0, self.hp):
            self.tic_image.draw(self.x, self.y - self.BAR_HEIGHT // 2 + 3 + (6 * i), self.TIC_WIDTH, self.TIC_HEIGHT)

    def update(self):
        pass

class Airman_hp:
    bar_image = None
    tic_image = None
    BAR_IMAGE_WIDTH = 8  # 바 원본이미지 크기
    BAR_IMAGE_HEIGHT = 56
    TIC_IMAGE_WIDTH = 6  # 틱 원본이미지 크기
    TIC_IMAGE_HEIGHT = 2

    BAR_WIDTH = BAR_IMAGE_WIDTH * 3  # 바 크기
    BAR_HEIGHT = BAR_IMAGE_HEIGHT * 3
    TIC_WIDTH = TIC_IMAGE_WIDTH * 3  # 틱 크기
    TIC_HEIGHT = TIC_IMAGE_HEIGHT * 3

    def __init__(self, hp):
        if Airman_hp.bar_image == None:
            Airman_hp.bar_image = load_image('resource/ui/hp_bar1.png')
        if Airman_hp.tic_image == None:
            Airman_hp.tic_image = load_image('resource/ui/airman_tic.png')
        self.hp = hp
        self.x, self.y = 100,600

    def draw(self):
        self.bar_image.draw(self.x, self.y, self.BAR_WIDTH, self.BAR_HEIGHT)
        for i in range(0, self.hp):
            self.tic_image.draw(self.x, self.y - self.BAR_HEIGHT // 2 + 3 + (6 * i), self.TIC_WIDTH, self.TIC_HEIGHT)

    def update(self):
        pass
