import random
import json
import os

from pico2d import *
import game_framework
import game_world

from rockman import Rockman
from airman_background import Airman_background


name = "MainState"

player = None

def enter():
    global player
    player = Rockman()
    background = Airman_background()
    background.set_center_object(player)
    game_world.add_object(background, 0)
    game_world.add_object(player, 1)


def exit():
    game_world.clear()

def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
        else:
            player.handle_event(event)


def update():
    for game_object in game_world.all_objects():
        game_object.update()
    delay(0.01)


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()






