import game_framework
import pico2d

import airman_stage
import start_state
import airmanboss_stage

pico2d.open_canvas(800, 700)
game_framework.run(airmanboss_stage)
pico2d.close_canvas()