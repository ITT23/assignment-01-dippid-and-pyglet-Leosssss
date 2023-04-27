import pyglet
from pyglet import window,shapes
import DIPPID
from DIPPID import SensorUDP
import numpy as np
import random

PORT = 5700
sensor = SensorUDP(PORT)

WINDOW_WIDTH = 300
WINDOW_HEIGHT = 500
WINDOW_TITLE = "Tetris"
#draw a window
win = window.Window(WINDOW_WIDTH,WINDOW_HEIGHT,WINDOW_TITLE)
batch = pyglet.graphics.Batch()

#a set of colors
ORANGE = (255,155,1)
YELLOW = (255,255,1)
RED = (255,1,1)
BLUE = (1,1,255)
GREEN = (1,255,1)
# init a array with color codes, because i want to generate shapes with random color
colors = np.array([ORANGE,YELLOW,RED,BLUE,GREEN])

# cite from: https://pyglet.readthedocs.io/en/latest/modules/shapes.html
square_element = shapes.Rectangle(WINDOW_WIDTH/2-10, WINDOW_HEIGHT-20, 20, 20, color=colors[random.randint(0, len(colors)-1)], batch=batch)

# update rectangle position
# cite from ChatGPT. [Code segment illustrating 怎么更新rectangle的位置，每秒更新一次，高度减少 (How to update the position of a rectangle, decrease its height every second)] Retrieved from OpenAI, 2023, https://openai.com. Accessed 27 April 2023.
def update(dt):
    # 每秒钟下降 50 个像素
    square_element.y -= 1
pyglet.clock.schedule_interval(update, 0.4)

# run the pyglet application
@win.event
def on_draw():
    win.clear()
    batch.draw()
pyglet.app.run()


# interact with M5 Stack cite from "demo_event.py"
#def handle_button_press(data):
#    if int(data) == 1:
#        print('button released')
#    else:
#        print('button pressed')

#sensor.register_callback('button_2', handle_button_press)