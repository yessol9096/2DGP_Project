import game_framework
from pico2d import *
from bullet import Bullet

import game_world
from sound_manager import *

# Rockman Run Speed
# fill expressions correctly
PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 60.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

JUMP_SPEED_KMPH = 3  # Km / Hour
JUMP_SPEED_MPM = (JUMP_SPEED_KMPH * 1000.0 / 60.0)
JUMP_SPEED_MPS = (JUMP_SPEED_MPM / 60.0)
JUMP_SPEED_PPS = (JUMP_SPEED_MPS * PIXEL_PER_METER)

FALL_SPEED_KMPH = 8  # Km / Hour
FALL_SPEED_MPM = (FALL_SPEED_KMPH * 1000.0 / 60.0)
FALL_SPEED_MPS = (FALL_SPEED_MPM / 60.0)
FALL_SPEED_PPS = (FALL_SPEED_MPS * PIXEL_PER_METER)

ENTER_SPEED_KMPH = 70.0  # Km / Hour
ENTER_SPEED_MPM = (ENTER_SPEED_KMPH * 1000.0 / 60.0)
ENTER_SPEED_MPS = (ENTER_SPEED_MPM / 60.0)
ENTER_SPEED_PPS = (ENTER_SPEED_MPS * PIXEL_PER_METER)

CHAR_SIZE = 120
ENTER_EFFECT_YSIZE = 100
ENTER_EFFECT_XSIZE = ENTER_EFFECT_YSIZE * 0.85

# Rockman Action Speed
# fill expressions correctly
TIME_PER_ACTION = 0.5   # 한번 액션하는데 0.5 걸린다
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION    # 시간당 몇번 액션 할 것인가
FRAMES_PER_ACTION = 5



# Boy Event
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, SPACE, ATTACK, ATTACK_OFF, JUMP, LANDING, STARTING = range(10)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE,
    (SDL_KEYDOWN, SDLK_z): ATTACK,
    (SDL_KEYUP, SDLK_z): ATTACK_OFF,
    (SDL_KEYDOWN, SDLK_x): JUMP
}


# Boy States

class IdleState:

    @staticmethod
    def enter(rockman, event):
        rockman.now_state = 'IdleState'
        if event == RIGHT_DOWN:
            rockman.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            rockman.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            rockman.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            rockman.velocity += RUN_SPEED_PPS

        rockman.timer = get_time()

    @staticmethod
    def exit(rockman, event):
        pass


    @staticmethod
    def do(rockman):
        rockman.frame = (rockman.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3
        rockman.x = clamp(rockman.clamp_x, rockman.x, rockman.bg.w)
        rockman.y = clamp(0, rockman.y, rockman.bg.h)
        rockman.rollsecreen_set_player_pos_x()

    @staticmethod
    def draw(rockman):
        if rockman.dir == 1:
            rockman.image.clip_draw(0, 240, 40, 40, rockman.off_set_x, rockman.y, CHAR_SIZE, CHAR_SIZE)
        else:
            rockman.image.clip_draw(0, 200, 40, 40, rockman.off_set_x, rockman.y, CHAR_SIZE, CHAR_SIZE)


class RunState:

    @staticmethod
    def enter(rockman, event):
        rockman.now_state = 'RunState'
        if event == RIGHT_DOWN:
            rockman.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            rockman.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            rockman.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            rockman.velocity += RUN_SPEED_PPS
        rockman.dir = clamp(-1, rockman.velocity, 1)

    @staticmethod
    def exit(rockman, event):
        pass

    @staticmethod
    def do(rockman):
        rockman.frame = (rockman.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3
        rockman.x += rockman.velocity * game_framework.frame_time
        rockman.x = clamp(rockman.clamp_x, rockman.x, rockman.bg.w)
        rockman.y = clamp(0, rockman.y, rockman.bg.h)
        rockman.rollsecreen_set_player_pos_x()



    @staticmethod
    def draw(rockman):
        if rockman.dir == 1:
            rockman.image.clip_draw(40 + int(rockman.frame) * 40, 240, 40, 40, rockman.off_set_x, rockman.y, CHAR_SIZE, CHAR_SIZE)
        else:
            rockman.image.clip_draw(40 + int(rockman.frame) * 40, 200, 40, 40, rockman.off_set_x, rockman.y, CHAR_SIZE, CHAR_SIZE)

class Idle_attackState:

    @staticmethod
    def enter(rockman, event):
        rockman.now_state = 'Idle_attackState'
        if event == RIGHT_DOWN:
            rockman.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            rockman.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            rockman.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            rockman.velocity += RUN_SPEED_PPS
        rockman.frame = 0
        rockman.attack()

    @staticmethod
    def exit(rockman, event):
        pass

    @staticmethod
    def do(rockman):
        rockman.x = clamp(rockman.clamp_x, rockman.x, rockman.bg.w)
        rockman.y = clamp(0, rockman.y, rockman.bg.h)
    @staticmethod
    def draw(rockman):
        if rockman.dir == 1:
            rockman.image.clip_draw(0, 160, 40, 40, rockman.off_set_x, rockman.y, CHAR_SIZE, CHAR_SIZE)
        else:
            rockman.image.clip_draw(0, 120, 40, 40, rockman.off_set_x, rockman.y, CHAR_SIZE, CHAR_SIZE)

class Run_attackState:

    @staticmethod
    def enter(rockman, event):
        rockman.now_state = 'Run_attackState'
        if event == RIGHT_DOWN:
            rockman.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            rockman.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            rockman.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            rockman.velocity += RUN_SPEED_PPS
        rockman.dir = clamp(-1, rockman.velocity, 1)

        rockman.attack()

    @staticmethod
    def exit(rockman, event):
        pass

    @staticmethod
    def do(rockman):
        rockman.frame = (rockman.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3
        rockman.x += rockman.velocity * game_framework.frame_time
        rockman.x = clamp(rockman.clamp_x, rockman.x, rockman.bg.w)
        rockman.y = clamp(0, rockman.y, rockman.bg.h)

    @staticmethod
    def draw(rockman):
        if rockman.dir == 1:
            rockman.image.clip_draw(40 + int(rockman.frame) * 40, 160, 40, 40, rockman.off_set_x, rockman.y, CHAR_SIZE,
                                    CHAR_SIZE)
        else:
            rockman.image.clip_draw(40 + int(rockman.frame) * 40, 120, 40, 40, rockman.off_set_x, rockman.y, CHAR_SIZE,
                                    CHAR_SIZE)

class JumpState:
    global frame_x

    @staticmethod
    def enter(rockman, event):
        rockman.now_state = 'JumpState'
        if(rockman.jump_time == 0):
            rockman.sound_manager.jump()
        global frame_y
        frame_y = 0
        if event == RIGHT_DOWN:
            rockman.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            rockman.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            rockman.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            rockman.velocity += RUN_SPEED_PPS
        if event == ATTACK:
            rockman.attack()
            frame_y = -80
        start_time = get_time()

    @staticmethod
    def exit(rockman, event):
        pass

    @staticmethod
    def do(rockman):
        now_time = rockman.jump_time
        rockman.jump_time += game_framework.frame_time
        rockman.y += JUMP_SPEED_PPS * now_time - FALL_SPEED_PPS*0.98 * now_time * now_time
        rockman.x += rockman.velocity * game_framework.frame_time
        rockman.x = clamp(rockman.clamp_x, rockman.x, rockman.bg.w)
        rockman.y = clamp(0, rockman.y, rockman.bg.h)
        rockman.rollsecreen_set_player_pos_x()
        if(rockman.y < rockman.min_y) :
            rockman.add_event(LANDING)
            rockman.y = rockman.min_y
            rockman.jump_time = 0

    @staticmethod
    def draw(rockman):
        global frame_y
        if rockman.dir == 1:
            rockman.image.clip_draw(160, 240 + frame_y, 40, 40, rockman.off_set_x, rockman.y, CHAR_SIZE, CHAR_SIZE)
        else:
            rockman.image.clip_draw(160, 200 + frame_y, 40, 40, rockman.off_set_x, rockman.y, CHAR_SIZE, CHAR_SIZE)


class StartState:
    global frame_x
    @staticmethod
    def enter(rockman, event):
        rockman.now_state = 'StartState'
        global frame_y
        frame_y = 0
        start_time = get_time()

    @staticmethod
    def exit(rockman, event):
        pass

    @staticmethod
    def do(rockman):
        if (rockman.y > rockman.min_y):
            rockman.y -= ENTER_SPEED_PPS * game_framework.frame_time
        if(rockman.y <= rockman.min_y):
            rockman.y = rockman.min_y
            rockman.add_event(LANDING)
            rockman.sound_manager.enter_stage()
        rockman.rollsecreen_set_player_pos_x()
    @staticmethod
    def draw(rockman):
        global frame_y
        rockman.start_image.clip_draw(0, 0, 30, 35, rockman.off_set_x, rockman.y, ENTER_EFFECT_XSIZE, ENTER_EFFECT_YSIZE)


next_state_table = {
    StartState: {RIGHT_UP: StartState, LEFT_UP: StartState, RIGHT_DOWN: StartState, LEFT_DOWN: StartState, SPACE: StartState, ATTACK: StartState, ATTACK_OFF: StartState, JUMP: StartState, LANDING: IdleState, STARTING: StartState},
    IdleState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState, SPACE: IdleState, ATTACK: Idle_attackState, ATTACK_OFF: IdleState, JUMP: JumpState, STARTING: StartState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: RunState, RIGHT_DOWN: RunState, SPACE: RunState, ATTACK: Run_attackState, ATTACK_OFF: RunState, JUMP: JumpState, STARTING: StartState},
    Idle_attackState: {RIGHT_UP: Idle_attackState, LEFT_UP: Idle_attackState, LEFT_DOWN: RunState, RIGHT_DOWN: RunState, ATTACK_OFF: IdleState,ATTACK: Idle_attackState, JUMP: JumpState, STARTING: StartState},
    Run_attackState: {RIGHT_UP: Idle_attackState, LEFT_UP: Idle_attackState, LEFT_DOWN: RunState, RIGHT_DOWN: RunState, ATTACK_OFF: RunState, ATTACK: Run_attackState, JUMP: JumpState, STARTING: StartState},
    JumpState: {RIGHT_UP: JumpState, LEFT_UP: JumpState, RIGHT_DOWN: JumpState, LEFT_DOWN: JumpState, ATTACK: JumpState, ATTACK_OFF: JumpState ,JUMP:JumpState,LANDING: IdleState, STARTING: StartState}
}

class Rockman:
    start_image = None
    image = None
    def __init__(self):
        self.x, self.y =800 // 2, 1500
        # Boy is only once created, so instance image loading is fine
        if(Rockman.image == None):
            self.image = load_image('resource/rockman/rockman240x280.png')
        if (Rockman.start_image == None):
            self.start_image = load_image('resource/rockman/enter_effect_90x35.png')
        self.font = load_font('ENCR10B.TTF', 16)
        self.canvas_width = 800
        self.canvas_height = 700
        self.dir = 1
        self.velocity = 0
        self.frame = 0
        self.event_que = []
        self.cur_state = StartState
        self.cur_state.enter(self, None)
        self.jump_time = 0
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.bullet_x = 0
        self.off_set_x = 0
        self.collide_check = False
        self.min_y = 0
        self.hp = 28
        self.idle_check = True
        self.fall_check = False
        self.fall_time = 0
        self.bg = None
        self.cur_stage = 'airman_stage'
        self.clamp_x = 0
        self.now_state = 'StartState'
        self.sound_manager = None

    def rollsecreen_set_player_pos_x(self):
        if (self.cur_stage == 'airman_stage'):
            self.off_set_x = self.x - self.bg.window_left
        elif(self.cur_stage == 'airmanboss_stage'):
            self.off_set_x = self.x

    def get_bb(self):
        return self.off_set_x - 30, self.y -30, self.off_set_x + 30, self.y + 30

    def set_background(self, bg):
        self.bg = bg
        self.x = self.canvas_width / 2
        self.y = 1500

    def collide(self,collide_y):
        self.min_y = collide_y
        self.collide_check = True

    def attack(self):
        self.bullet_x =  self.off_set_x
        self.sound_manager.shot()
        bullet = Bullet(self.bullet_x, self.y, self.dir)
        game_world.add_object(bullet, 2)

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

        if (self.cur_state == IdleState):
            self.idle_check = True
        else:
            self.idle_check = False

        if (self.cur_stage == 'airmanboss_stage'):
            self.min_y = 170

        if (self.y > self.min_y and self.fall_check == True and self.cur_state != StartState and self.cur_state != JumpState):
            self.y -= 5

        if (self.y <= 0 ):
            self.y = 900
            self.x = 400
            self.add_event(STARTING)

    def draw(self):
        self.fx, self.fy = self.x - self.bg.window_left, self.y - self.bg.window_bottom
        self.cur_state.draw(self)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

    def set_sound_manager(self, sm):
        self.sound_manager = sm

