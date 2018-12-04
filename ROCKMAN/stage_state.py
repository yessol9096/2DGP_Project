import game_framework
from pico2d import *
import title_state
import airman_stage

name = "StageState"
image = None
logo_time = 0.0


def enter():
    global image
    image = load_image('resource/state/stage_state.png')


def exit():
    global image
    del(image)


def update():
    global logo_time
    if(logo_time > 0.5):
        game_framework.change_state(airman_stage)
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




