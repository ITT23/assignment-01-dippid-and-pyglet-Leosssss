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
WINDOW_TITLE = "Not Real Tetris"
SQUARE_LENGTH = 10 #length of one square
FALLING_SPEED = 10
UPDATE_INTERVAL = 0.03
NEED_NEW_ELEMENT = True

# draw a window
win = window.Window(WINDOW_WIDTH,WINDOW_HEIGHT,WINDOW_TITLE)
# init a two dimension array as playground to check if a "pixel(SQUARE_LENGTH*SQUARE_LENGTH)" is free
playground = [[0]*round(WINDOW_WIDTH/SQUARE_LENGTH) for i in range(round(WINDOW_HEIGHT/SQUARE_LENGTH))] # cite from: https://stackoverflow.com/questions/2397141/how-to-initialize-a-two-dimensional-array-in-python?page=1&tab=scoredesc#tab-top
batch = pyglet.graphics.Batch()
elements = []

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
    def update(dt): # update element position, cite from ChatGPT. [Code segment illustrating 怎么更新rectangle的位置，每秒更新一次，高度减少 (How to update the position of a rectangle, decrease its height every second)] Retrieved from OpenAI, 2023, https://openai.com. Accessed 27 April 2023.
        if EL_I.y > 0:
            if playground[len(playground)-int(EL_I.y/10)] != 0:
                EL_I.y -= FALLING_SPEED
        else: 
            updatePlayground("I", EL_I.x, EL_I.y)
            pyglet.clock.unschedule(update)
    pyglet.clock.schedule_interval(update, UPDATE_INTERVAL)
    return EL_I

def create_O(color):
    EL_O = shapes.Rectangle((WINDOW_WIDTH-(SQUARE_LENGTH*2))/2, WINDOW_HEIGHT-SQUARE_LENGTH*2, SQUARE_LENGTH*2, SQUARE_LENGTH*2, color=color, batch=batch)
    def update(dt): # update element position, cite from ChatGPT. [Code segment illustrating 怎么更新rectangle的位置，每秒更新一次，高度减少 (How to update the position of a rectangle, decrease its height every second)] Retrieved from OpenAI, 2023, https://openai.com. Accessed 27 April 2023.
        if EL_O.y > 0:
            if playground[len(playground)-int(EL_O.y/10)] != 0:
                EL_O.y -= FALLING_SPEED
        else: 
            updatePlayground("O", EL_O.x, EL_O.y)
            pyglet.clock.unschedule(update)
    pyglet.clock.schedule_interval(update, UPDATE_INTERVAL)
    return EL_O

def create_L(color):
    EL_L_PART_TOP = shapes.Rectangle((WINDOW_WIDTH+(SQUARE_LENGTH))/2, WINDOW_HEIGHT-SQUARE_LENGTH, SQUARE_LENGTH, SQUARE_LENGTH, color=color, batch=batch)  
    EL_L_PART_BOTTOM = shapes.Rectangle((WINDOW_WIDTH-(SQUARE_LENGTH*3))/2, WINDOW_HEIGHT-SQUARE_LENGTH*2, SQUARE_LENGTH*3, SQUARE_LENGTH, color=color, batch=batch)  
    def update(dt): # update element position, cite from ChatGPT. [Code segment illustrating 怎么更新rectangle的位置，每秒更新一次，高度减少 (How to update the position of a rectangle, decrease its height every second)] Retrieved from OpenAI, 2023, https://openai.com. Accessed 27 April 2023.
        if EL_L_PART_BOTTOM.y > 0:
            EL_L_PART_TOP.y -= FALLING_SPEED
            EL_L_PART_BOTTOM.y -= FALLING_SPEED
    pyglet.clock.schedule_interval(update, UPDATE_INTERVAL)
    return EL_L_PART_TOP, EL_L_PART_BOTTOM

def create_J(color):
    EL_J_PART_TOP = shapes.Rectangle((WINDOW_WIDTH-(SQUARE_LENGTH*3))/2, WINDOW_HEIGHT-SQUARE_LENGTH, SQUARE_LENGTH, SQUARE_LENGTH, color=color, batch=batch)  
    EL_J_PART_BOTTOM = shapes.Rectangle((WINDOW_WIDTH-(SQUARE_LENGTH*3))/2, WINDOW_HEIGHT-SQUARE_LENGTH*2, SQUARE_LENGTH*3, SQUARE_LENGTH, color=color, batch=batch)  
    def update(dt): # update element position, cite from ChatGPT. [Code segment illustrating 怎么更新rectangle的位置，每秒更新一次，高度减少 (How to update the position of a rectangle, decrease its height every second)] Retrieved from OpenAI, 2023, https://openai.com. Accessed 27 April 2023.
        if EL_J_PART_BOTTOM.y > 0:
            EL_J_PART_TOP.y -= FALLING_SPEED
            EL_J_PART_BOTTOM.y -= FALLING_SPEED
    pyglet.clock.schedule_interval(update, UPDATE_INTERVAL)
    return EL_J_PART_TOP, EL_J_PART_BOTTOM

def create_Z(color):
    EL_Z_PART_TOP = shapes.Rectangle((WINDOW_WIDTH+(SQUARE_LENGTH))/2, WINDOW_HEIGHT-SQUARE_LENGTH, SQUARE_LENGTH, SQUARE_LENGTH, color=color, batch=batch)  
    EL_Z_PART_MIDDLE = shapes.Rectangle((WINDOW_WIDTH-(SQUARE_LENGTH*3))/2, WINDOW_HEIGHT-SQUARE_LENGTH*2, SQUARE_LENGTH*3, SQUARE_LENGTH, color=color, batch=batch)  
    EL_Z_PART_BOTTOM = shapes.Rectangle((WINDOW_WIDTH-(SQUARE_LENGTH*3))/2, WINDOW_HEIGHT-SQUARE_LENGTH*3, SQUARE_LENGTH, SQUARE_LENGTH, color=color, batch=batch)  
    def update(dt): # update element position, cite from ChatGPT. [Code segment illustrating 怎么更新rectangle的位置，每秒更新一次，高度减少 (How to update the position of a rectangle, decrease its height every second)] Retrieved from OpenAI, 2023, https://openai.com. Accessed 27 April 2023.
        if EL_Z_PART_BOTTOM.y > 0:
            EL_Z_PART_TOP.y -= FALLING_SPEED
            EL_Z_PART_MIDDLE.y -= FALLING_SPEED
            EL_Z_PART_BOTTOM.y -= FALLING_SPEED
    pyglet.clock.schedule_interval(update, UPDATE_INTERVAL)
    return EL_Z_PART_TOP, EL_Z_PART_MIDDLE, EL_Z_PART_BOTTOM

def create_S(color):
    EL_S_PART_TOP = shapes.Rectangle((WINDOW_WIDTH-(SQUARE_LENGTH*3))/2, WINDOW_HEIGHT-SQUARE_LENGTH*3, SQUARE_LENGTH, SQUARE_LENGTH, color=color, batch=batch)  
    EL_S_PART_MIDDLE = shapes.Rectangle((WINDOW_WIDTH-(SQUARE_LENGTH*3))/2, WINDOW_HEIGHT-SQUARE_LENGTH*2, SQUARE_LENGTH*3, SQUARE_LENGTH, color=color, batch=batch)  
    EL_S_PART_BOTTOM = shapes.Rectangle((WINDOW_WIDTH+(SQUARE_LENGTH))/2, WINDOW_HEIGHT-SQUARE_LENGTH, SQUARE_LENGTH, SQUARE_LENGTH, color=color, batch=batch)  
    def update(dt): # update element position, cite from ChatGPT. [Code segment illustrating 怎么更新rectangle的位置，每秒更新一次，高度减少 (How to update the position of a rectangle, decrease its height every second)] Retrieved from OpenAI, 2023, https://openai.com. Accessed 27 April 2023.
        if EL_S_PART_BOTTOM.y > 0:
            EL_S_PART_TOP.y -= FALLING_SPEED
            EL_S_PART_MIDDLE.y -= FALLING_SPEED
            EL_S_PART_BOTTOM.y -= FALLING_SPEED
    pyglet.clock.schedule_interval(update, UPDATE_INTERVAL)
    return EL_S_PART_TOP, EL_S_PART_MIDDLE, EL_S_PART_BOTTOM
    
def create_T(color):
    EL_T_PART_TOP = shapes.Rectangle(((WINDOW_WIDTH-SQUARE_LENGTH)/2), WINDOW_HEIGHT-SQUARE_LENGTH, SQUARE_LENGTH, SQUARE_LENGTH, color=color, batch=batch)
    EL_T_PART_BOTTOM = shapes.Rectangle((WINDOW_WIDTH-(SQUARE_LENGTH*3))/2, WINDOW_HEIGHT-SQUARE_LENGTH*2, SQUARE_LENGTH*3, SQUARE_LENGTH, color=color, batch=batch)
    def update(dt): # update element position, cite from ChatGPT. [Code segment illustrating 怎么更新rectangle的位置，每秒更新一次，高度减少 (How to update the position of a rectangle, decrease its height every second)] Retrieved from OpenAI, 2023, https://openai.com. Accessed 27 April 2023.
        if EL_T_PART_BOTTOM.y > 0:
            EL_T_PART_TOP.y -= FALLING_SPEED
            EL_T_PART_BOTTOM.y -= FALLING_SPEED
    pyglet.clock.schedule_interval(update, UPDATE_INTERVAL)
    return EL_T_PART_TOP, EL_T_PART_BOTTOM

elements_list = ["I","O","L","J","Z","S","T"]

def updatePlayground(element_index, pos_x, pos_y):
    if element_index == "I":
        playground[len(playground)-1-int(pos_y/10)][int(pos_x/10)] = 1
        playground[len(playground)-1-int(pos_y/10)][int(pos_x/10)+1] = 1
        playground[len(playground)-1-int(pos_y/10)][int(pos_x/10)+2] = 1
        playground[len(playground)-1-int(pos_y/10)][int(pos_x/10)+3] = 1

 #   for i in range(len(playground)):
  #      for j in range(len(playground[i])):
   #         print(playground[i][j], end=' ')
    #    print()
        
    #print(len(playground))

def create_elements(dt):
    element_index = elements_list[random.randint(0, len(elements_list)-1)]
    if element_index == "I": create_element = create_I(colors[random.randint(0, len(colors)-1)])
    elif element_index == "O": create_element = create_O(colors[random.randint(0, len(colors)-1)])
    elif element_index == "L": create_element = create_L(colors[random.randint(0, len(colors)-1)])
    elif element_index == "J": create_element = create_J(colors[random.randint(0, len(colors)-1)])
    elif element_index == "Z": create_element = create_Z(colors[random.randint(0, len(colors)-1)])
    elif element_index == "S": create_element = create_S(colors[random.randint(0, len(colors)-1)])
    elif element_index == "T": create_element = create_T(colors[random.randint(0, len(colors)-1)])
    elements.append(create_element)

@win.event
def on_draw():
    win.clear()
    for element in elements:
        batch.draw()

pyglet.clock.schedule_interval(create_elements,5)
    
# run the pyglet application       
pyglet.app.run()





# interact with M5 Stack cite from "demo_event.py"
# def handle_button_press(data):
#    if int(data) == 1:
#        print('button released')
#    else:
#        print('button pressed')

# sensor.register_callback('button_2', handle_button_press)