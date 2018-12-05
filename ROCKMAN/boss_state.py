import game_framework
from pico2d import *
import title_state
import airmanboss_stage

name = "BossState"
image = None
logo_time = 0.0


def enter():
    global image
    image = load_image('resource/state/boss_state.png')


def exit():
    global image
    del(image)


def update():
    global logo_time
    if(logo_time > 0.4):
        game_framework.change_state(airmanboss_stage)
        logo_time = 0
    logo_time += 0.01


def draw():
    global image
    clear_canvas()
    image.draw(400, 350)
    update_canvas()




def handle_events():
    events = get_events()
    pass


def pause(): pass


def resume(): pass




