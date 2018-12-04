import game_framework
import pico2d

import airman_stage
import title_state
import airmanboss_stage
import boss_state

pico2d.open_canvas(800, 700)
game_framework.run(title_state)
pico2d.close_canvas()