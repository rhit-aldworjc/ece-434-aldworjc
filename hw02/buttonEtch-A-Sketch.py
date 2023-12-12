#!/usr/bin/env python3
# //////////////////////////////////////
# 	getset.py
#  Get the value of P8_16 and write it to P9_14. 
#     P8_16 is line 14 on chip 1.  P9_14 is line 18 of chip 1.
# 	Wiring:	Attach a switch to P8_16 and 3.3V and an LED to P9_14.
# 	Setup:	sudo apt uupdate; sudo apt install libgpiod-dev
#           Run: gpioinfo | grep -i -e chip -e P9_14 to find chip and line numbers
# 	See:	https://github.com/starnight/libgpiod-example/blob/master/libgpiod-led/main.c
# //////////////////////////////////////
# Based on https://git.kernel.org/pub/scm/libs/libgpiod/libgpiod.git/tree/bindings/python/examples

import gpiod
import sys

CONSUMER='getset'
CHIP='1'
getoffsets=[14,15,12,13,17]# P8_16, P8_15, P8_12, P8_11, P9_23

chip = gpiod.Chip(CHIP)

getlines = chip.get_lines(getoffsets)
getlines.request(consumer=CONSUMER, type=gpiod.LINE_REQ_DIR_IN)

def printboard(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            print(arr[i][j], end = " ")
        print()
    print()
        
def clearboard(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            arr[i][j] = '.'

print("Welcome to Etch-a-sketch")
com = input("Number of Rows: ")
rows = int(com)
com = input("Number of Columns: ")
cols = int(com)

board = [["." for i in range(cols)] for j in range(rows)]

curr = [0,0]

print("Controls:")
print("Button1 = MOVE UP, Button2 = MOVE DOWN, Button3 = MOVE RIGHT, Button4 = MOVE LEFT, Button5 = CLEAR BOARD")
print("Note: clearing board does not reset currsor (just like a real etch-sketch)")
print("Hit ^C to stop")
ovals = getlines.get_values()
printboard(board)
while True:
    vals = getlines.get_values()
    
    board[curr[0]][curr[1]] = 'X'
    if vals != ovals:
        printboard(board)
    if vals[0] == 1 and curr[0] > 0 and vals[0] != ovals[0]:
        curr[0] = curr[0] - 1
    if vals[1] == 1 and curr[0] < cols -1 and vals[1] != ovals[1]:
        curr[0] = curr[0] + 1
    if vals[2] == 1 and curr[1] > 0 and vals[2] != ovals[2]:
        curr[1] = curr[1] - 1
    if vals[3] == 1 and curr[1] < rows - 1 and vals[3] != ovals[3]:
        curr[1] = curr[1] + 1
    if vals[4] == 1 and vals[4] != ovals[4]:
        clearboard(board)
    ovals = vals
