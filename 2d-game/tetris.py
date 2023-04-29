import pyglet
from pyglet import window,shapes
import DIPPID
from DIPPID import SensorUDP
import numpy as np
import random
import time

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
    def update(dt):
        EL_I.y -= 10
    pyglet.clock.schedule_interval(update, 0.3)
    return EL_I

def create_O(color):
    EL_O = shapes.Rectangle((WINDOW_WIDTH-(SQUARE_LENGTH*2))/2, WINDOW_HEIGHT-SQUARE_LENGTH*2, SQUARE_LENGTH*2, SQUARE_LENGTH*2, color=color, batch=batch)
    def update(dt):
        EL_O.y -= 10
    pyglet.clock.schedule_interval(update, 0.3)
    return EL_O

def create_L(color):
    EL_L_PART_TOP = shapes.Rectangle((WINDOW_WIDTH+(SQUARE_LENGTH))/2, WINDOW_HEIGHT-SQUARE_LENGTH, SQUARE_LENGTH, SQUARE_LENGTH, color=color, batch=batch)  
    EL_L_PART_BOTTOM = shapes.Rectangle((WINDOW_WIDTH-(SQUARE_LENGTH*3))/2, WINDOW_HEIGHT-SQUARE_LENGTH*2, SQUARE_LENGTH*3, SQUARE_LENGTH, color=color, batch=batch)  
    def update(dt):
        EL_L_PART_TOP.y -= 10
        EL_L_PART_BOTTOM.y -= 10
    pyglet.clock.schedule_interval(update, 0.3)
    return EL_L_PART_TOP, EL_L_PART_BOTTOM

def create_J(color):
    EL_J_PART_TOP = shapes.Rectangle((WINDOW_WIDTH-(SQUARE_LENGTH*3))/2, WINDOW_HEIGHT-SQUARE_LENGTH, SQUARE_LENGTH, SQUARE_LENGTH, color=color, batch=batch)  
    EL_J_PART_BOTTOM = shapes.Rectangle((WINDOW_WIDTH-(SQUARE_LENGTH*3))/2, WINDOW_HEIGHT-SQUARE_LENGTH*2, SQUARE_LENGTH*3, SQUARE_LENGTH, color=color, batch=batch)  
    def update(dt):
        EL_J_PART_TOP.y -= 10
        EL_J_PART_BOTTOM.y -= 10
    pyglet.clock.schedule_interval(update, 0.3)
    return EL_J_PART_TOP, EL_J_PART_BOTTOM

def create_Z(color):
    EL_Z_PART_TOP = shapes.Rectangle((WINDOW_WIDTH+(SQUARE_LENGTH))/2, WINDOW_HEIGHT-SQUARE_LENGTH, SQUARE_LENGTH, SQUARE_LENGTH, color=color, batch=batch)  
    EL_Z_PART_MIDDLE = shapes.Rectangle((WINDOW_WIDTH-(SQUARE_LENGTH*3))/2, WINDOW_HEIGHT-SQUARE_LENGTH*2, SQUARE_LENGTH*3, SQUARE_LENGTH, color=color, batch=batch)  
    EL_Z_PART_BOTTOM = shapes.Rectangle((WINDOW_WIDTH-(SQUARE_LENGTH*3))/2, WINDOW_HEIGHT-SQUARE_LENGTH*3, SQUARE_LENGTH, SQUARE_LENGTH, color=color, batch=batch)  
    def update(dt):
            EL_Z_PART_TOP.y -= 10
            EL_Z_PART_MIDDLE.y -= 10
            EL_Z_PART_BOTTOM.y -= 10
    pyglet.clock.schedule_interval(update, 0.3)
    return EL_Z_PART_TOP, EL_Z_PART_MIDDLE, EL_Z_PART_BOTTOM

def create_S(color):
    EL_S_PART_TOP = shapes.Rectangle((WINDOW_WIDTH-(SQUARE_LENGTH*3))/2, WINDOW_HEIGHT-SQUARE_LENGTH*3, SQUARE_LENGTH, SQUARE_LENGTH, color=color, batch=batch)  
    EL_S_PART_MIDDLE = shapes.Rectangle((WINDOW_WIDTH-(SQUARE_LENGTH*3))/2, WINDOW_HEIGHT-SQUARE_LENGTH*2, SQUARE_LENGTH*3, SQUARE_LENGTH, color=color, batch=batch)  
    EL_S_PART_BOTTOM = shapes.Rectangle((WINDOW_WIDTH+(SQUARE_LENGTH))/2, WINDOW_HEIGHT-SQUARE_LENGTH, SQUARE_LENGTH, SQUARE_LENGTH, color=color, batch=batch)  
    def update(dt):
            EL_S_PART_TOP.y -= 10
            EL_S_PART_MIDDLE.y -= 10
            EL_S_PART_BOTTOM.y -= 10
    pyglet.clock.schedule_interval(update, 0.3)
    return EL_S_PART_TOP, EL_S_PART_MIDDLE, EL_S_PART_BOTTOM
    
def create_T(color):
    EL_T_PART_TOP = shapes.Rectangle(((WINDOW_WIDTH-SQUARE_LENGTH)/2), WINDOW_HEIGHT-SQUARE_LENGTH, SQUARE_LENGTH, SQUARE_LENGTH, color=color, batch=batch)
    EL_T_PART_BOTTOM = shapes.Rectangle((WINDOW_WIDTH-(SQUARE_LENGTH*3))/2, WINDOW_HEIGHT-SQUARE_LENGTH*2, SQUARE_LENGTH*3, SQUARE_LENGTH, color=color, batch=batch)
    def update(dt):
        EL_T_PART_TOP.y -= 10
        EL_T_PART_BOTTOM.y -= 10
    pyglet.clock.schedule_interval(update, 0.3)
    return EL_T_PART_TOP, EL_T_PART_BOTTOM

elements_list = ["I","O","L","J","Z","S","T"]

while True:
    create_element_index = elements_list[random.randint(0, len(elements_list)-1)]
    if create_element_index == "I": create_element = create_I(colors[random.randint(0, len(colors)-1)])
    elif create_element_index == "O": create_element = create_O(colors[random.randint(0, len(colors)-1)])
    elif create_element_index == "L": create_element = create_L(colors[random.randint(0, len(colors)-1)])
    elif create_element_index == "J": create_element = create_J(colors[random.randint(0, len(colors)-1)])
    elif create_element_index == "Z": create_element = create_Z(colors[random.randint(0, len(colors)-1)])
    elif create_element_index == "S": create_element = create_S(colors[random.randint(0, len(colors)-1)])
    elif create_element_index == "T": create_element = create_T(colors[random.randint(0, len(colors)-1)])
    
    # run the pyglet application
    @win.event
    def on_draw():
        win.clear()
        batch.draw()
    
    pyglet.app.run()

# update element position
# cite from ChatGPT. [Code segment illustrating 怎么更新rectangle的位置，每秒更新一次，高度减少 (How to update the position of a rectangle, decrease its height every second)] Retrieved from OpenAI, 2023, https://openai.com. Accessed 27 April 2023.
def update(dt):
    EL_S_PART_TOP.y -= 10
    
pyglet.clock.schedule_interval(update, 0.3)




# interact with M5 Stack cite from "demo_event.py"
#def handle_button_press(data):
#    if int(data) == 1:
#        print('button released')
#    else:
#        print('button pressed')

#sensor.register_callback('button_2', handle_button_press)