import socket
import numpy as np
import time
import random

IP = '127.0.0.1'
PORT = 5700

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

counter = 0
# coordinate x&y
x = 0.0
y = 0.0

# var frequency
sin_frequency = 1

while True:
    y = np.sin(sin_frequency * x)
    message = '{"coordinate(x,y)" : (' + str(x) + ',' + str(y) + ')}'
    print(message)
    if counter%random.randint(7,10) == 0:
        print('button1 released')
        print('button1 pressed')
    sock.sendto(message.encode(), (IP, PORT))

    x += 0.1
    counter += 1
    # change frequency
    sin_frequency += 0.01
    time.sleep(0.1)
    