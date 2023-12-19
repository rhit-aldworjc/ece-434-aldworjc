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

eQEP = ['2','1']
COUNTERPATH = ['/dev/bone/counter/'+eQEP[0]+'/count0','/dev/bone/counter/'+eQEP[1]+'/count0']

ms = 100
maxCount = '1000000'

f1 = open(COUNTERPATH[0]+'/ceiling','w')
f1.write(maxCount);
f1.close();
f1 = open(COUNTERPATH[0]+'/count','r')
f1.seek(0)
olddataR = f1.read()[:-1]

f2 = open(COUNTERPATH[1]+'/ceiling','w')
f2.write(maxCount);
f2.close();
f2 = open(COUNTERPATH[1]+'/count','r')
f2.seek(0)
olddataL = f2.read()[:-1]

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
print("w = MOVE UP, s = MOVE DOWN, a = MOVE RIGHT, d = MOVE LEFT, space = CLEAR BOARD")
print("hit enter after move to submit")
print("Note: clearing board does not reset currsor (just like a real etch-sketch")

#Main loop
while True:
    red = updateboard(greens)
    bus.write_i2c_block_data(matrix, 0, getMessage(greens,red))
    f1.seek(0)
    dataR = f1.read()[:-1]
    f2.seek(0)
    dataL = f2.read()[:-1]
    if dataL > olddataL and curr[0] > 0:
        curr[0] = curr[0] - 1
    elif dataL < olddataL and curr[0] < cols -1:
        curr[0] = curr[0] + 1
    elif dataR > olddataR and curr[1] > 0:
        curr[1] = curr[1] - 1
    elif dataR < olddataR and curr[1] < rows - 1:
        curr[1] = curr[1] + 1
    #elif com ==" ":
    #    clearboard(greens)

    olddataR = dataR
    olddataL = dataL
    time.sleep(ms/1000)
