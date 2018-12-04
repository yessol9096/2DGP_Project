import random
import json
import os

from pico2d import *
import game_framework
import game_world
import gameover_state

from rockman import Rockman
from airman_background import Airman_bossbackground
from game_ui import Player_hp, Airman_hp
from airman import Airman
from sound_manager import *


player = None
player_hp = None
airman = None
airman_hp = None
sound_manager = None

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
    global player, airman, player_hp, airman_hp, sound_manager
    player = Rockman()
    airman = Airman(600, 190)
    player.clamp_x = 80
    background = Airman_bossbackground()
    background.set_center_object(player)
    sound_manager = Sound_Manager()

    player.set_background(background)
    player.cur_stage = 'airmanboss_stage'
    player_hp = Player_hp(player.hp)
    player.set_sound_manager(sound_manager)

    airman_hp = Airman_hp(airman.hp)
    sound_manager.battle_start()
    game_world.add_object(background, 0)
    game_world.add_object(player, 1)
    game_world.add_object(player_hp, 1)
    game_world.add_object(airman, 1)
    game_world.add_object(airman_hp, 1)


def exit():
    global sound_manager
    game_world.clear()
    del (sound_manager)

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
    global airman_hp, player_hp, airman, player
    for game_object in game_world.all_objects():
        game_object.update()

        # 총알과 에어맨 충돌체크
    for bullet in game_world.objects[2]:
        if collide(bullet, airman):
            airman.damage = True
            game_world.remove_object(bullet)
            airman.hp -= 1

        # 총알과 토네이도 충돌체크
    for bullet in game_world.objects[2]:
        for tornado in game_world.objects[3]:
            if collide(bullet, tornado):
                game_world.remove_object(bullet)

        # 토네이도와 플레이어 충돌
    for tornado in game_world.objects[3]:
        if collide(player, tornado):
            game_world.remove_object(tornado)
            player.hp -= 2

        # 에어맨 플레이어 충돌
    if collide(player, airman):
        player.hp -= 2
        if (player.dir == 1):
            player.x -= 10
        else:
            player.x += 10

    player_hp.hp = player.hp
    airman_hp.hp = airman.hp

    if(player.hp < 0):
        game_framework.change_state(gameover_state)



def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()