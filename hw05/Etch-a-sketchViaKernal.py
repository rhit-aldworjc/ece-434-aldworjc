#!/usr/bin/env python3
#Author: Jack Aldworth
#Date: 12/17/2023
#A recreation of an etch-a-sketch using a 8x8 LED matrix and two rotary encoders

import smbus
import time
#Set up Busses
bus = smbus.SMBus(2)  # Use i2c bus 1
matrix = 0x70         # Use address 0x70

bus.write_byte_data(matrix, 0x21, 0)   # Start oscillator (p10)
bus.write_byte_data(matrix, 0x81, 0)   # Disp on, blink off (p11)
bus.write_byte_data(matrix, 0xe7, 0)   # Full brightness (page 15)

PATH = '/sys/class/i2c-adapter/i2c-2/2-0053/iio:device1/'

fx = open(PATH+'in_accel_x_raw','r');
fx.seek(0);
fy = open(PATH+'in_accel_y_raw','r');
fy.seek(0);
# setting up deffinitions
def clearboard(arr):
    for i in range(len(arr)):
        arr[i] = 0

def updateboard(greens):
    reds = [0 for i in range(2*8)]
    reds[curr[1]] = 1 << (7 - curr[0])
    greens[curr[1]] = greens[curr[1]] | (1 << (7 - curr[0]))
    return reds

def getMessage(greens,reds):
    out = [0 for i in range(2*8)]
    for i in range(8):
        out[2*i] = greens[i]
        out[2*i+1] = reds[i]
    return out
#setup before main loop
print("Welcome to Etch-a-sketch")
rows = 8
cols = 8

greens = [0 for i in range(cols)]
curr = [0,0]
print("Controls:")
print("Tilt in the direction you want to go")

#Main loop
while True:
    red = updateboard(greens)
    bus.write_i2c_block_data(matrix, 0, getMessage(greens,red))
    fx.seek(0)
    xdir = int(fx.read()[:-1])
    fy.seek(0)
    ydir = int(fy.read()[:-1])
    if ydir < 70 and curr[0] > 0:
        curr[0] = curr[0] - 1
    elif ydir > 70 and curr[0] < cols -1:
        curr[0] = curr[0] + 1
    if xdir > 70 and curr[1] > 0:
        curr[1] = curr[1] - 1
    elif xdir < 70 and curr[1] < rows - 1:
        curr[1] = curr[1] + 1
    #elif com ==" ":
    #    clearboard(greens)
    time.sleep(0.2)
