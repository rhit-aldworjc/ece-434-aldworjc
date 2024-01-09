#!/usr/bin/env python3
# Based off: https://towardsdatascience.com/python-webserver-with-flask-and-raspberry-pi-398423cc6f5d

#imports for LED Matrix
import smbus
import time

#imports for Flask server
from flask import Flask, render_template, request

#Set up matrix busses
bus = smbus.SMBus(2)  # Use i2c bus 1
matrix = 0x70         # Use address 0x70

bus.write_byte_data(matrix, 0x21, 0)   # Start oscillator (p10)
bus.write_byte_data(matrix, 0x81, 0)   # Disp on, blink off (p11)
bus.write_byte_data(matrix, 0xe7, 0)   # Full brightness (page 15)

# setting up methods
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

#setup variables/constants
print("Welcome to Etch-a-sketch")
rows = 8
cols = 8

greens = [0 for i in range(cols)]
curr = [0,0]

#start flask server
app = Flask(__name__)

@app.route("/")
def index():
	red = updateboard(greens)
	bus.write_i2c_block_data(matrix, 0, getMessage(greens,red))
	
	return render_template('index.html')
	
@app.route("/<deviceName>/<action>")
def action(deviceName, action):
    if deviceName == 'matrix':
        print("button pressed")

    if action == "left" and curr[0] > 0:
        #left button code
        curr[0] = curr[0] -1
                
        red = updateboard(greens)
        bus.write_i2c_block_data(matrix, 0, getMessage(greens,red))
    if action == "down" and curr[1] > 0:
		#down button code
        curr[1] = curr[1] - 1
                
        red = updateboard(greens)
        bus.write_i2c_block_data(matrix, 0, getMessage(greens,red))
    if action == "up" and curr[1] < rows - 1:
		#up button code
        curr[1] = curr[1] + 1
                
        red = updateboard(greens)
        bus.write_i2c_block_data(matrix, 0, getMessage(greens,red))
    if action == "right" and curr[0] < rows -1:
		#right button code
        curr[0] = curr[0] + 1
                
        red = updateboard(greens)
        bus.write_i2c_block_data(matrix, 0, getMessage(greens,red))

    return render_template('index.html')
if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8081, debug=True)
