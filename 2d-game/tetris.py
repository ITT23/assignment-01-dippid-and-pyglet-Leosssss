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
SQUARE_LENGTH = 10 #length of one square
# draw a window
win = window.Window(WINDOW_WIDTH,WINDOW_HEIGHT,WINDOW_TITLE)
batch = pyglet.graphics.Batch()

# a set of colors
ORANGE = (255,155,1)
YELLOW = (255,255,1)
RED = (255,1,1)
BLUE = (1,1,255)
GREEN = (1,255,1)
# init a array with color codes, because i want to generate shapes with random color
colors = np.array([ORANGE,YELLOW,RED,BLUE,GREEN])

# init a rectangle cite from: https://pyglet.readthedocs.io/en/latest/modules/shapes.html
# square_element = shapes.Rectangle((WINDOW_WIDTH-SQUARE_LENGTH)/2, WINDOW_HEIGHT-SQUARE_LENGTH, SQUARE_LENGTH, SQUARE_LENGTH, color=colors[random.randint(0, len(colors)-1)], batch=batch)
# init 7 elements of tetris: I O L J Z S T
def create_I(color):#color = colors[random.randint(0, len(colors)-1)]
    EL_I = shapes.Rectangle((WINDOW_WIDTH-(SQUARE_LENGTH*4))/2, WINDOW_HEIGHT-SQUARE_LENGTH, SQUARE_LENGTH*4, SQUARE_LENGTH, color=color, batch=batch)

def create_O(color):
    EL_O = shapes.Rectangle((WINDOW_WIDTH-(SQUARE_LENGTH*2))/2, WINDOW_HEIGHT-SQUARE_LENGTH*2, SQUARE_LENGTH*2, SQUARE_LENGTH*2, color=color, batch=batch)

def create_L(color):
    EL_L_PART_TOP = shapes.Rectangle((WINDOW_WIDTH+(SQUARE_LENGTH))/2, WINDOW_HEIGHT-SQUARE_LENGTH, SQUARE_LENGTH, SQUARE_LENGTH, color=color, batch=batch)  
    EL_L_PART_BOTTOM = shapes.Rectangle((WINDOW_WIDTH-(SQUARE_LENGTH*3))/2, WINDOW_HEIGHT-SQUARE_LENGTH*2, SQUARE_LENGTH*3, SQUARE_LENGTH, color=color, batch=batch)  

def create_J(color):
    EL_J_PART_TOP = shapes.Rectangle((WINDOW_WIDTH-(SQUARE_LENGTH*3))/2, WINDOW_HEIGHT-SQUARE_LENGTH, SQUARE_LENGTH, SQUARE_LENGTH, color=color, batch=batch)  
    EL_J_PART_BOTTOM = shapes.Rectangle((WINDOW_WIDTH-(SQUARE_LENGTH*3))/2, WINDOW_HEIGHT-SQUARE_LENGTH*2, SQUARE_LENGTH*3, SQUARE_LENGTH, color=color, batch=batch)  

def create_Z(color):
    EL_Z_PART_TOP = shapes.Rectangle((WINDOW_WIDTH+(SQUARE_LENGTH))/2, WINDOW_HEIGHT-SQUARE_LENGTH, SQUARE_LENGTH, SQUARE_LENGTH, color=color, batch=batch)  
    EL_Z_PART_MIDDLE = shapes.Rectangle((WINDOW_WIDTH-(SQUARE_LENGTH*3))/2, WINDOW_HEIGHT-SQUARE_LENGTH*2, SQUARE_LENGTH*3, SQUARE_LENGTH, color=color, batch=batch)  
    EL_Z_PART_BOTTOM = shapes.Rectangle((WINDOW_WIDTH-(SQUARE_LENGTH*3))/2, WINDOW_HEIGHT-SQUARE_LENGTH*3, SQUARE_LENGTH, SQUARE_LENGTH, color=color, batch=batch)  

def create_S(color):
    EL_S_PART_TOP = shapes.Rectangle((WINDOW_WIDTH-(SQUARE_LENGTH*3))/2, WINDOW_HEIGHT-SQUARE_LENGTH*3, SQUARE_LENGTH, SQUARE_LENGTH, color=color, batch=batch)  
    EL_S_PART_MIDDLE = shapes.Rectangle((WINDOW_WIDTH-(SQUARE_LENGTH*3))/2, WINDOW_HEIGHT-SQUARE_LENGTH*2, SQUARE_LENGTH*3, SQUARE_LENGTH, color=color, batch=batch)  
    EL_S_PART_BOTTOM = shapes.Rectangle((WINDOW_WIDTH+(SQUARE_LENGTH))/2, WINDOW_HEIGHT-SQUARE_LENGTH, SQUARE_LENGTH, SQUARE_LENGTH, color=color, batch=batch)  

def create_T(color):
    EL_T_PART_TOP = shapes.Rectangle(((WINDOW_WIDTH-SQUARE_LENGTH)/2), WINDOW_HEIGHT-SQUARE_LENGTH, SQUARE_LENGTH, SQUARE_LENGTH, color=color, batch=batch)
    EL_T_PART_BOTTOM = shapes.Rectangle((WINDOW_WIDTH-(SQUARE_LENGTH*3))/2, WINDOW_HEIGHT-SQUARE_LENGTH*2, SQUARE_LENGTH*3, SQUARE_LENGTH, color=color, batch=batch)

def_create_list = [create_I, create_O, create_L,
                            create_J, create_Z, create_S,
                            create_T]
selected_def = random.choice(def_create_list)
selected_def(colors[random.randint(0, len(colors)-1)])

# update element position
# cite from ChatGPT. [Code segment illustrating 怎么更新rectangle的位置，每秒更新一次，高度减少 (How to update the position of a rectangle, decrease its height every second)] Retrieved from OpenAI, 2023, https://openai.com. Accessed 27 April 2023.
#def update(dt):
#    EL_S_PART_TOP.y -= 10
    
#pyglet.clock.schedule_interval(update, 0.3)

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