import game_framework
from pico2d import *
import title_state


name = "WinState"
image = None



def enter():
    global image
    image = load_image('resource/state/win_state.png')


def exit():
    global image
    del(image)


def update():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RETURN):
                game_framework.change_state(title_state)


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




