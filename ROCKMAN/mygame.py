import game_framework
import pico2d

import airman_stage
import start_state

pico2d.open_canvas(800, 700)
game_framework.run(airman_stage)
pico2d.close_canvas()