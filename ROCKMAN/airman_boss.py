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
tikkys_position = [(1000,300), (1550, 250), (2050, 350), (2550, 330), (3050, 330), (7950, 330), (8350, 360)]
lightning_lord_position = [(3800,350,8,8), (4100, 350, 6, 6), (4600, 350, 5, 4), (5000, 350, 5, 5)]
fan_fineds_position = [(9600,465), (11500,465), (11750, 557)]
player = None

def enter():
    global player
    player = Rockman()

    # 적 생성, 위치조정
    tikkys = [Tikky(tikkys_position[i]) for i in range(7)]
    lightning_lords = [Lightning_lord(lightning_lord_position[i]) for i in range(4)]
    fan_fineds = [Fan_fined(fan_fineds_position[i]) for i in range(3)]

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