import pyglet
from pyglet import window,shapes
import DIPPID
from DIPPID import SensorUDP
import numpy as np

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
#init a array with color codes
colors = np.array([ORANGE,YELLOW,RED,BLUE,GREEN])


#cite from "demo_event.py"
#def handle_button_press(data):
#    if int(data) == 1:
#        print('button released')
#    else:
#        print('button pressed')

#sensor.register_callback('button_2', handle_button_press)

#cite from: https://pyglet.readthedocs.io/en/latest/modules/shapes.html
square_element = square = shapes.Rectangle(200, 200, 200, 200, color=(55, 55, 255), batch=batch)

@win.event
def on_draw():
    win.clear()
    batch.draw()
 
# run the pyglet application
pyglet.app.run()