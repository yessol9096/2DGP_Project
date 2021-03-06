import game_framework
from pico2d import *
import stage_state
from sound_manager import *

name = "StageState"
image = None
sound_manager = None


def enter():
    global image, sound_manager
    image = load_image('resource/state/title.png')
    sound_manager = Sound_Manager()
    sound_manager.title_start()


def exit():
    global image, sound_manager
    del(sound_manager)
    del(image)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RETURN):
                game_framework.change_state(stage_state)



def draw():
    clear_canvas()
    image.draw(400, 350)
    update_canvas()






def update():
    pass


def pause():
    pass


def resume():
    pass






