import socket
import numpy as np
import time

IP = '127.0.0.1'
PORT = 5700

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

counter = 0
#coordinate x&y
x = 0.0
y = 0.0

#var frequency
sin_frequency = 1

#if no button click, print with "normal" speed
while True:
    y = np.sin(sin_frequency * x)
    message = '{"coordinate(x,y)" : (' + str(x) + ',' + str(y) + ')}'
    print(message)

    sock.sendto(message.encode(), (IP, PORT))

    x += 0.1
    sin_frequency += 0.01
    time.sleep(0.1)
    