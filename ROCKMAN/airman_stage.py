import random
import json
import os

from pico2d import *
import game_framework
import game_world

from rockman import Rockman
from airman_background import Airman_background
from ariman_enemy import Tikky, Lightning_lord, Fan_fined


name = "MainState"

player = None

def enter():
    global player
    player = Rockman()
    tikkys = [Tikky() for i in range(7)]
    tikkys[0].set_xy(1000, 300)
    tikkys[1].set_xy(1550, 250)
    tikkys[2].set_xy(2050, 350)
    tikkys[3].set_xy(2550, 330)
    tikkys[4].set_xy(3050, 330)
    tikkys[5].set_xy(7950, 330)
    tikkys[6].set_xy(8350, 360)

    lightning_lords = [Lightning_lord() for i in range(4)]
    lightning_lords[0].set_xy(3800,350,8,0.08)
    lightning_lords[1].set_xy(4100, 350, 6, 0.06)
    lightning_lords[2].set_xy(4600, 350, 5, 0.04)
    lightning_lords[3].set_xy(5000, 350, 5, 0.05)

    fan_fineds = [Fan_fined() for i in range(3)]
    fan_fineds[0].set_xy(9600,465)
    fan_fineds[1].set_xy(11500,465)
    fan_fineds[2].set_xy(11750, 557)
    background = Airman_background()
    background.set_center_object(player)

    for tikky in tikkys:
        tikky.set_background(background)
        tikky.set_center_object(player)

    for lightning_lord in lightning_lords:
        lightning_lord.set_background(background)

    for fan_fined in fan_fineds:
        fan_fined.set_background(background)
    player.set_background(background)


    game_world.add_object(background, 0)
    game_world.add_objects(tikkys, 0)
    game_world.add_objects(lightning_lords, 1)
    game_world.add_objects(fan_fineds, 1)
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






