#!/usr/bin/env python3

#Author: Jack Aldworth
#Date Made: 12/4/2023
#Description: A simple recreation of and Etch-a-sketch on a computer

import smbus
import time

bus = smbus.SMBus(2)
matrix = 0x70

def printboard(arr):
    for i in range(len(arr)):

        for j in range(len(arr[i])):
            print(arr[i][j], end = " ")
        print()

def clearboard(arr):
    for i in range(len(arr)):

        for j in range(len(arr[i])):
            arr[i][j] = '.'

def getgreens(arr):
    out = [0 for i in range(cols)]

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            out[i] = 2*out[i] + arr[i][j]
    return out

def getreds(arr):
    out = [0 for i in range(cols)]
    out[curr[0]] = 1 << (8 - curr[1])
    return out

def getMessage(greens,reds):
    out = [0 for i in range(2*8)]
    for i in range(8):
        out[2*i] = greens[i]
        out[2*i+1] = reds[i]
    return out

print("Welcome to Etch-a-sketch")
rows = 8
cols = 8

board = [[0]*cols]*rows


curr = [0,0]
print("Controls:")
print("w = MOVE UP, s = MOVE DOWN, a = MOVE RIGHT, d = MOVE LEFT, space = CLEAR BOARD")
print("hit enter after move to submit")
print("Note: clearing board does not reset currsor (just like a real etch-sketch")

while True:
    board[curr[0]][curr[1]] = 1
    bus.write_i2c_block_data(matrix, 0, getMessage(getgreens(board),getreds(board)))
    com = input("Move:")
    if com == "w" and curr[0] > 0:
        curr[0] = curr[0] - 1
    elif com == "s" and curr[0] < cols -1:
        curr[0] = curr[0] + 1
    elif com == "a" and curr[1] > 0:
        curr[1] = curr[1] - 1
    elif com == "d" and curr[1] < rows - 1:
        curr[1] = curr[1] + 1
    elif com ==" ":
        clearboard(board)
    else:
        print("not a valid move")