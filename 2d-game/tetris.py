import pyglet
from pyglet import window,shapes
from DIPPID import SensorUDP
import numpy as np
import random

PORT = 5700
WINDOW_WIDTH = 300
WINDOW_HEIGHT = 400
WINDOW_TITLE = "Not Real Tetris, Draw a Picture with Tetris Element!"
SQUARE_LENGTH = 10 #length of one square
START_POS_X = (WINDOW_WIDTH-(SQUARE_LENGTH*4))/2
FALLING_SPEED = 10
MOVING_SPEED = 10
UPDATE_INTERVAL = 0.05
# a set of colors
ORANGE = (255,155,1)
YELLOW = (255,255,1)
RED = (255,1,1)
BLUE = (1,1,255)
GREEN = (1,255,1)
# init a array with color codes, because i want to generate shapes with random color
colors = np.array([ORANGE,YELLOW,RED,BLUE,GREEN])
sensor = SensorUDP(PORT)

# draw a window
win = window.Window(WINDOW_WIDTH,WINDOW_HEIGHT,WINDOW_TITLE)
# init a two dimension array as playground to check if a "pixel(SQUARE_LENGTH*SQUARE_LENGTH)" is free
playground = [[0]*round(WINDOW_WIDTH/SQUARE_LENGTH) for i in range(round(WINDOW_HEIGHT/SQUARE_LENGTH))] # cite from: https://stackoverflow.com/questions/2397141/how-to-initialize-a-two-dimensional-array-in-python?page=1&tab=scoredesc#tab-top
batch = pyglet.graphics.Batch()
elements = []
moving_left = False
moving_right = False

# init a rectangle cite from: https://pyglet.readthedocs.io/en/latest/modules/shapes.html
# square_element = shapes.Rectangle((WINDOW_WIDTH-SQUARE_LENGTH)/2, WINDOW_HEIGHT-SQUARE_LENGTH, SQUARE_LENGTH, SQUARE_LENGTH, color=colors[random.randint(0, len(colors)-1)], batch=batch)
# init 7 elements of tetris: I O L J Z S T
def create_I(color):#color = colors[random.randint(0, len(colors)-1)]
    EL_I = shapes.Rectangle(START_POS_X, WINDOW_HEIGHT-SQUARE_LENGTH, SQUARE_LENGTH*4, SQUARE_LENGTH, color=color, batch=batch)
    def update(dt): # update element position, cite from ChatGPT. [Code segment illustrating 怎么更新rectangle的位置，每秒更新一次，高度减少 (How to update the position of a rectangle, decrease its height every second)] Retrieved from OpenAI, 2023, https://openai.com. Accessed 27 April 2023.
        if EL_I.y > 0: 
            if int(EL_I.y/10)>0 and playground[len(playground)-int(EL_I.y/10)][int(EL_I.x/10)] != 1 and int(EL_I.y/10)>0 and playground[len(playground)-int(EL_I.y/10)][int(EL_I.x/10)+1] != 1 and int(EL_I.y/10)>0 and playground[len(playground)-int(EL_I.y/10)][int(EL_I.x/10)+2] != 1 and int(EL_I.y/10)>0 and playground[len(playground)-int(EL_I.y/10)][int(EL_I.x/10)+3] != 1:
                EL_I.y -= FALLING_SPEED
                if moving_left and EL_I.x > 0 and playground[len(playground)-int(EL_I.y/10)-1][int(EL_I.x/10)-1] != 1:
                    EL_I.x -= MOVING_SPEED
                if moving_right and EL_I.x < WINDOW_WIDTH-SQUARE_LENGTH*4 and playground[len(playground)-int(EL_I.y/10)-1][int(EL_I.x/10)+4] != 1:
                    EL_I.x += MOVING_SPEED
            else: 
                updatePlayground("I", EL_I.x, EL_I.y, EL_I.width)
                pyglet.clock.unschedule(update)
        else: 
            updatePlayground("I", EL_I.x, EL_I.y, EL_I.width)
            pyglet.clock.unschedule(update)
    pyglet.clock.schedule_interval(update, UPDATE_INTERVAL)
    
    return EL_I

def create_O(color):
    EL_O = shapes.Rectangle(START_POS_X, WINDOW_HEIGHT-SQUARE_LENGTH*2, SQUARE_LENGTH*2, SQUARE_LENGTH*2, color=color, batch=batch)
    print(EL_O.position)
    def update(dt): # update element position, cite from ChatGPT. [Code segment illustrating 怎么更新rectangle的位置，每秒更新一次，高度减少 (How to update the position of a rectangle, decrease its height every second)] Retrieved from OpenAI, 2023, https://openai.com. Accessed 27 April 2023.
        if EL_O.y > 0:
            if playground[len(playground)-int(EL_O.y/10)][int(EL_O.x/10)] != 1 and playground[len(playground)-int(EL_O.y/10)][int(EL_O.x/10)+1] != 1:
                EL_O.y -= FALLING_SPEED
                if moving_left and EL_O.x > 0 and playground[len(playground)-int(EL_O.y/10)-1][int(EL_O.x/10)-1] != 1 and playground[len(playground)-int(EL_O.y/10)-2][int(EL_O.x/10)-1] != 1:
                    EL_O.x -= MOVING_SPEED
                if moving_right and EL_O.x < WINDOW_WIDTH-SQUARE_LENGTH*2 and playground[len(playground)-int(EL_O.y/10)-1][int(EL_O.x/10)+2] != 1 and playground[len(playground)-int(EL_O.y/10)-2][int(EL_O.x/10)+2] != 1:
                    EL_O.x += MOVING_SPEED
            else: 
                updatePlayground("O", EL_O.x, EL_O.y, EL_O.width)
                pyglet.clock.unschedule(update)
        else: 
            updatePlayground("O", EL_O.x, EL_O.y, EL_O.width)
            pyglet.clock.unschedule(update)
    pyglet.clock.schedule_interval(update, UPDATE_INTERVAL)
    return EL_O

def create_L(color):
    EL_L_PART_TOP = shapes.Rectangle(START_POS_X+SQUARE_LENGTH*2, WINDOW_HEIGHT-SQUARE_LENGTH, SQUARE_LENGTH, SQUARE_LENGTH, color=color, batch=batch)  
    EL_L_PART_BOTTOM = shapes.Rectangle(START_POS_X, WINDOW_HEIGHT-SQUARE_LENGTH*2, SQUARE_LENGTH*3, SQUARE_LENGTH, color=color, batch=batch)  
    def update(dt): # update element position, cite from ChatGPT. [Code segment illustrating 怎么更新rectangle的位置，每秒更新一次，高度减少 (How to update the position of a rectangle, decrease its height every second)] Retrieved from OpenAI, 2023, https://openai.com. Accessed 27 April 2023.
        if EL_L_PART_BOTTOM.y > 0:
            if playground[len(playground)-int(EL_L_PART_BOTTOM.y/10)][int(EL_L_PART_BOTTOM.x/10)] != 1 and playground[len(playground)-int(EL_L_PART_BOTTOM.y/10)][int(EL_L_PART_BOTTOM.x/10)+1] != 1 and playground[len(playground)-int(EL_L_PART_BOTTOM.y/10)][int(EL_L_PART_BOTTOM.x/10)+2] != 1:
                EL_L_PART_TOP.y -= FALLING_SPEED
                EL_L_PART_BOTTOM.y -= FALLING_SPEED
                if moving_left and EL_L_PART_BOTTOM.x > 0 and playground[len(playground)-int(EL_L_PART_BOTTOM.y/10)-1][int(EL_L_PART_BOTTOM.x/10)-1] != 1 and playground[len(playground)-int(EL_L_PART_TOP.y/10)-1][int(EL_L_PART_TOP.x/10)-1] != 1:
                    EL_L_PART_TOP.x -= MOVING_SPEED
                    EL_L_PART_BOTTOM.x -= MOVING_SPEED
                if moving_right and EL_L_PART_BOTTOM.x < WINDOW_WIDTH-SQUARE_LENGTH*3 and playground[len(playground)-int(EL_L_PART_BOTTOM.y/10)-1][int(EL_L_PART_BOTTOM.x/10)+3] != 1 and playground[len(playground)-int(EL_L_PART_TOP.y/10)-1][int(EL_L_PART_TOP.x/10)+1] != 1:
                    EL_L_PART_TOP.x += MOVING_SPEED
                    EL_L_PART_BOTTOM.x += MOVING_SPEED
            else: 
                updatePlayground("L", EL_L_PART_BOTTOM.x, EL_L_PART_BOTTOM.y, EL_L_PART_BOTTOM.width)
                pyglet.clock.unschedule(update)
        else: 
            updatePlayground("L", EL_L_PART_BOTTOM.x, EL_L_PART_BOTTOM.y, EL_L_PART_BOTTOM.width)
            pyglet.clock.unschedule(update)
    pyglet.clock.schedule_interval(update, UPDATE_INTERVAL)
    return EL_L_PART_TOP, EL_L_PART_BOTTOM

def create_J(color):
    EL_J_PART_TOP = shapes.Rectangle(START_POS_X, WINDOW_HEIGHT-SQUARE_LENGTH, SQUARE_LENGTH, SQUARE_LENGTH, color=color, batch=batch)  
    EL_J_PART_BOTTOM = shapes.Rectangle(START_POS_X, WINDOW_HEIGHT-SQUARE_LENGTH*2, SQUARE_LENGTH*3, SQUARE_LENGTH, color=color, batch=batch)  
    def update(dt): # update element position, cite from ChatGPT. [Code segment illustrating 怎么更新rectangle的位置，每秒更新一次，高度减少 (How to update the position of a rectangle, decrease its height every second)] Retrieved from OpenAI, 2023, https://openai.com. Accessed 27 April 2023.
        if EL_J_PART_BOTTOM.y > 0:
            if playground[len(playground)-int(EL_J_PART_BOTTOM.y/10)][int(EL_J_PART_BOTTOM.x/10)] != 1 and playground[len(playground)-int(EL_J_PART_BOTTOM.y/10)][int(EL_J_PART_BOTTOM.x/10)+1] != 1 and playground[len(playground)-int(EL_J_PART_BOTTOM.y/10)][int(EL_J_PART_BOTTOM.x/10)+2] != 1:
                EL_J_PART_TOP.y -= FALLING_SPEED
                EL_J_PART_BOTTOM.y -= FALLING_SPEED
                if moving_left and EL_J_PART_BOTTOM.x > 0 and playground[len(playground)-int(EL_J_PART_BOTTOM.y/10)-1][int(EL_J_PART_BOTTOM.x/10)-1] != 1 and playground[len(playground)-int(EL_J_PART_TOP.y/10)-1][int(EL_J_PART_TOP.x/10)-1] != 1:
                    EL_J_PART_TOP.x -= MOVING_SPEED
                    EL_J_PART_BOTTOM.x -= MOVING_SPEED
                if moving_right and EL_J_PART_BOTTOM.x < WINDOW_WIDTH-SQUARE_LENGTH*3 and playground[len(playground)-int(EL_J_PART_BOTTOM.y/10)-1][int(EL_J_PART_BOTTOM.x/10)+3] != 1 and playground[len(playground)-int(EL_J_PART_TOP.y/10)-1][int(EL_J_PART_TOP.x/10)+1] != 1:
                    EL_J_PART_TOP.x += MOVING_SPEED
                    EL_J_PART_BOTTOM.x += MOVING_SPEED
            else: 
                updatePlayground("J", EL_J_PART_BOTTOM.x, EL_J_PART_BOTTOM.y, EL_J_PART_BOTTOM.width)
                pyglet.clock.unschedule(update)
        else: 
            updatePlayground("J", EL_J_PART_BOTTOM.x, EL_J_PART_BOTTOM.y, EL_J_PART_BOTTOM.width)
            pyglet.clock.unschedule(update)
    pyglet.clock.schedule_interval(update, UPDATE_INTERVAL)
    return EL_J_PART_TOP, EL_J_PART_BOTTOM

def create_Z(color):
    EL_Z_PART_TOP = shapes.Rectangle(START_POS_X+SQUARE_LENGTH*2, WINDOW_HEIGHT-SQUARE_LENGTH, SQUARE_LENGTH, SQUARE_LENGTH, color=color, batch=batch)  
    EL_Z_PART_MIDDLE = shapes.Rectangle(START_POS_X, WINDOW_HEIGHT-SQUARE_LENGTH*2, SQUARE_LENGTH*3, SQUARE_LENGTH, color=color, batch=batch)  
    EL_Z_PART_BOTTOM = shapes.Rectangle(START_POS_X, WINDOW_HEIGHT-SQUARE_LENGTH*3, SQUARE_LENGTH, SQUARE_LENGTH, color=color, batch=batch)  
    def update(dt): # update element position, cite from ChatGPT. [Code segment illustrating 怎么更新rectangle的位置，每秒更新一次，高度减少 (How to update the position of a rectangle, decrease its height every second)] Retrieved from OpenAI, 2023, https://openai.com. Accessed 27 April 2023.
        if EL_Z_PART_BOTTOM.y > 0:
            if playground[len(playground)-int(EL_Z_PART_BOTTOM.y/10)][int(EL_Z_PART_BOTTOM.x/10)] != 1 and playground[len(playground)-int(EL_Z_PART_MIDDLE.y/10)][int(EL_Z_PART_MIDDLE.x/10)+1] != 1 and playground[len(playground)-int(EL_Z_PART_MIDDLE.y/10)][int(EL_Z_PART_MIDDLE.x/10)+2] != 1:
                EL_Z_PART_TOP.y -= FALLING_SPEED
                EL_Z_PART_MIDDLE.y -= FALLING_SPEED
                EL_Z_PART_BOTTOM.y -= FALLING_SPEED
                if moving_left and EL_Z_PART_MIDDLE.x > 0 and playground[len(playground)-int(EL_Z_PART_MIDDLE.y/10)-1][int(EL_Z_PART_MIDDLE.x/10)-1] != 1 and playground[len(playground)-int(EL_Z_PART_TOP.y/10)-1][int(EL_Z_PART_TOP.x/10)-1] != 1 and playground[len(playground)-int(EL_Z_PART_BOTTOM.y/10)-1][int(EL_Z_PART_BOTTOM.x/10)-1] != 1:
                    EL_Z_PART_TOP.x -= MOVING_SPEED
                    EL_Z_PART_MIDDLE.x -= MOVING_SPEED
                    EL_Z_PART_BOTTOM.x -= MOVING_SPEED
                if moving_right and EL_Z_PART_MIDDLE.x < WINDOW_WIDTH-SQUARE_LENGTH*3 and playground[len(playground)-int(EL_Z_PART_MIDDLE.y/10)-1][int(EL_Z_PART_MIDDLE.x/10)+3] != 1 and playground[len(playground)-int(EL_Z_PART_TOP.y/10)-1][int(EL_Z_PART_TOP.x/10)+1] != 1 and playground[len(playground)-int(EL_Z_PART_BOTTOM.y/10)-1][int(EL_Z_PART_BOTTOM.x/10)+1] != 1:
                    EL_Z_PART_TOP.x += MOVING_SPEED
                    EL_Z_PART_MIDDLE.x += MOVING_SPEED
                    EL_Z_PART_BOTTOM.x += MOVING_SPEED
            else: 
                updatePlayground("Z", EL_Z_PART_MIDDLE.x, EL_Z_PART_MIDDLE.y, EL_Z_PART_MIDDLE.width)
                pyglet.clock.unschedule(update)
        else: 
            updatePlayground("Z", EL_Z_PART_MIDDLE.x, EL_Z_PART_MIDDLE.y, EL_Z_PART_MIDDLE.width)
            pyglet.clock.unschedule(update)
    pyglet.clock.schedule_interval(update, UPDATE_INTERVAL)
    return EL_Z_PART_TOP, EL_Z_PART_MIDDLE, EL_Z_PART_BOTTOM

def create_S(color):
    EL_S_PART_TOP = shapes.Rectangle(START_POS_X, WINDOW_HEIGHT-SQUARE_LENGTH, SQUARE_LENGTH, SQUARE_LENGTH, color=color, batch=batch)  
    EL_S_PART_MIDDLE = shapes.Rectangle(START_POS_X, WINDOW_HEIGHT-SQUARE_LENGTH*2, SQUARE_LENGTH*3, SQUARE_LENGTH, color=color, batch=batch)  
    EL_S_PART_BOTTOM = shapes.Rectangle(START_POS_X+SQUARE_LENGTH*2, WINDOW_HEIGHT-SQUARE_LENGTH*3, SQUARE_LENGTH, SQUARE_LENGTH, color=color, batch=batch)  
    def update(dt): # update element position, cite from ChatGPT. [Code segment illustrating 怎么更新rectangle的位置，每秒更新一次，高度减少 (How to update the position of a rectangle, decrease its height every second)] Retrieved from OpenAI, 2023, https://openai.com. Accessed 27 April 2023.
        if EL_S_PART_BOTTOM.y > 0:
            if playground[len(playground)-int(EL_S_PART_BOTTOM.y/10)][int(EL_S_PART_BOTTOM.x/10)] != 1 and playground[len(playground)-int(EL_S_PART_MIDDLE.y/10)][int(EL_S_PART_MIDDLE.x/10)] != 1 and playground[len(playground)-int(EL_S_PART_MIDDLE.y/10)][int(EL_S_PART_MIDDLE.x/10)+1] != 1:
                EL_S_PART_TOP.y -= FALLING_SPEED
                EL_S_PART_MIDDLE.y -= FALLING_SPEED
                EL_S_PART_BOTTOM.y -= FALLING_SPEED
                if moving_left and EL_S_PART_MIDDLE.x > 0 and playground[len(playground)-int(EL_S_PART_MIDDLE.y/10)-1][int(EL_S_PART_MIDDLE.x/10)-1] != 1 and playground[len(playground)-int(EL_S_PART_TOP.y/10)-1][int(EL_S_PART_TOP.x/10)-1] != 1 and playground[len(playground)-int(EL_S_PART_BOTTOM.y/10)-1][int(EL_S_PART_BOTTOM.x/10)-1] != 1:
                    EL_S_PART_TOP.x -= MOVING_SPEED
                    EL_S_PART_MIDDLE.x -= MOVING_SPEED
                    EL_S_PART_BOTTOM.x -= MOVING_SPEED
                if moving_right and EL_S_PART_MIDDLE.x < WINDOW_WIDTH-SQUARE_LENGTH*3 and playground[len(playground)-int(EL_S_PART_MIDDLE.y/10)-1][int(EL_S_PART_MIDDLE.x/10)+3] != 1 and playground[len(playground)-int(EL_S_PART_TOP.y/10)-1][int(EL_S_PART_TOP.x/10)+1] != 1 and playground[len(playground)-int(EL_S_PART_BOTTOM.y/10)-1][int(EL_S_PART_BOTTOM.x/10)+1] != 1:
                    EL_S_PART_TOP.x += MOVING_SPEED
                    EL_S_PART_MIDDLE.x += MOVING_SPEED
                    EL_S_PART_BOTTOM.x += MOVING_SPEED
            else: 
                updatePlayground("S", EL_S_PART_MIDDLE.x, EL_S_PART_MIDDLE.y, EL_S_PART_MIDDLE.width)
                pyglet.clock.unschedule(update)
        else: 
            updatePlayground("S", EL_S_PART_MIDDLE.x, EL_S_PART_MIDDLE.y, EL_S_PART_MIDDLE.width)
            pyglet.clock.unschedule(update)
    pyglet.clock.schedule_interval(update, UPDATE_INTERVAL)
    return EL_S_PART_TOP, EL_S_PART_MIDDLE, EL_S_PART_BOTTOM
    
def create_T(color):
    EL_T_PART_TOP = shapes.Rectangle(START_POS_X+SQUARE_LENGTH, WINDOW_HEIGHT-SQUARE_LENGTH, SQUARE_LENGTH, SQUARE_LENGTH, color=color, batch=batch)
    EL_T_PART_BOTTOM = shapes.Rectangle(START_POS_X, WINDOW_HEIGHT-SQUARE_LENGTH*2, SQUARE_LENGTH*3, SQUARE_LENGTH, color=color, batch=batch)
    def update(dt): # update element position, cite from ChatGPT. [Code segment illustrating 怎么更新rectangle的位置，每秒更新一次，高度减少 (How to update the position of a rectangle, decrease its height every second)] Retrieved from OpenAI, 2023, https://openai.com. Accessed 27 April 2023.
        if EL_T_PART_BOTTOM.y > 0:
            if playground[len(playground)-int(EL_T_PART_BOTTOM.y/10)][int(EL_T_PART_BOTTOM.x/10)] != 1 and playground[len(playground)-int(EL_T_PART_BOTTOM.y/10)][int(EL_T_PART_BOTTOM.x/10)+1] != 1 and playground[len(playground)-int(EL_T_PART_BOTTOM.y/10)][int(EL_T_PART_BOTTOM.x/10)+2] != 1:
                EL_T_PART_TOP.y -= FALLING_SPEED
                EL_T_PART_BOTTOM.y -= FALLING_SPEED
                if moving_left and EL_T_PART_BOTTOM.x > 0 and playground[len(playground)-int(EL_T_PART_BOTTOM.y/10)-1][int(EL_T_PART_BOTTOM.x/10)-1] != 1 and playground[len(playground)-int(EL_T_PART_TOP.y/10)-1][int(EL_T_PART_TOP.x/10)-1] != 1:
                    EL_T_PART_TOP.x -= MOVING_SPEED
                    EL_T_PART_BOTTOM.x -= MOVING_SPEED
                if moving_right and EL_T_PART_BOTTOM.x < WINDOW_WIDTH-SQUARE_LENGTH*3 and playground[len(playground)-int(EL_T_PART_BOTTOM.y/10)-1][int(EL_T_PART_BOTTOM.x/10)+3] != 1 and playground[len(playground)-int(EL_T_PART_TOP.y/10)-1][int(EL_T_PART_TOP.x/10)+1] != 1:
                    EL_T_PART_TOP.x += MOVING_SPEED
                    EL_T_PART_BOTTOM.x += MOVING_SPEED
            else: 
                updatePlayground("T", EL_T_PART_BOTTOM.x, EL_T_PART_BOTTOM.y, EL_T_PART_BOTTOM.width)
                pyglet.clock.unschedule(update)
        else: 
            updatePlayground("T", EL_T_PART_BOTTOM.x, EL_T_PART_BOTTOM.y, EL_T_PART_BOTTOM.width)
            pyglet.clock.unschedule(update)
    pyglet.clock.schedule_interval(update, UPDATE_INTERVAL)
    return EL_T_PART_TOP, EL_T_PART_BOTTOM

elements_list = ["I","O","L","J","Z","S","T"]

def updatePlayground(element_index, pos_x, pos_y, el_width):
    if element_index == "I":
        for i in range(int(el_width/10)):
            playground[len(playground)-1-int(pos_y/10)][int(pos_x/10)+i] = 1
    elif element_index == "O":
        for i in range(int(el_width/10)):
            playground[len(playground)-2-int(pos_y/10)][int(pos_x/10)+i] = 1
            playground[len(playground)-1-int(pos_y/10)][int(pos_x/10)+i] = 1
    elif element_index == "L":
        for i in range(int(el_width/10)):
            playground[len(playground)-1-int(pos_y/10)][int(pos_x/10)+i] = 1
        playground[len(playground)-2-int(pos_y/10)][int(pos_x/10)+int(el_width/10)-1] = 1
    elif element_index == "J":
        for i in range(int(el_width/10)):
            playground[len(playground)-1-int(pos_y/10)][int(pos_x/10)+i] = 1
        playground[len(playground)-2-int(pos_y/10)][int(pos_x/10)] = 1
    elif element_index == "Z":
        for i in range(int(el_width/10)):
            playground[len(playground)-1-int(pos_y/10)][int(pos_x/10)+i] = 1
        playground[len(playground)-2-int(pos_y/10)][int(pos_x/10)+int(el_width/10)-1] = 1
        playground[len(playground)-int(pos_y/10)][int(pos_x/10)] = 1
    elif element_index == "S":
        for i in range(int(el_width/10)):
            playground[len(playground)-1-int(pos_y/10)][int(pos_x/10)+i] = 1
        playground[len(playground)-int(pos_y/10)][int(pos_x/10)+int(el_width/10)-1] = 1
        playground[len(playground)-2-int(pos_y/10)][int(pos_x/10)] = 1
    elif element_index == "T":
        for i in range(int(el_width/10)):
            playground[len(playground)-1-int(pos_y/10)][int(pos_x/10)+i] = 1
        playground[len(playground)-2-int(pos_y/10)][int(pos_x/10)+1] = 1
        
        
    for i in range(len(playground)):
        for j in range(len(playground[i])):
            print(playground[i][j], end=' ')
        print()
        
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
    # interact with M5 Stack cite from "demo_vis.py"
    global moving_left, moving_right
    if sensor.get_value('accelerometer')['x'] > 0:
        moving_left = True
        moving_right = False
    else:
        moving_right = True
        moving_left = False
    #print('capabilities: ', sensor.get_value('accelerometer')['x'], "; moving left: ", moving_left, "; moving right: ", moving_right)
    
    # interact with M5 Stack cite from "demo_event.py"
    # click button_1 to exit
    def handle_button_1_press(data):
        if int(data) == 0:
            pyglet.app.exit()
    sensor.register_callback('button_1', handle_button_1_press)
    for element in elements:
        batch.draw()

pyglet.clock.schedule_interval(create_elements,5)
pyglet.gl.glClearColor(0.8,1,0.6,0.5) # change background color cite from: https://stackoverflow.com/questions/42470333/how-to-change-the-color-of-a-pyglet-window    
# run the pyglet application       
pyglet.app.run()