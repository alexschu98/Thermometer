#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import serial

# configure serial port
ser = serial.Serial()
ser.port = '/dev/ttyACM0'
ser.baudrate = 9600
ser.timeout = 5
ser.open()

plt.style.use('dark_background')

fig = plt.figure()
ax = fig.add_subplot(111)

xs = []
ys = []

for k in range(5):
    ser.read_all()

def anim(i, xs, ys):
    
    # parse from serial port
    line = ser.readline()
    line_list = line.split(b',')

    i = int(line_list[0])
    temp_float = float(line_list[1].split(b'\n')[0])

    xs.append(i)
    ys.append(temp_float)
    
    mean = np.sum(np.array(ys)) / len(ys) 

    ax.clear()
    ax.plot(xs, ys)

    plt.xticks(rotation=45, ha='right')

    plt.xlabel("t [s]")
    plt.ylabel("T [°C]")
    
    plt.title("T = {:.1f} °C | M: {:.1f} °C".format(temp_float, mean), fontsize=20)
    plt.axis([0, None, 19.9, 40.1])
    
ani = animation.FuncAnimation(fig, anim, fargs=(xs, ys), interval=1000)
plt.show()
