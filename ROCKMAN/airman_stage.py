import random
import json
import os

from pico2d import *
import game_framework
import game_world

from rockman import Rockman
from airman_background import Airman_stagebackground
from ariman_enemy import Tikky, Cloud, Fan_fined
from airman_brick import Brick
from game_ui import Player_hp


name = "MainState"
tikkys_position = [(950,300), (1500, 250), (2000, 350), (2450, 330), (2900, 330), (7900, 330), (8270, 360)]
cloud_position = [(3500,350,4,8), (3800, 350, 6, 6), (4200, 350, 5, 4), (4500, 350, 4, 5),(4800, 350, 5, 6) ,(5100, 400, 4, 8)]
fan_fineds_position = [(8400,480), (11210,480), (11750, 570)]
bricks_num = 24
bricks_position = [(345,325), (1225, 415), (1730,415), (2255,455) ,(2735,415), (3238,415), (6415,325),(7730,325),(8105,325), (8375,410), (8570,500)
                   ,(8800, 325),(9140,325),(9430,325),(9640,325),(9860,325),(10090,325),(10230,415),(10500,500),(10900,325),(11200,415), (11430,500), (11710,500),(12175,325)]
bricks_size = [(400,20), (46,20), (23,20), (23,20), (23,20), (69,20), (1100, 20), (115,20), (160, 20),(90,20),(90,20), (135, 20),(90,20),(90,20),(23,20),(90,20),(43,20)
               ,(85,10),(160,10),(135,20),(85,10),(85,20),(85,20),(355,20)]
player = None
testx = 400
tikkys = []
clouds= []
fan_fineds = []
bricks= []
player_hp = None
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
    global player, bricks_num, player_hp
    player = Rockman()
    global tikkys, lightning_lords, fan_fineds, bricks
    # 적 생성, 위치조정
    tikkys = [Tikky(tikkys_position[i]) for i in range(5)]
    clouds = [Cloud(cloud_position[i]) for i in range(6)]
    fan_fineds = [Fan_fined(fan_fineds_position[i]) for i in range(3)]
    bricks = [Brick(bricks_position[i],bricks_size[i]) for i in range(bricks_num)]
    background = Airman_stagebackground()
    background.set_center_object(player)

    player.clamp_x = 0
    player.cur_stae = 'airman_stage'

    for tikky in tikkys:
        tikky.set_background(background)
        tikky.set_center_object(player)

    for cloud in clouds:
        cloud.set_background(background)

    for fan_fined in fan_fineds:
        fan_fined.set_background(background)

    for brick in bricks:
        brick.set_background(background)

    player.set_background(background)

    player_hp = Player_hp(player.hp)


    game_world.add_object(background, 0)
    game_world.add_objects(tikkys, 1)
    game_world.add_objects(clouds, 1)
    game_world.add_objects(bricks, 1)
    game_world.add_objects(fan_fineds, 3)
    game_world.add_object(player, 3)
    game_world.add_object(player_hp, 3)

    player.x = testx
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

    for obj in game_world.objects[1]:
        if collide(player, obj):
            if (obj.name == Cloud):
                #if (player.idle_check == True):
                player.x = obj.x
                player.y,player.min_y = obj.y+50,obj.y+50
                #player.fall_check = False
            else:
                player.min_y = obj.collide_y
            break
        else:
            player.min_y = -200
            player.fall_check = True


    # fan_fined 와 bullet 충돌처리
    for bullet in game_world.objects[2]:
        for fan_fined in fan_fineds:
            if collide(bullet, fan_fined):
                fan_fined.damage = True
                game_world.remove_object(bullet)
                fan_fined.hp -= 10


    for fan_fined in fan_fineds:
        if(fan_fined.hp < 0):
            game_world.remove_object(fan_fined)
        if collide(player, fan_fined):
            player.hp -= 1

    player_hp.hp = player.hp





def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()






