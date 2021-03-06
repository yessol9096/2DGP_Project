from pico2d import *
import random
import game_framework
from tornado import Tornado
import game_world
import math
from BehaviorTree import BehaviorTree, SelectorNode, SequenceNode, LeafNode
# Airman Run Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 10.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)


TIME_PER_ACTION = 1.0
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 0

TORNAMDO_FRAMES_PER_ACTION = 15


class Airman:

    def __init__(self, x, y):
        self.image = load_image('resource/boss/airman/airman.png')
        self.hit_image = load_image('resource/boss/hit.png')
        self.tornado_image = load_image('resource/boss/airman/tornado.png')
        self.dead_image = load_image('resource/boss/airman/airman_dead.png')
        self.canvas_width = get_canvas_width()
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.w = self.image.w
        self.h = self.image.h
        self.speed = 0
        self.frame = 0
        self.x = x
        self.y = y
        self.dir = 1
        self.damage = False
        self.time = 0
        self.cur_state = 'idle'
        self.jump_time = 0
        self.idle_time = 0
        self.hp = 28
        self.build_behavior_tree()

    def get_bb(self):
        # fill here
        return self.x - 50, self.y - 50, self.x + 50, self.y + 50

    def build_behavior_tree(self):
        jump_node = LeafNode("Jump", self.jump)
        attack_node = LeafNode("Attack", self.attack)
        idle_node = LeafNode("Idle", self.idle)
        JumpandAttack_node = SequenceNode("JumpandAttack")
        JumpandAttack_node.add_children(idle_node,jump_node, attack_node)
        self.bt = BehaviorTree(JumpandAttack_node)

    def update(self):
        self.frame = (self.frame + 15 * ACTION_PER_TIME * game_framework.frame_time) % 15
        self.bt.run()


    def idle(self):
        self.cur_state = 'idle'
        self.idle_time += game_framework.frame_time
        if (self.idle_time < 3):
            return BehaviorTree.RUNNING
        if (self.idle_time > 3):
            return BehaviorTree.SUCCESS


    def jump(self):
        self.jump_time += game_framework.frame_time
        self.cur_state = 'jump'
        r = math.pi / 180
        if(self.y >= 190):
            if(self.dir == 1):
                self.x = self.x + 5*math.cos(110*r)*self.jump_time
                self.y = self.y + (5*math.sin(110*r) - 0.98*self.jump_time*5.0)*self.jump_time
            else:
                self.x = self.x - 5 * math.cos(110 * r) * self.jump_time
                self.y = self.y + (5 * math.sin(110 * r) - 0.98 * self.jump_time * 5.0) * self.jump_time
        else:
            self.jump_time = 0
            self.y = 190
            if (self.dir == 1):
                self.dir = 0
                self.x = 200
            else:
                self.dir = 1
                self.x = 650
        if (self.y == 190):
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.FAIL

    def attack(self):
        self.cur_state = 'attack'
        self.idle_time = 0
        r = math.pi / 180
        tornado_leftpos = [(self.x + math.cos(150 * r) * 200, self.y + math.sin(150 * r) * 200),
                           (self.x + math.cos(113 * r) * 200, self.y + math.sin(113 * r) * 200),
                           (self.x + math.cos(180 * r) * 200, self.y + math.sin(180 * r) * 200),
                           (self.x + math.cos(120 * r) * 450, self.y + math.sin(120 * r) * 450),
                           (self.x + (math.cos(150 * r) * 450), self.y + (math.sin(150 * r) * 450)),
                           (self.x + (math.cos(170 * r) * 450), self.y + (math.sin(170 * r) * 450))
                           ]
        tornado_rightpos = [(self.x + math.cos(50 * r) * 200, self.y + math.sin(50 * r) * 200),
                            (self.x + math.cos(13 * r) * 200, self.y + math.sin(13 * r) * 200),
                            (self.x + math.cos(80 * r) * 200, self.y + math.sin(80 * r) * 200),
                            (self.x + math.cos(20 * r) * 450, self.y + math.sin(20 * r) * 450),
                            (self.x + (math.cos(50 * r) * 450), self.y + (math.sin(50 * r) * 450)),
                            (self.x + (math.cos(70 * r) * 450), self.y + (math.sin(70 * r) * 450))
                            ]
        if(self.dir == 1):
            tornadoes = [Tornado(tornado_leftpos[i], self.dir) for i in range(6)]

        else:
            tornadoes = [Tornado(tornado_rightpos[i], self.dir) for i in range(6)]

        game_world.add_objects(tornadoes, 3)
        return BehaviorTree.SUCCESS


    def draw(self):
        if(self.cur_state == 'idle'):
            self.image.clip_draw(0, self.dir * 40, 40, 40, self.x, self.y, 120, 120)
        elif(self.cur_state == 'attack'):
            self.image.clip_draw(160, self.dir * 40, 40, 40, self.x, self.y, 120, 120)
        elif(self.cur_state == 'jump'):
            self.image.clip_draw(40, self.dir * 40, 40, 40, self.x, self.y, 120, 120)
        elif (self.cur_state == 'dead'):
            self.dead_image.clip_draw(int(self.frame) * 170, 0, 170, 170, self.x, self.y, 120, 120)

        if(self.damage == True):
            self.hit_image.clip_draw(0, 0, 30, 30, self.x, self.y, 120, 120)
            self.time += 0.1
            if (self.time > 1.0):
                self.damage = False
                self.time = 0
