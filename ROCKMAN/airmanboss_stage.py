import random
import json
import os

from pico2d import *
import game_framework
import game_world

from rockman import Rockman
from airman_background import Airman_bossbackground
from game_ui import Player_hp
from airman import Airman

player = None
player_hp = None
airman = None

def collide(a, b):
    # fill here
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

def enter():
    global player, airman
    player = Rockman()
    airman = Airman(600,190)
    player.clamp_x = 80
    background = Airman_bossbackground()
    background.set_center_object(player)

    player.set_background(background)

    player_hp = Player_hp(player.hp)

    game_world.add_object(background, 0)
    game_world.add_object(player, 1)
    game_world.add_object(player_hp, 1)
    game_world.add_object(airman, 1)


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

    for bullet in game_world.objects[2]:
        if collide(bullet, airman):
            airman.damage = True
            game_world.remove_object(bullet)



def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()